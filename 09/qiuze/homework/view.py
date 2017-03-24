#!/usr/bin/env python
# coding:utf-8
# @Date     : 2016-09-07 21:53
# @Author   : William/linqz

from flask import request,render_template,redirect,session
import time,json
from run import app
from db import *

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user = dict((k,v[0]) for k,v in dict(request.form).items())
        oneUser = check_user(user)
        if not user.get('name',None) or not user.get('password',None):
            errmsg = 'username or password cannot be null!'
            return json.dumps({'code':'1','errmsg':errmsg})
        elif not oneUser:
            errmsg = 'username or password not right!'
            return json.dumps({'code':'1','errmsg':errmsg})
        elif oneUser: # 账号和密码都正确
            session['id'] = oneUser['id'] # 添加一个session
            session['role'] = oneUser['role'] # 添加一个session角色   //登录之后增加一个session 和 role
            return json.dumps({'code':'0','result':'login sucess'})
    elif request.method == 'GET':
        return render_template('login_new.html')

@app.route('/logout')
def logout():
    session.pop('name')
    session.pop('role')
    return redirect('/login')

@app.route('/onelist',methods=['GET','POST'])
def onelist():
    if not session['id']:
        return redirect('/login')
    user = selectOne(session['id']) # 以session['id']作为字段查询
    return render_template('onelist.html',user=user)

@app.route('/getbyid')
def getbyid():
    # $.getJSON 后台get请求到这里，获取到用户的userdict
    if not session.get('id',None):
        return redirect('/login')
    id = request.args.get('id')
    if not id:
        return json.dumps({'code':'1','errmsg':'must have a condition'})
    #condition = 'id=%s' % id
    user = selectOne(id)
    return json.dumps({'code':'0','result':user})

@app.route('/update',methods=['GET','POST'])
def update():
    if not session['id']:
        return redirect('/login')
    if request.method == 'GET':
        uid = request.args.get('id')
        return render_template('update.html',uid=uid,type=session['role'])
    elif request.method == 'POST':
        user = dict((k,v[0]) for k,v in dict(request.form).items())
        updateOne(user)
        return json.dumps({'code':'0','result':'update sucess'})

@app.route('/userlist',methods=['GET','POST'])
def userlist():
    if not session['id']:
        return redirect('/login')
    if session['role'] != 'admin':
        return redirect('/onelist')
    if request.method == 'GET':
        users = selectAll()
        return render_template('userlist.html',users=users)

@app.route('/delete',methods=['GET','POST'])
def delete():
    if not session.get('id',None):
        return redirect('/login')
    if session['role'] != 'admin':
        return redirect('/onelist')
    if request.method == 'GET':
        id = request.args.get('id')
        print id
        print session['id']
        if session['id'] == id:
            return "can not delete yourself!!!"
        else:
            deleteOne(id)
            return redirect('/userlist')

# 添加用户，第一次请求获取添加页面为一个GET请求，填写表单后点击提交post请求。
@app.route('/register',methods=['GET','POST'])
def register():
    if not session.get('id',None):
        return redirect('/login')
    if session['role'] != 'admin':
        return json.dumps({'code':'1','errmsg':'not admin,not permisson!'})
        #return redirect('/onelist')
    if request.method == 'POST':
        user = dict((k,v[0]) for k ,v in dict(request.form).items())
        fields = ['name','name_cn','password','email','mobile','role']
        for i in fields:
            if not user[i]:
                errmsg = "%s can not be null!!!" % (i)
                return json.dumps({'code':'1','errmsg':errmsg})
        if user['password'] != user['repwd']:
            errmsg = "twice password not correct!!"
            return json.dumps({'code':'1','errmsg':errmsg})
        insertOne(user) #执行数据插入sql
        result="register sucessful!!"
        return json.dumps({'code':'0','result':result})
    if request.method == 'GET':
        return render_template('register.html')