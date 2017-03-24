#!/usr/bin/env python
#coding=utf-8

import time
import traceback
import json
from flask import request,render_template,redirect,session
from dbapi import *
from run_server import app

@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
  if request.method == 'POST':
    uinfo=dict((k,v[0]) for k,v in dict(request.form).items())
    if not uinfo.get('user',None) or not uinfo.get('pass',None):
      errmsg = 'please input username and password...'
      return json.dumps({"code" : 1,"errmsg" : errmsg})
    fields=['id','name','password','role','status']
    res=seluser(fields,name=uinfo['user'])
    if not res:
      errmsg = '%s not exist..please create it' %(uinfo['user'])
      return json.dumps({"code" : 1,"errmsg" : errmsg})
    udata=dict((k,res[i]) for i,k in enumerate(fields))
    if udata['status'] == 1:
      errmsg = '%s is lock..please unlock it' %(uinfo['user'])
      return json.dumps({"code" : 1,"errmsg" : errmsg})
    if uinfo['pass'] != udata['password']:
      errmsg = 'password not true...'
      return json.dumps({"code" : 1,"errmsg" : errmsg})
    else:
      session['username']=udata['name']
      session['password']=udata['password']
      session['role']=udata['role']
      errmsg = 'Login Success!!!'
      return json.dumps({"code" : 0,"result" : errmsg})
  else:
    return render_template('login.html')

@app.route('/logout')
def logout():
  session.clear()
  return redirect('/login')

@app.route('/userinfo')
def userinfo():
  if not session.get('username'):
    return redirect('/login')
  if session['role'] == "admin":
    return redirect('/userlist')
  fields=['id','name','name_cn','email','mobile','role','status','create_time','last_time']
  result=seluser(fields,name=session['username'])
  uinfo=dict((k,result[i]) for i,k in enumerate(fields))
  return render_template('juser/userinfo.html',user=uinfo)

@app.route('/oneuser')
def oneuser():
  uname=request.args.get('user')
  if not uname:
    return redirect('/userlist') 
  fields=['id','name','name_cn','email','mobile','role','status','create_time','last_time']
  result=seluser(fields,name=uname)
  uinfo=dict((k,result[i]) for i,k in enumerate(fields))
  return render_template('juser/userlist.html',user=uinfo)

@app.route('/userlist')
def userlist():
  if not session.get('username'):
    return redirect('/login')
  if session['role'] == "admin":
    fields=['id','name','name_cn','email','mobile','role','status','create_time','last_time']
    result=seluser(fields)
    return render_template('juser/userlist.html',users=result)
  else:
    return redirect('/userinfo')

@app.route('/register',methods=['GET','POST'])
def register():
  if request.method == 'POST':
    reginfo=dict((k,v[0]) for k,v in dict(request.form).items())
    reginfo["create_time"]=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    reginfo["last_time"]=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    fields=['name','name_cn','password','email','mobile','role','status','create_time','last_time']
    if not reginfo['name'] or not reginfo['password'] or not reginfo['email']:
      errmsg = 'please input username,password,email at least!'
      return json.dumps({"code" : 1,"errmsg" : errmsg})
    if reginfo["password"] != reginfo["passre"]:
      errmsg = 'password not match,please retry input'
      return json.dumps({"code" : 1,"errmsg" : errmsg})
    try:
      res=adduser(fields,reginfo)
      if res:
        uinfo=dict((k,res[i]) for i,k in enumerate(fields))
	msg = "Register Success!!!"
        return json.dumps({"code" : 0,"errmsg" : errmsg})
    except:
      errmsg = 'register failed'
      print traceback.print_exc()
      return json.dumps({"code" : 1,"errmsg" : errmsg})
  else:
    if not session.get('username'):
      return redirect('/login')
    if session['role'] != "admin":
      return redirect('/userinfo')
    return render_template('register.html')

@app.route('/update',methods=['GET','POST'])
def update():
  if request.method == 'POST':
    userdata=dict(request.form)
    try:
      moduser(userdata)
      msg = "Update Success!!!"
      return json.dumps({"code" : 0,"errmsg" : errmsg})
    except:
      errmsg = 'update failed'
      print traceback.print_exc()
      return json.dumps({"code" : 1,"errmsg" : errmsg})
  else:
    if not session.get('username'):
      return redirect('/login')
    fields=['id','name','name_cn','email','mobile','role','status']
    try:
      data=seluser(fields,uid=request.args.get('id'))
      uinfo=dict((k,data[i]) for i,k in enumerate(fields))
      if session['role'] == "admin":
        return render_template('juser/admin_edit.html',user=uinfo)
      return render_template('juser/user_edit.html',user=uinfo)
    except:
      errmsg = 'update failed'
      print traceback.print_exc()
      return render_template("juser/userinfo.html",result=errmsg)     

@app.route('/deluser')
def deluser():
  if not session.get('username'):
    return redirect('/login')
  try:
    killuser(request.args.get('id'))
    return redirect('/userlist')
  except:
    print traceback.print_exc()
    return redirect('/userlist')
 
@app.route('/modpasswd', methods=['GET','POST'])
def modpasswd():
  if request.method == 'POST':
    data=dict((k,v[0])  for k,v in dict(request.form).items())    
    if not data['passwd'] or not data['passmd'] or not data['passrd']:
      errmsg='you should input full password...'
      return json.dumps({"code" : 1,"errmsg" : errmsg})
    if data['passmd'] != data['passrd']:
      errmsg='you should input tow same password...'
      return json.dumps({"code" : 1,"errmsg" : errmsg})
    try:
      chgpass(data['passmd'],data['name'])
      msg='Password Change Success !!!'
      return json.dumps({"code" : 0,"result" : msg})
    except:
      errmsg='password change faild...'
      print traceback.print_exc()
      return json.dumps({"code" : 1,"errmsg" : errmsg})
  else:
    if not session.get('username'):
      return redirect('/login')
    fields=['id','name','role']
    data=seluser(fields,uid=request.args.get('id'))
    uinfo=dict((k,data[i]) for i,k in enumerate(fields))
    return render_template('pass_edit.html',user=uinfo)

