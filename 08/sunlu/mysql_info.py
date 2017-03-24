# coding=utf8
import MySQLdb
import sys
import datetime

reload(sys)
sys.setdefaultencoding('utf8')

dbhost = '192.168.1.13'
dbuser = 'root'
dbpasswd = '123456'
database = 'ops'
db = MySQLdb.connect(host=dbhost, user=dbuser, passwd=dbpasswd, db=database, charset='utf8')




def nowtime():
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return now


def check_users(username, password=''):
    users_list = users_all()
    for user in users_list:
        if username == user['name'] and password == user['password']:
            return 0
        else:
            pass


def gettables(tablename):
    cur = db.cursor()
    cur.execute('desc %s' % (tablename))
    tablenames = [row[0] for row in cur.fetchall()]
    db.commit()
    cur.close()
    return tablenames


def users_all():
    # users = []
    fields = gettables('users')
    sql = 'select %s from users' % (",".join(fields))
    cur = db.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    users = [dict((k, row[i]) for i, k in enumerate(fields)) for row in result]
    # for row in result:
    #     user = {}
    #     for k, v in enumerate(fields):
    #         user[v] = row[k]
    #     users.append(user)
    cur.close()
    return users

def user_one(names):
    fields = gettables('users')
    sql = 'select %s from users where name="%s"' % (",".join(fields), names)
    cur = db.cursor()
    cur.execute(sql)
    res = cur.fetchone()
    d = [dict(zip(fields, [i for i in res]))]
    cur.close()
    return d


def insert_user(d):
    # d = eval(d)
    del d['re_password']
    sql = 'insert into users (%s,create_time) values (%s,"%s")' % (
        ','.join(d.keys()), ','.join(['"%s"' % d[i] for i in d.keys()]), nowtime())
    cur = db.cursor()
    cur.execute(sql)
    db.commit()
    cur.close()


def del_user(ids):
    sql = 'delete from users where id=%d' % (int(ids))
    cur = db.cursor()
    cur.execute(sql)
    db.commit()
    cur.close()


def upuser_dict(ids):
    fields = ['name', 'name_cn', 'password', 'email', 'mobile', 'role', 'status']
    d = dict((i, user[i]) for user in users_all() if ids == user['id'] for i in fields)
    return d

# print upuser_dict('admin')


def up_user(data,ids):
    List = ['%s="%s"' %(k, v) for k,v in data.iteritems()]
    sql = 'update users set %s where id=%s' % (','.join(List), ids)
    cur = db.cursor()
    cur.execute(sql)
    db.commit()
    cur.close()


def get_one(field, sp_field, sp_field_val):
    sql = 'select %s from users where %s="%s"' % (field, sp_field, sp_field_val)
    cur = db.cursor()
    cur.execute(sql)
    result = cur.fetchone()
    return result


def up_passwd(data,ids):
    List= ['%s="%s"' %(k, v[0]) for k, v in data.iteritems() if k <> 're_password']
    sql = 'update users set %s where id=%s' % (','.join(List), ids)
    cur = db.cursor()
    cur.execute(sql)
    db.commit()
    cur.close()

def insert_time(username):
    sql = 'update users set last_time="%s" where name="%s"' %(nowtime(), username)
    cur = db.cursor()
    cur.execute(sql)
    db.commit()
    cur.close()

def get_all(data,role):
    # data = {u'status': 0L, u'name': u'admin', u'mobile': u'18621070871', u'name_cn': u'\u5b59\u7490', u'id': 21L,
    #  u'create_time': datetime.datetime(2016, 8, 14, 15, 50, 2), u'role': u'1', u'password': u'123456',
    #  u'last_time': datetime.datetime(2016, 8, 21, 16, 31, 8), u'email': u'289763560@qq.com'}
    users = users_all()
    # print users
    # List = [user for user in users for k, v in user.iteritems() if data == user[k]]
    List = []
    for user in users:
        for k, v in user.iteritems():
            if role == '1':
                if data == user[k]:
                    List.append(user)
            else:
                if data == user[k] and role == user['role']:
                    List.append(user)


    return List
# print get_all('admin')

# print get_all('sunlu','2')