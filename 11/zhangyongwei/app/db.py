#coding: utf-8

import MySQLdb
from datetime import datetime

def auth_user(username, password):
    sql = "select * from users where name='%s' and password='%s'" % (username, password)
    sql_count, rt_list = execute_sql(sql)
    if sql_count == 0:
        return False
    last_login = datetime.now()
    sql1 = "update users set last_time='%s' where name='%s'" % (last_login,username)
    execute_sql(sql1, fetch=False)
    return True


def user_list():
    columns = ('id', 'name', 'name_cn', 'password', 'email', 'mobile', 'role', 'status', 'create_time', 'last_time')
    sql = 'select %s from users' % ','.join(columns)
    sql_count, rt_list = execute_sql(sql)
    users = []
    for i in rt_list:
        users.append(dict(zip(columns, i)))
    return users


def user_regedit_check(user_data):
    for v in user_data.values():
        if v == '':
            error = {"status":1, "msg":"All msg can't be null"}
            return error
    if user_check(user_data['name']):
        error = {"status":1, "msg":'user %s exist' % (user_data['name'])}
        return error
    if user_data['password'] != user_data['repwd']:
        error = {"status":1, "msg":"password and repwd are not same"}
        return error
    error = {"status":0, "msg":'success'}
    return error


def user_check(name):
    sql = "select * from users where name='%s'" % (name)
    sql_cnt, rt_list = execute_sql(sql)
    if sql_cnt !=0:
        return True
    return False


def get_user_role(name):
    columns = ('id', 'name', 'name_cn', 'password', 'email', 'mobile', 'role', 'status', 'create_time', 'last_time')
    sql = "select %s from users where name='%s'" % (','.join(columns), name)
    sql_cnt, rt_list = execute_sql(sql)
    return dict(zip(columns,rt_list[0])).get('role','user')


def user_info(name):
    columns = ('id', 'name', 'name_cn', 'password', 'email', 'mobile', 'role', 'status', 'create_time', 'last_time')
    sql = "select %s from users where name='%s'" % (','.join(columns), name)
    sql_cnt, rt_list = execute_sql(sql)
    return dict(zip(columns,rt_list[0]))


def user_add(user_data):
    columns = ['name', 'password', 'name_cn', 'email', 'mobile', 'role', 'status', 'create_time', 'last_time']
    sql = "insert into users(%s) values(%s)" % (','.join(columns),','.join(['"%s"' % user_data[k] for k in columns]))
    execute_sql(sql, fetch=False)
    return True


def user_update(user_name, user_data):
    if len(user_data['mobile']) != 11:
        return {'code': 1, 'errmsg': '手机位数不正确'}
    data = ",".join(["%s='%s'" % (k, v) for k, v in user_data.items()])
    sql = "update users set %s where name='%s'" % (data, user_name)
    if execute_sql(sql, fetch=False):
        return {'code': 0, 'errmsg': '更新成功'}
    else:
        return {'code':1, 'errmsg':'更新失败'}



def user_update_oneself(user_name, user_data):
    if len(user_data['mobile']) != 11:
        return {'code': 1, 'errmsg': '手机位数不正确'}
    data = ",".join(["%s='%s'" % (k, v) for k, v in user_data.items()])
    sql = "update users set %s where name='%s'" % (data, user_name)
    if execute_sql(sql, fetch=False):
        return {'code': 0, 'errmsg': '更新成功'}
    else:
        return {'code':1, 'errmsg':'更新失败'}


def get_user_by_id(id):
    columns = ('id', 'name', 'name_cn', 'password', 'email', 'mobile', 'role', 'status', 'create_time', 'last_time')
    sql = 'select %s from users where id=%s' % (','.join(columns), id)
    sql_cnt, rt_list = execute_sql(sql)
    return dict(zip(columns,rt_list[0]))


def user_del(id):
    sql = 'delete from users where id=%s' % (id)
    sql_cnt, rt_list = execute_sql(sql, fetch=False)
    if sql_cnt != 0:
        return True
    return False

def change_pass_admin(name, new_pass):
    if new_pass == '':
        return {'code': 1, 'errmsg': '密码不能为空'}
    sql = "update users set password='%s' where name='%s'" % (new_pass, name)
    if execute_sql(sql, fetch=False):
        return {'code': 0, 'errmsg': '更新成功'}
    else:
        return {'code':1, 'errmsg':'更新失败'}


def change_pass(login_name, name,old_pass,new_pass):
    if old_pass == '' or new_pass == '':
        return {'code': 1, 'errmsg': '密码不能为空'}
    sql = "select password from users where name='%s'" % (name)
    sql_cnt, rt_list = execute_sql(sql)
    pass_in_db = ''.join(rt_list[0]).strip()
    if old_pass != pass_in_db:
        return {'code': 1, 'errmsg': '原始密码输入错误'}
    sql = "update users set password='%s' where name='%s'" % (new_pass, name)
    if execute_sql(sql, fetch=False):
        return {'code': 0, 'errmsg': '更新成功'}
    else:
        return {'code':1, 'errmsg':'更新失败'}


def execute_sql(sql, fetch=True):
    conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='123.com', port=3306, db='reboot10', charset='utf8')
    cur = conn.cursor()
    sql_count = 0
    rt_list = []
    if fetch:
        sql_count = cur.execute(sql)
        rt_list = cur.fetchall()
    else:
        sql_count = cur.execute(sql)
        conn.commit()

    cur.close()
    conn.close()
    return sql_count, rt_list


if __name__ == '__main__':
    change_pass('nmshuishui','1','1')
