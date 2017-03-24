#coding:utf-8
import MySQLdb as mysql

conn=mysql.connect(user='root',host='127.0.0.1',passwd='123456',db='reboot10',charset='utf8')

conn.autocommit(True)
cur = conn.cursor()

def ulist(fields):
    sql = 'select %s from users' % ','.join(fields)
    cur.execute(sql)
    cur = cur.fetchall()
    user_list = [dict((k,row[i]) for i,k in enumerate(fields)) for row in result]
    return user_list

def getone(uid):
    fields = ['id', 'name', 'name_cn', 'email', 'mobile','role']
    sql = 'select %s from users where %s' % (','.join(fields),uid)
    cur.execute(sql)
    res = cur.fetchone()
    user_dict = dict((k,res[i]) for i,k in enumerate(fields))
    return user_dict

def modify(fields):
    condition = ["%s='%s'" % (k,v[0]) for k,v in data.items()]
    sql = 'update users set %s where id = ' % (','.join(condition),fields['name'])
    cur.execute(sql)

def insert(fields):
    sql = 'insert into users (%s) values (%s)' % (','.join(fields),','.join(['"%s"' % data[x] for x in fields]))    
    cur.execute(sql)
    
def delete(uid):
    sql = 'delete from users where id = %s' % uid
    cur.execute(sql)

def userinfo(fields,condition):
    sql = 'select %s from users where %s' % (','.join(fields),condition)
    cur.execute(sql)
    res = cur.fetchone()
    user_info = dict((k,res[i]) for i,k in enumerate(fields))
    return user_info




