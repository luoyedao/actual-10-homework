#!/usr/bin/python
#coding:utf-8

import  MySQLdb as mysql

conn = mysql.connect(user='root',passwd='123456',host='localhost',db='reboot')
cur = conn.cursor()

def userlist(name=None):
    users = []
    fields = ['id','name','name_cn','password','email','mobile','create_time']            
    if not name:
        sql = "select %s from users"%','.join(fields)
        cur.execute(sql)
        result = cur.fetchall()
        for row in result:
            user = {}
            for i,k in enumerate(fields):
                user[k] = row[i]
            users.append(user)
        return users
    else:
        sql2 = "select %s from users where name='%s'"%(','.join(fields),name)
        cur.execute(sql2)
        result = cur.fetchone()
        user = {}
        for i,k in enumerate(fields):
            user[k] = result[i]
        return user

def update_list(id):
    fields = ['id','name','name_cn','password','email','mobile','role','status','create_time']
    sql = "select %s from users where id='%s'"%(','.join(fields),id)
    cur.execute(sql)
    result = cur.fetchone()
    user = {}
    for i,k in enumerate(fields):
        user[k] = result[i]
    return user

def register(*args):
    sql = 'insert into users(name,name_cn,password,email,mobile,role,status) values("%s")'%'","'.join(args)
    cur.execute(sql)
    conn.commit()
    
def deluser(id):
    sql = "delete from users where id='%s'"%(id)
    cur.execute(sql)
    conn.commit()

def update(*args):
    sql = "update users set name_cn='{}',password='{}',email='{}',mobile='{}',role='{}',status='{}' where id='{}'".format(*args)
    print sql
    cur.execute(sql)
    conn.commit()
