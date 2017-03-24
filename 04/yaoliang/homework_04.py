#!/usr/bin/python
#coding:utf-8

service = raw_input('which service you want to choose,register or login: ').strip()

def file():
    name_list = []
    with open('user.txt') as fo:
        for msg in fo:
            msg_name = msg.strip('\n').split(':')[0]
            name_list.append(msg_name)
    return name_list

def test(arr):
    while True:
        name = raw_input('Please Input your name: ').strip()
        passwd = raw_input('Please Input your password: ').strip()
        repasswd = raw_input('Please Input your password again: ').strip()

        if not name:
            print 'Name can not be null'
            continue
        elif name in arr:
            print 'User already exist.'
            continue
        elif not passwd or passwd!=repasswd:
            print 'Wrong password'
            continue
        else:
            return name,passwd
            break

def write_in(name,passwd):
    with open('user.txt','a+') as fo:
        fo.write('%s:%s\n'%(name,passwd))
        print 'Registration completed'

def register():
    res = file()
    name,passwd = test(res)
    write_in(name,passwd)

def login():
    with open('user.txt') as fo:
        d = {}
        for user in fo:
            user_name = user.strip('\n').split(':')[0]
            user_passwd = user.strip('\n').split(':')[1]
            d[user_name] = user_passwd 
    return d

def judge(arr):
    while True:
        name = raw_input('Please input your name: ').strip()
        passwd = raw_input('Please input your passwd: ').strip()

        if not name:
            print 'Name can not be null'
            continue
        elif name not in arr:
            print 'No such user'
            continue
        elif not passwd or passwd!=arr[name]:
            print 'Wrong password'
            continue
        else:
            print 'login successfully'
            break

def msg():
    if service=='login':
	arr = login()
 	judge(arr)
    elif service=='register':
	register()
    else:
	print 'No other choice.'	

msg()
