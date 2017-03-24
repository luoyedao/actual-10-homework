#!/usr/bin/env python
#encoding=utf-8

import MySQLdb as mysql
import time

conn=mysql.connect(host='localhost',user='root',passwd='123',db='reboot10',unix_socket='/app/mysql/data/mysql.sock',charset='utf8')
cur=conn.cursor()

#Select User
def seluser(fields,uid="None",name="None"):
  if uid != 'None':
    sql='select %s from users where id=%s' %(','.join(fields),uid)
    cur.execute(sql)
    result=cur.fetchone()
  elif name != 'None':
    sql='select %s from users where name="%s"' %(','.join(fields),name)
    cur.execute(sql)
    result=cur.fetchone()
  else:
    sql='select %s from users' % ','.join(fields)
    cur.execute(sql)
    result=cur.fetchall()
  return result

#Add User
def adduser(fields,userinfo):
  sql='insert into users(%s) values (%s)' %(','.join(fields),','.join(['"%s"' % userinfo[x] for x in fields]))
  cur.execute(sql)
  conn.commit()
  res=seluser(fields,name=userinfo['name'])
  return res

#Modification UserInfo
def moduser(uinfo):
  now=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
  uinfo['last_time']=[unicode(now)]
  condition=[ '%s="%s"' %(k,v[0]) for k,v in uinfo.items() ]
  uid=uinfo["id"][0]
  sql='update users set %s where id=%s'%(','.join(condition),uid)
  cur.execute(sql)
  conn.commit()
#Change Password
def chgpass(newpass,name):
  sql='update users set password="%s" where name="%s"' %(newpass,name)
  cur.execute(sql)
  conn.commit()

#Delete user
def killuser(uid):
  sql='delete from users where id="%s"' %(uid)
  cur.execute(sql)
  conn.commit()
