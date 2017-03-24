#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-08-06 18:41:53
# @Author  : yang ke (jack_keyang@163.com)

import MySQLdb as mysql

conn = mysql.Connect(host="localhost",user="root", passwd="123456",db="reboot10",charset="utf8")
curs = conn.cursor()

def get_userlist(fieldlist):
    sql = "select %s from users"%",".join(fieldlist)
    users = []
    curs.execute(sql)
    result = curs.fetchall()
    for row in result:
        user = {}
        for i, k in enumerate(fieldlist):
            user[k] = row[i]
        users.append(user)
    return users

def getone(uid):
    field_lsit = ["name","name_cn","email","mobile","role","status"]
    sql = "select %s from users where id = %s"%(",".join(field_lsit),uid)
    curs.execute(sql)
    result = curs.fetchone()
    conn.commit()
    userinfo = {}
    for i, k in enumerate(field_lsit):
        userinfo[k] = result[i]
    return userinfo

def add_user(fieldlist):
    sql = 'insert into users(name,name_cn,password,email,mobile,role,status)values("%s")'%'","'.join(fieldlist)
    curs.execute(sql)
    conn.commit()

def del_user(uid):
    sql = "delete from users where id=%s"%uid
    curs.execute(sql)
    conn.commit()

def up_user(fielddic):
    sql = "update users set email='%(email)s',mobile='%(mobile)s',role='%(role)s',status='%(status)s' where name='%(name)s'"%(fielddic)
    curs.execute(sql)
    conn.commit()