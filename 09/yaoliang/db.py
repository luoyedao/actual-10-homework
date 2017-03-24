#!/usr/bin/python
#coding:utf-8

import  MySQLdb as mysql

conn = mysql.connect(user='root',passwd='123456',host='localhost',db='reboot10')
cur = conn.cursor()

def userlist(name=None):
    users = []
    fields = ['id','name','name_cn','password','email','mobile','role','status']
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
    fields = ['id','name','name_cn','password','email','mobile','role','status']
    sql = "select %s from users where id='%s'"%(','.join(fields),id)
    print sql
    cur.execute(sql)
    result = cur.fetchone()
    user = {}
    for i,k in enumerate(fields):
        user[k] = result[i]
    return user

#def register(args):
#    sql = 'insert into users set %s'%','.join(args)
#    cur.execute(sql)
#    conn.commit()
    
def deluser(id):
    sql = "delete from users where name='%s'"%(id)
    cur.execute(sql)
    conn.commit()

def update(args,id):
    sql = "update users set %s where id=%s"%(','.join(args),id)
    cur.execute(sql)
    conn.commit()
