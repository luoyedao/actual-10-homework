#!/usr/bin/env python
#coding=utf-8

#用户登陆
import time

f=open("user.txt")
d={}
for i in f.readlines():
  u=i.strip("\n").split(":")[0]
  d[u]=i.strip("\n").split(":")[1]
c=0
while True:
  c+=1
  if c > 3:
    print "操作太频繁，请稍后再试..."
    time.sleep(5) 
  user=raw_input("请输入你的用户名：")
  if not user:
    print "请输入用户名。"
    continue
  elif user not in d:
    print "用户名不存在，请重新输入..."
    continue
  passwd=raw_input("请输入你的密码：")
  if d[user] == passwd:
    print "%s 登陆成功！！！" %(user)
    break
  else:
    print "用户密码不正确，请重启输入..."

f.close()
