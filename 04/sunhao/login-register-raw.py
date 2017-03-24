#!/usr/local/bin/python
#-*- coding: UTF-8 -*-

f = open('passwd.txt','a+')
passwd = {}
for line in f.readlines():
    tmp = line.strip('\n').split(":")
    passwd[tmp[0]] = tmp[1]

while True:
    print 'register : 1 ----- login : 2'
    input = raw_input('inter your operation:')
    if input == '1':
        user = raw_input('please input your name :')
        if passwd.has_key(user) == True:
            print 'this name has registered , please input another one.'
            continue
        else:
            password = raw_input('please input your password :')
            pwd = raw_input('please input your password again :')
            if password == pwd:
                passwd[user] = pwd
                print "register successfully!!!"
                u = str(user)
                p = str(pwd)
                f.writelines(('%s:%s\n')%(u,p))
                f.close()
                break
            else:
                pwd = raw_input('the second time input wrong , please input your password again :')
                continue
    if input == '2':
        username = raw_input('please input your name :')
        if passwd.has_key(username) == True:
            secret = raw_input('please input your password :')
            if str(secret) == str(passwd[username]):
                print '%s , login successfully , welcome back !'%(username)
                break
            else:
                secret = raw_input('passwd error , please input your password agagin :')
                continue
        else:
            username = raw_input('username not exist , please input your name again :')
