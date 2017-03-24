#!/usr/bin/env python
#coding:utf-8

import MySQLdb as mysql
import time

conn=mysql.connect(host='localhost',user='root',passwd='123',db='reboot10',unix_socket='/app/mysql/data/mysql.sock',charset='utf8')
cur=conn.cursor()

def c_sel(fields,tb,cid=None):
  if cid:
    sql='select %s from %s where id=%s' % (','.join(fields),tb,cid)
    cur.execute(sql)
    result=cur.fetchone()
  else:
    sql='select %s from %s' % (','.join(fields),tb)
    cur.execute(sql)
    result=cur.fetchall()
  return result 

def c_add(fields,data,tb):
  sql='insert into %s(%s) values(%s)' % (tb,','.join(fields),','.join(['"%s"' % data[v] for v in fields])) #通过字段顺序循环提取生成列表
  cur.execute(sql)
  conn.commit()
  sql='select * from %s where name="%s"' %(tb,data['name'])
  cur.execute(sql)
  result=cur.fetchone()
  return result

def c_edit(data,tb):
  condition=['%s="%s"' % (k,v[0]) for k,v in data.items()]
  sql='update %s set %s where id=%s' % (tb,','.join(condition),data['id'][0])
  cur.execute(sql)
  conn.commit()

def c_del(cid,tb):
  sql='delete from %s where id=%s' % (tb,cid)
  cur.execute(sql)
  conn.commit()

