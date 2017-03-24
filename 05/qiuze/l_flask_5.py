#!/usr/bin/env python
# coding:utf-8

from flask import Flask,request,render_template,redirect
app = Flask(__name__)

# 填加用户名账号密码模块
def add_user(name,pwd):
    with open('user.txt','a+') as f:
        f.write('%s:%s\n' % (name,pwd))
    return
def check_user(name,pwd):
    with open('user.txt') as f:
        user_dict={}
        for line in f.readlines():
            user=line.split(":")[0]
            passwd=line.split(":")[1].strip("\n")
            user_dict[user]=passwd
    print user_dict
    if user_dict[name] == pwd:
        return 0
    else:
        return 1

# 用户管理界面
@app.route('/user_admin')
def user_admin():
    return render_template('portal.html')

# 注册用户
@app.route('/adduser')
def adduser():
    name = request.args.get('name')
    pwd = request.args.get('password')
    if name and pwd:
        return "注册成功！"
    else:
        return "注册失败！"

# 用户登录
@app.route('/login')
def login():
    name = request.args.get('name')
    pwd = request.args.get('password')
    print str(name)
    check_value=check_user(name,pwd)
    if check_value == 0:
        return "登录成功！"
    else:
        return "登录失败！"



# main
if __name__ =='__main__':
    app.run(host='0.0.0.0',port=8888,debug=True)
