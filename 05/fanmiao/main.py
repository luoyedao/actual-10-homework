#coding=UTF-8


def get_user():
	dic={}
	with open('user.txt') as f:
		for line in f:
			tmp = line.strip().split(":")
			dic.setdefault(tmp[0],tmp[1])
	return dic


def add_user(username,passwd):
	with open('user.txt','a') as f:
		f.write("%s:%s\n" %(username,passwd))


def del_user(user):
	dic=get_user()
	del dic[user]
 	with open('user.txt','w') as f:
		for i in dic:
			f.write("%s:%s\n"%(i,dic[i]))
