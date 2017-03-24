#!/usr/bin/python
#coding:utf-8
import sys

def  get_UP(filename):
	with open(filename , "r") as f:
		mes_dict = {}
		for line in f :
			k,v = line.strip("\n").split(":")
			mes_dict[k] = v 
		return mes_dict

def write_lock(filename,str,p="None"):
	with open(filename,"a+") as w_f:
		w_f.write("%s:%s\n" %(str,p))
		print "用户%s已锁定".format(str)

def Login():
#	print "1111111111111"
	userName = raw_input("请输入用户名:").strip(" ")
	password = raw_input("请输入密码:")
	lock_u = get_UP("lock.txt")
	confirm_u = get_UP("users.txt")
	if userName in lock_u.keys():
		sys.exit( "用户已经锁定,请联系管理员处理!退出")
	for count in range(1,4):
#		print "2222222222222"
		if userName in confirm_u.keys() :
#			print "3333333333333333333333333333"
			if  password == confirm_u[userName]:
				sys.exit("登录成功")
			else:
				if count < 3:
					password = raw_input("第%d次输入密码,还有%d次可以输入: "%((count+1),(2-count)))
				else :
					write_lock("lock.txt",userName)
		else:
			print "用户不存在"
			break

if __name__ == '__main__':
	Login()


