#!/usr/bin/env python
#coding:utf-8
fo=open("user.txt")
'''
num=1
while True:
	line=fo.readline()
#	print repr(line)
	print "%s-->%s" %(num,line.rstrip("\n"))
	num+=1
	if len(line)==0:
		break
'''
#从文件中读取所有字符，并存为字典
dict1={}
content=fo.readlines()   #讲文件结果保存为列表
fo.close()
#print content
for user in content:
	name=user.rstrip("\n").split(":")[0]
#	print name
	dict1[name]=user.rstrip("\n").split(":")[1]
#print dict1

#判断用户的账号密码。都ok提示登陆成功。否则失败
count=0
while True:
	count+=1
	if count >3:
		print "对不起，您输入的错误次数过多，账户已锁定。请联系管理员"
		break
        name=raw_input('请输入用户姓名:').strip()
	if name not in dict1:
		print "用户名不存在，请重新输入！！"
		continue;
        password=raw_input('请输入您的密码:').strip()
        if password !=dict1[name]:
                print "密码输入有误"
                continue;
        else:
                print "恭喜你，登陆成功"
                break;
