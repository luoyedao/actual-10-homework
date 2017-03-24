#!/usr/bin/env python
#coding=utf-8

#注册账号


f=open("user.txt","a+")
d={}
for i in f.readlines():
  u=i.strip("\n").split(":")[0]
  d[u]=i.strip("\n").split(":")[1]

while True:
  user=raw_input("请输入你的账号：")
  if not user:
    print "请输入用户名..."
    continue
  elif user in d:
    print "%s 账号已被使用，请重新输入..." % (user)
    continue
  passwd=raw_input("请输入你的密码：")
  passre=raw_input("请输入你的密码：")
  if passwd and passwd == passre:
    f.write('%s:%s\n' %(user,passwd))
    print "恭喜! %s 账号注册成功！！" % (user)
    break
  else:
    print "密码不匹配，请重新输入！"
    continue
f.close()
