#!/usr/bin/env python
#coding:utf-8
f=open('user.txt','a+')
#单行写入
#f.write("wd:1234")
#多行写入
#names=["pc:123\n","panda:123\n"]
#f.writelines(names)
#交互式注册
while True:
	name=raw_input('请输入用户姓名:').strip()
	password=raw_input('请输入您的密码:').strip()
	repass=raw_input('请再次输入密码:').strip()
	if len(name)==0:
		print "用户名不能为空，请重新输入！！"
		continue;
	if len(password)==0 or password !=repass:
		print "密码输入有误"
		continue;
	else:
		print "恭喜你，注册成功"
		break;
f.write("%s:%s\n" %(name,password))
f.close()
