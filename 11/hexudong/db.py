#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-08-13 18:59:48
# @Author  : yang ke (jack_keyang@163.com)

import MySQLdb as mysql

conn = mysql.connect(host="localhost",user="root",passwd="123.com",db="reboot10",charset="utf8")
conn.autocommit(True)
curs = conn.cursor()

def userlist(fields):
    sql = "select %s from users"%",".join(fields)
    curs.execute(sql)
    result = curs.fetchall()
    u_list = [dict((k,row[i]) for i, k in enumerate(fields)) for row in result]
    return u_list

def getone(where):
    fields = ["id","name","name_cn","mobile","email","role","status"]
    condition = '%s = "%s"' % (where.keys()[0],where.values()[0])
    sql = "select %s from users where %s" % (",".join(fields),condition)
    print sql
    curs.execute(sql)
    result = curs.fetchone()
    u_dict = dict((k, result[i])for i, k in enumerate(fields))
    print u_dict
    return u_dict

def modfiy(fields):
    data = ",".join(["%s='%s'"%(k,v) for k,v in fields.items()])
    sql = "update users set %s where id=%s "%(data,fields["id"])
    curs.execute(sql)
    conn.commit()

def adduser(fields):
    sql = "insert into users(%s)values('%s')"%(",".join(fields.keys()),"','".join(fields.values()))
    curs.execute(sql)
    conn.commit()

def delete(uid):
    sql = "delete from users where id=%s"%uid
    curs.execute(sql)
    conn.commit()

def checkuser(dict,fields):
    sql = "select %s from users where %s='%s'"%(','.join(fields),dict.keys()[0],dict.values()[0])
    print sql
    curs.execute(sql)
    result = curs.fetchone()
    #res = dict((k, result[i]) for i, k in enumerate(fields))
    res = {}
    for i, k in enumerate(fields):
        res[k] = result[i]
    return res

def modpasswd(dict):
    sql = "update users set password='%(password)s' where id=%(id)s"%dict
    curs.execute(sql)
    conn.commit()

def Userlist_idc(fields):
    sql = "select %s from idc"%",".join(fields)
    print sql
    curs.execute(sql)
    result = curs.fetchall()
    u_list = [dict((k,row[i]) for i, k in enumerate(fields)) for row in result]
    return u_list
