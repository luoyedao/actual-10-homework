#!/usr/bin/env python
#coding:utf-8


#获取用户
def get_user():
    res={}
    with open('user.txt') as f:
        for line in f:
            tmp=line.strip().split(":")
            res[tmp[0]]=tmp[1]
    return res

#注册
def reg():
    while True:
        name=raw_input('请输入用户名:').strip()
        if len(name)==0 or name in get_user():
            print "用户名输入有误"
            continue
        password=raw_input('请输入密码:').strip()
        repass=raw_input('请再次输入密码:').strip()
        if len(password)==0 or password !=repass:
            print "密码输入错误,请检查你的密码是否一致"
            continue
        else:
            print "恭喜你，注册成功！"
            break
#将用户名和密码保存到文件
    with open('user.txt','a+') as f:
        f.write("%s:%s\n" % (name,password))


#用户登录
def login (res):
    while True:
        name=raw_input('请输入用户姓名:').strip()
        password=raw_input('请输入您的密码:').strip()
        if name not in res or len(name)==0:
            print "用户名不存在请重新输入"
            continue
        elif password !=res[name]:
                print "密码输入有误"
                continue
        else:
                print "恭喜你，登陆成功"
                break


while True:
        result=raw_input("注册还是登录:")
        res=get_user()
        if result=="登录":
            startlogin=login(res)
            break
        elif result=="注册":
            start_reg=reg()
            break
