#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
def open_file(file_name):
    with open('passwd.txt','a+') as f:
        passwd = {}
        for line in f.readlines():
            tmp = line.rstrip('\n').split(":")
            passwd[tmp[0]] = tmp[1]
    return passwd

def register(passwd):
    while True:
        user = raw_input('please input your name :')
        if passwd.has_key(user) == True:
            print 'this name has registered , please input another one.'
            continue
        else:
            password = str(raw_input('please input your password :')).strip()
            pwd = str(raw_input('please input your password again :')).strip()
            if  password == pwd:
                passwd[user] = pwd
                print "register successfully!!!"
                u = str(user)
                p = str(pwd)
                with open('passwd.txt','a+') as ff:
                    ff.write('%s:%s\n'%(u,p))
                    break
            else:
                pwd = raw_input('the second time input wrong , please input your password again :')
                continue
def login(passwd):
    while True:
        username = str(raw_input('please input your name :')).strip()
        if passwd.has_key(username) == True:
            secret = str(raw_input('please input your password :')).strip()
            if str(secret) == str(passwd[username]):
                print '%s , login successfully , welcome back !'%(username)
                break
            else:
                secret2 = raw_input('passwd error , please input your password agagin :')
                if str(secret2) == str(passwd[username]):
                    print '%s , login successfully , welcome back !'%(username)
                else:
                    print '2 times wrong error , you were locked !!!'
                    break
        else:
            user = raw_input('username not exist , please input your name again :')
            break
def main():
    print 'register : 1 ----- login : 2'
    input = raw_input('inter your operation:')
    dict_passwd = open_file('passwd.txt')
    if input == '1':
        register(dict_passwd)
    elif input == '2':
        login(dict_passwd)
    else:
        input('input error , please reinput :')
main()
