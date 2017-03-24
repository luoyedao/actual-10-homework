#encoding: utf-8
import json

import MySQLdb

import gconf
from dbutils import execute_fetch_sql, execute_commit_sql


def get_users(wheres=[]):
    _columns = ('id', 'name', 'password', 'age')
    _sql = 'select * from users where 1=1'
    _args = []
    for _key, _value in wheres:
        _sql += ' AND {key} = %s'.format(key=_key)
        _args.append(_value)

    _count, _rt_list = execute_fetch_sql(_sql, _args)
    _rt = []
    for _line in _rt_list:
        #(6L, u'kk4', u'e10adc3949ba59abbe56e057f20f883e', 29L)
        _rt.append(dict(zip(_columns, _line)))
    return _rt


'''验证用户名，密码是否正确
返回值: True/False
'''
def validate_login(name, password):

    #_sql = 'select * from user where username="{username}" and password=md5("{password}")'.format(username=username, password=password)
    _sql = 'select * from users where name=%s and password=(%s)'
    _count, _rt_list = execute_fetch_sql(_sql, (name, password))
    return _count != 0


'''检查新建用户信息
返回值: True/False, 错误信息
'''
def validate_add_user(name, password, age):
    if name.strip() == '':
        return False, u'用户名不能为空'

    #检查用户名是否重复
    #get_user_by_name()
    if get_user_by_name(name):
        return False, u'用户名已存在'

    #密码要求长度必须大于等于6
    if len(password) < 6:
        return False, u'密码必须大于等于6'

    return True, ''


'''添加用户信息
'''
def add_user(name, password, age):
    _sql = 'insert into users(name, password, age) values(%s, md5(%s), %s)'
    _args = (name, password, age)
    execute_commit_sql(_sql, _args)


'''获取用户信息
'''
def get_user(uid):
    _rt = get_users([('id', uid)])
    return _rt[0] if len(_rt) > 0 else None


'''检查更新用户信息
返回值: True/False, 错误信息
'''
def validate_update_user(uid, name, password, age):
    if get_user(uid) is None:
        return False, u'用户信息不存在'

    return True, ''


'''更新用户信息
'''
def update_user(uid, name, password, age):
    _sql = 'update user set age=%s where id=%s'
    execute_commit_sql(_sql, (age, uid))

'''删除用户信息
'''
def delete_user(uid):
    _sql = 'delete from user where id=%s'
    execute_commit_sql(_sql, (uid, ))

def get_user_by_name(name):
    _rt = get_users([('name', name)])
    return _rt[0] if len(_rt) > 0 else None


