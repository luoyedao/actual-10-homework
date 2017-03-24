#!/usr/bin/python
#coding:utf-8 
#filename:update_zhuce.py

import os
os.system("clear")

def jiance(filename):
	with open(filename,"r") as jiance_f:
		mes_dict = {}
		for line in jiance_f:
			k,v = line.strip().split(":")
			mes_dict[k] = v 
		return mes_dict

def user_mes():
	name = raw_input('请输入姓名：')
	getPassword = raw_input('请输入密码：')
	confirm_Password = raw_input('请再次输入密码：')
	return name,getPassword,confirm_Password

def success(filename,*name):
	with open(filename,"a+") as jilu_f:
		jilu_f.write("%s:%s\n" %(name[0],name[1]))

if __name__ == '__main__':
	while True :
		res = jiance("users.txt")
		show = lambda x:x
		tmp = user_mes()
		name , p , confirm_p = tmp[0] ,tmp[1] ,tmp[2]
		if ( name == "" ) or ( name in res.keys()):
			print show('用户名已经存在了或者为空,请重新输入：')
			continue
		if (p.isspace()) or ( p != confirm_p ) or (confirm_p.isspace()) :
			print show('密码不一致或者密码不能为空')
			continue
		else :
			success("users.txt",name,p)
			print show("注册成功")
			break

