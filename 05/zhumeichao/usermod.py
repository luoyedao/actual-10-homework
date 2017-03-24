#!/usr/bin/env python
#coding=utf-8

#查询获取账号信息
def userlist(userfile):
  userinfo={}
  with open(userfile,'a+') as f:
    for i in f:
      u=i.strip("\n").split(":")[0]
      userinfo[u]=i.strip("\n").split(":")[1]
  return userinfo

#注册账号
def adduser(userinfo,userfile,user,passwd,passre):
  if not user:
    return "please input username and password...."
  elif user in userinfo:
    return "%s in use, please use others" % (user)
  if passwd and passwd == passre:
    with open(userfile,'a+') as f:
      f.write('%s:%s\n' %(user,passwd))
  else:
    return "user password no pass..."
  users=userlist(userfile)
  if user in users:
    return "%s zhuce seccess!!!" % (user)

#用户登陆
def userlogin(userinfo,user,passwd):
    if not user:
      return "plase input username and password"
    elif user not in userinfo:
      return "User not esxit...please create it."
    elif userinfo[user] == passwd:
      return 0
    else:
      return "User Password no pass..."
#删除用户
def deluser(userinfo,userfile,user):
   if user in userinfo:
     userinfo.pop(user)
     with open(userfile,'w+') as f:
       for k,v in userinfo.items():
         f.write('%s:%s\n' % (k,v))
