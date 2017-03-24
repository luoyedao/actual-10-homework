#!/bin/env python
#encoding:utf-8

import sys,time

# 登录
def start_login():
        res={}
        while True:
                with open('user.txt') as f:
                        li=f.readlines()
                        for line in li:
                                word=line.strip().split(':')
                                res[word[0]]=word[1]
                print res
                account=raw_input('请输入用户名:')
                passw=raw_input('请输入密码:')
                if account in res and passw==res[account]:
                        print '登录成功'
                        return 'success'
                else:
                        print '用户名密码错误'
                        continue
# 账户密码生成字典
def acc_dic():
        user_res={}
        with open('user.txt') as f:
                li=f.readlines()
                for line in li:
                        word=line.strip().split(':')
                        user_res[word[0]]=word[1]
                return user_res

# 账户持久化
def save_account(account,passw):
        with open('user.txt','a+') as f2:
                f2.write('%s:%s\n'%(account,passw))
# 注册
def start_reg():
        print '开始注册'
        while True:
                res=acc_dic()
                account=raw_input('请输入用户名:')
                if account in res:
                        print '用户名已存在'
                        continue
                passw=raw_input('请输入密码:')
                repassw=raw_input('请再次输入密码:')
                if len(passw)==0:
                        print '密码不能为空!'
                        continue
                elif passw!=repassw:
                        print '两次密码输入不一致'
                        continue
                else:
                        print '注册成功'
                        save_account(account,passw)
                        return 'success'
                        break

while True:
        time.sleep(1)
        result=raw_input('你好，是登录还是注册：')
        if result=="登录":
                val=start_login()
                if val=='success':
                        break
        elif result=="注册":
                val=start_reg()
                if val=='success':
                        break
        elif result=="out":
                break
        else:
                print '不能为空!,输入 out 推出!'
                continue
