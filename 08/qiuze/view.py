#!/usr/bin/env python
# coding:utf-8
# @Date     : 2016-09-07 21:53
# @Author   : William/linqz

from flask import request,render_template,redirect,session
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
        if not user['name'] or not user['password']:
            errmsg = 'username or password cannot be null!'
            return render_template('login.html',result=errmsg)
        elif not oneUser:
            errmsg = 'username or password not right!'
            return render_template('login.html',result=errmsg)
        elif oneUser:
            session['id'] = oneUser['id'] # 添加一个session
            session['role'] = oneUser['role'] # 添加一个session角色
            if session['role'] == 'admin':
                return redirect('/userlist')
            elif session['role'] == 'common':
                return redirect('/onelist')
    elif request.method == 'GET':
        return render_template('login.html')

@app.route('/onelist',methods=['GET','POST'])
def onelist():
    if not session['id']:
        return redirect('/login')
    user = selectOne(session['id']) # 以session['id']作为字段查询
    return render_template('onelist.html',user=user)

@app.route('/update',methods=['GET','POST'])
def update():
    if not session['id']:
        return redirect('/login')
    if request.method == 'GET':
        id = request.args.get('id')
        user = selectOne(id)
        return render_template('update.html',user=user,type=session['role'])
    elif request.method == 'POST':
        user = dict((k,v[0]) for k,v in dict(request.form).items())
        updateOne(user)
        if session['role'] == 'admin':
            return redirect('/userlist')
        else:
            return redirect('/onelist')

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
    if not session['id']:
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

@app.route('/register',methods=['GET','POST'])
def register():
    if not session['id']:
        return redirect('/login')
    if session['role'] != 'admin':
        return redirect('/onelist')
    if request.method == 'POST':
        user = dict((k,v[0]) for k ,v in dict(request.form).items())
        fields = ['name','name_cn','password','email','mobile','role']
        for i in fields:
            if not user[i]:
                errmsg = "%s can not be null!!!" % (i)
                return render_template('register.html',result=errmsg)
        if user['password'] != user['repwd']:
            errmsg = "twice password not correct!!"
            return render_template('register.html',result=errmsg)
        insertOne(user)
        result="register sucessful!!"
        return render_template('login.html',result=result)
    if request.method == 'GET':
        return render_template('register.html')