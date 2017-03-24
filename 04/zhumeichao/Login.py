#!/usr/bin/env python
#encoding=utf-8

import Usermod

num=raw_input("<登陆1> <注册2>\n 请输入操作数字：")
if num == '1':
   userinfo=Usermod.userlist("user.txt")
   Usermod.userlogin(userinfo)
elif num == '2':
   userinfo=Usermod.userlist("user.txt")
   Usermod.adduser(userinfo,"user.txt")
else:
  print "PS:\t输入数字1 ->登陆\n\t输入数字2 ->注册"
