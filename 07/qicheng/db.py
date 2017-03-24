#coding: utf-8

import MySQLdb
from datetime import datetime


def auth_user(username, password):
    sql = 'select * from users where name=%s and password=%s'
    param = (username, password)
    sql_count, rt_list = execute_sql(sql, param)
    if sql_count == 0:
        return False
    last_login = datetime.now()
    sql1 = "update users set last_time=%s where name=%s"
    param1 = (last_login,username)
    sql_cnt, rt_list = execute_sql(sql1, param1, fetch=False)
    return True


def userlist():
    sql = 'select * from users'
    param = ()
    sql_count, rt_list = execute_sql(sql, param)
    columns = ('id', 'name', 'name_cn', 'password', 'email', 'mobile', 'role', 'status', 'create_time', 'last_time')
    users = []
    for i in rt_list:
        users.append(dict(zip(columns, i)))
    return users


def user_regedit_check(username,password,name_cn,email,mobile,role,status,create_time,last_time):
    if username=='' or password=='' or name_cn=='' or email=='' or mobile=='' or role=='' or status=='' or create_time=='' or last_time=='':
        return "False"
    return True


def user_add(username,password,name_cn,email,mobile,role,status,create_time,last_time):
    columns = ['username', 'password', 'name_cn', 'email', 'mobile', 'role', 'status', 'create_time', 'last_time']
    sql = "insert into users(name, password, name_cn, email, mobile, role, status, create_time, last_time) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    param = (username, password, name_cn, email, mobile, role, status, create_time, last_time)
    sql_cnt, rt_list = execute_sql(sql, param, fetch=False)
    return True


# def user_update(password,name_cn,email,mobile,role,status):
#     sql = "update users set password=%s,name_cn=%s,email=%s,mobile=%s,role=%s,status=%s"
#     param = (password, name_cn, email, mobile, role, status)
#     sql_cnt, rt_list = execute_sql(sql, param, fetch=False)
# def user_update(user_data):
#     data = ",".join(["%s='%s'" % (k, v) for k, v in user_data.items()])
#     sql = "update users set %s where name='%s'" % (data, user_data['name'])
#     execute_sql(sql, fetch=False)



def get_user_by_id(id):
    sql = 'select * from users where id=%s'
    param = (id,)
    sql_cnt, rt_list = execute_sql(sql, param)
    columns = ('id', 'name', 'name_cn', 'password', 'email', 'mobile', 'role', 'status', 'create_time', 'last_time')
    return dict(zip(columns,rt_list[0]))


def user_del(id):
    sql = 'delete from users where id=%s'
    param = (id,)
    sql_cnt, rt_list = execute_sql(sql, param, fetch=False)
    if sql_cnt != 0:
        return True
    return False


def execute_sql(sql,param,fetch=True):
    conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='123456', port=3306, db='reboot10', charset='utf8')
    cur = conn.cursor()
    sql_count = 0
    rt_list = []
    if fetch:
        sql_count = cur.execute(sql,param)
        rt_list = cur.fetchall()
    else:
        sql_count = cur.execute(sql,param)
        conn.commit()

    cur.close()
    conn.close()
    return sql_count, rt_list


if __name__ == '__main__':
    get_user_by_id(1)
