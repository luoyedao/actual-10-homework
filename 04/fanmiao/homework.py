#/usr/bin/python
#coding=UTF-8



def get_user():
	dict={}
	with open('user.txt') as f:
		for line in f:
			tmp = line.strip().split(":")
			dict.setdefault(tmp[0],tmp[1])
	return dict

def add_user(username,passwd):
	with open('user.txt','a') as f:
		f.write("%s:%s\n" %(username,passwd))



def register():
	while True:
		username=raw_input("请输入用户名:").strip()
		if len(username)==0:
			print "用户名不能为空"
		elif username in get_user():
			print "用户已经存在"
		else:
                        passwd=raw_input("请输入密码：").strip()
                        repass = raw_input("请再次输入密码：").strip()
                        if passwd !=repass:
                        	print "密码输入有误!"
                                continue
			else:
				add_user(username,passwd)
				print "注册成功!"
				break

def login():
	username=raw_input("请输入登录用户名:").strip()
	passwd=raw_input("请输入登录密码：").strip()
	dic=get_user()
	if not dic.has_key(username):
		print "用户不存在！请重新输入"
	elif dic[username] != passwd:
		print "用户名或者密码错误，请重新输入!"
	else:
		print "登录成功!"

def start():
	choice=raw_input("请选择登录或者注册用户:login or register?")
	if choice != 'login' and choice != 'register':
		print "hello"
	elif choice == 'login':
		login()
	else:
		register()

start()

