#!/usr/bin/env python
#coding=utf-8
import time

#查询获取账号信息
def userlist(userfile):
  userinfo={}
  with open(userfile,'a+') as f:
    for i in f:
      u=i.strip("\n").split(":")[0]
      userinfo[u]=i.strip("\n").split(":")[1]
  return userinfo

#注册账号
def adduser(userinfo,userfile):
  print "注册用户："
  while True:
    user=raw_input("请输入你的账号：")
    if not user:
      print "请输入用户名..."
      continue
    elif user in userinfo:
      print "%s 账号已被使用，请重新输入..." % (user)
      continue
    passwd=raw_input("请输入你的密码：")
    passre=raw_input("请输入你的密码：")
    if passwd and passwd == passre:
      with open(userfile,'a+') as f:
        f.write('%s:%s\n' %(user,passwd))
      print "恭喜! %s 账号注册成功！！" % (user)
      break
    else:
      print "密码不匹配，请重新输入！"
      continue

#用户登陆
def userlogin(userinfo):
  print "登陆用户："
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
    elif user not in userinfo:
      print "用户名不存在，请重新输入..."
      continue
    passwd=raw_input("请输入你的密码：")
    if userinfo[user] == passwd:
      print "%s 登陆成功！！！" %(user)
      break
    else:
      print "用户密码不正确，请重启输入..."

