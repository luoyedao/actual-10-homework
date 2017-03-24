#!/usr/bin/env python
# coding:utf-8
# @Date     : 2016-09-07 21:53
# @Author   : William/linqz

import MySQLdb as mysql

conn = mysql.connect(host='localhost',user='root',passwd='123456',db='yw',charset='utf8')
conn.autocommit(True)
cur =conn.cursor()

def check_user(user):
    fields = ['name','password','role','id']
    table = 'users'
    sql = 'select %s from %s where name="%s" and password="%s"' % (','.join(fields),table,user['name'],user['password'])
    result = cur.execute(sql)
    if not result:
        return result
    else:
        res = cur.fetchone()
        oneUser = dict((k,res[i]) for i,k in enumerate(fields))
        return oneUser

def selectOne(id):
    fields = ['id','name','name_cn','password','email','mobile','role','status']
    table = 'users'
    sql = 'select %s from %s where id="%s"' % (','.join(fields),table,id)
    cur.execute(sql)
    res = cur.fetchone()
    oneUser = dict((k,res[i]) for i,k in enumerate(fields))
    return oneUser

def updateOne(user):
    conditions = ['%s="%s"' % (k,v) for k,v in user.items()]
    table = 'users'
    sql = 'update %s set %s where id=%s' % (table,','.join(conditions),user['id'])
    cur.execute(sql)
    return

def selectAll():
    fields = ['id','name','name_cn','password','email','mobile','role']
    table = 'users'
    sql = 'select %s from %s' % (','.join(fields),table)
    cur.execute(sql)
    res = cur.fetchall()
    users = []
    for row in res:
        tmp = dict((k,row[i]) for i,k in enumerate(fields))
        users.append(tmp)
    return users

def deleteOne(id):

    table = 'users'
    sql = 'delete from %s where id="%s"' % (table,id)
    cur.execute(sql)
    return

def insertOne(user):
    fields = ['name','name_cn','password','email','mobile','role']
    table = 'users'
    sql = 'insert into %s (%s) VALUES (%s)' % (table,','.join(fields),','.join(['"%s"' % user[x] for x in fields]))
    cur.execute(sql)
    return
