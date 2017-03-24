#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-08-13 18:59:48
# @Author  : yang ke (jack_keyang@163.com)

import MySQLdb as mysql

conn = mysql.connect(host="localhost",user="root",passwd="123.com",db="reboot10",charset="utf8")
conn.autocommit(True)
curs = conn.cursor()

#获取用户信息列表
def userlist(fields):
    sql = "select %s from users"%",".join(fields)
    curs.execute(sql)
    result = curs.fetchall()
    u_list = [dict((k,row[i]) for i, k in enumerate(fields)) for row in result]
    return u_list

'''
    获取单个用户信息，可通过id或用户名查询该用户信息
    getone({"id":1})
    getone({"name":"admin"})

'''
def getone(dic):
    fields = ["id","name","name_cn","password","mobile","email","role"]
    sql = "select %s from users where %s='%s'"%(",".join(fields),dic.keys()[0],dic.values()[0])
    print sql
    curs.execute(sql)
    result = curs.fetchone()
    if result:
        u_dict = dict((k, result[i])for i, k in enumerate(fields))
        return u_dict
    else:
        return False

#修改用户信息
def modfiy(fields):
    print fields
    data = ",".join(["%s='%s'"%(k,v) for k,v in fields.items()])
    sql = "update users set %s where name='%s'"%(data,fields["name"])
    curs.execute(sql)
    conn.commit()

#添加用户
def adduser(fields):
    sql = "insert into users(%s)values('%s')"%(",".join(fields.keys()),"','".join(fields.values()))
    curs.execute(sql)
    conn.commit()

#删除用户
def delete(uid):
    sql = "delete from users where id=%s"%uid
    curs.execute(sql)
    conn.commit()

def modpasswd(dict):
    sql = "update users set password='%(password)s' where id=%(id)s"%dict
    print sql
    curs.execute(sql)
    conn.commit()

if __name__ == "__main__":
#    field = ["role"]
    #fields = ["id","name","name_cn","mobile","email","role","status"]

#    print checkuser({"name":"admin"},",".join(field))
    # delete(10)
    #print userlist(['id','name'])
    # print getone("11")
    #oprint checkuser({"name":"admin"})
    modfiy({'username': u'jack', 'status': u'1', 'name_cn': u'yang12323123', 'role': u'CU', 'email': u'123@qq.comadsfasdf'})
    #modfiy({"name":"jack","mobile":"12345","id":"1"})
    #modpasswd({"id":"22","password":"1234"})
    #mydb.delete(11)
