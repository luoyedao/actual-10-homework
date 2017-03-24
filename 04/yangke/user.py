#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-07-23 18:35:18
# @Author  : yang ke (jack_keyang@163.com)


def get_user():
    userfile = "userlist.txt"
    userinfo = {}
    with open(userfile) as f:
        for line in f:
            tmp = line.strip().split(":")
            userinfo[tmp[0]] = tmp[1]
    return userinfo

def add_user(user,passwd):
    userfile = "userlist.txt"
    userinfo = "%s:%s\n"%(user,passwd)
    with open(userfile,"a") as f:
        f.write(userinfo)

def check_user(user):
    if len(user) == 0:
        return False
    else:
        return True 

def login_check(user,passwd):
    if user in get_user() and passwd == get_user()[user]:
        return True
    else:
        return False

def add_check(user):
    if user in get_user():
        return False
    else:
        return True

def login(user,passwd):
    if login_check(user,passwd):
        print "登陆成功!"
        return True
    else:
        print "用户名或密码错误!"
        return False

def regis(user,passwd):
    if add_check(user):
        add_user(user,passwd)
        print "用户注册成功"
        return True
    else:
        print "用户已存在"
        return False

def main():
    stat = raw_input("用户登陆还是注册？（登陆输入１，注册输入２）　>")
    if stat != "1" and stat != "2":
        print "输入错误"
        return True
    while True:
        if stat == "1":
            user = raw_input("请输入用户名　>")
            if  not check_user(user):
                print "用户名不能为空"
                continue
            passwd = raw_input("请输入密码　>")
            if login(user,passwd):
                break
        elif stat == "2":
            user = raw_input("请输入用户名　>")
            if not check_user(user):
                print "用户名不能为空"
                continue
            passwd = raw_input("请输入密码　>")
            r_passwd = raw_input("请再次输入密码　>")
            if passwd == r_passwd:
                if regis(user,passwd):
                    break
            else:
                print "２次输入密码不同，请重新注册"
        else:
            pass

main()