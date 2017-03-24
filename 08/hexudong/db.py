#!/usr/bin/env python
# -*- coding:utf-8 -*-
#__author__ = 'Madon'
import MySQLdb as mysql

conn=mysql.connect(host='192.168.9.10',port=3306,user='admin',passwd='123.com',db='backstage',charset='utf8')
conn.autocommit(True)
cur = conn.cursor()

fields = ['id', 'name', 'name_cn', 'email', 'mobile']

#add fields
def Userlist():
    sql = "select %s from users" % ",".join(fields)
    cur.execute(sql)
    result = cur.fetchall()
    u_list = [dict((k,row[i]) for i,k in enumerate(fields)) for row in result]
    return u_list

def Checkuser(name):
    sql = "select password from users where name ='%s'" %name
    cur.execute(sql)
    password = cur.fetchone()
    return password[0]

def Request(conditions):
    sql ="insert into users set %s" %','.join(conditions)
    cur.execute(sql)
    conn.commit()

#add fields
def Getone(name):
    sql="select %s from users where name='%s'" %(','.join(fields),name)
    cur.execute(sql)
    result=cur.fetchone()
    u_dict=dict((k,result[i]) for i,k in enumerate(fields))
    return u_dict

#add fields
def Getid(id):
    sql="select %s from users where id='%s'" %(','.join(fields),id)
    cur.execute(sql)
    result=cur.fetchone()
    u_dict=dict((k,result[i]) for i,k in enumerate(fields))
    return u_dict

def Monfiy(conditions,id):
    sql ="update users set %s where id =%s" %(','.join(conditions),id)
    print sql
    cur.execute(sql)
    conn.commit()

def SelectPassword(id):
    fields = ['id','name']
    sql = "select %s from users where id = %s" % (','.join(fields),id)
    cur.execute(sql)
    result=cur.fetchone()
    u_dict=dict((k,result[i]) for i,k in enumerate(fields))
    return u_dict

def Checkpassword(id):
    sql = "select password from users where id ='%s'" %id
    cur.execute(sql)
    password = cur.fetchone()
    return password[0]

def Delete(id):
    sql ="delete from users where id ='%s'" %id
    cur.execute(sql)
    conn.commit()
