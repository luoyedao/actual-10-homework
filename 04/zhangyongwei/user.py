#coding: utf-8

def login():
	flag = True
	while flag:
		name = raw_input('please input your name:')
		password = raw_input('please input your password:')

		if login_required(name, password):
			print '登录成功！'
			flag = False
		else:
			print '用户名或密码不正确！'


def regedit():
	name = raw_input('please enter your name:').strip()
	if name_exist(name):
		print 'user %s is exist' % name
	else:
		password1 = raw_input('please enter your password:').strip()
		password2 = raw_input('please confirm your password:').strip()
		if password1 == password2:
			store(name, password1)
			print '用户注册成功！'
		else:
			print '注册失败，两次密码输入不一致！'


def name_exist(name):
	with open('db.txt') as f:
		for i in f.readlines():
				if name == i.strip('\n').split(',')[0].split(':')[1]:
					return True
				else:
					return False


def login_required(name, password):
	with open('db.txt') as f:
		for i in f:
			if name == i.strip('\n').split(',')[0].split(':')[1] and password == i.strip('\n').split(',')[1].strip('}')[-1]:
				return True
			else:
				return False


def store(name, password):
	f = open('db.txt', 'a+')
	f.write("{'name':%s, 'password':%s}\n" % (name, password))
	f.close()


x = raw_input('please choice login or regedit:')
if x == 'login':
	login()
elif x == 'regedit':
	regedit()
else:
	print 'Only login or regedit suport!'
