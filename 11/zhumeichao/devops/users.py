#!/usr/bin/env python
#coding=utf-8

import time
import traceback
import json
import hashlib
from . import app
from flask import request,render_template,redirect,session
from udbapi import *
salt="xiaozhu"

@app.route('/')
@app.route('/index')
def index():
  if not session.get('username',None):
    return redirect('/login')
  if not session.get('username'):
    return redirect('/login')
  fields=['id','name','name_cn','email','mobile','role','status','create_time','last_time']
  result=seluser(fields,name=session['username'])
  uinfo=dict((k,result[i]) for i,k in enumerate(fields))
  return render_template('index.html',user=uinfo)
#  return redirect('/index')

@app.route('/login', methods=['GET','POST'])
def login():
  if request.method == 'POST':
    uinfo=dict((k,v[0]) for k,v in dict(request.form).items())
    uinfo["pass"] = hashlib.md5(uinfo["pass"]+salt).hexdigest()
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
    reginfo["password"] = hashlib.md5(reginfo["password"]+salt).hexdigest()
    try:
      res=adduser(fields,reginfo)
      if res:
	msg = "Register Success!!!"
        return json.dumps({"code" : 0,"errmsg" : msg})
    except:
      errmsg = 'register failed'
      print traceback.print_exc()
      return json.dumps({"code" : 1,"errmsg" : errmsg})
  else:
    if not session.get('username'):
      return redirect('/login')
    if session['role'] != "admin":
      return redirect('/userinfo')
    return render_template('juser/register.html')

@app.route('/update',methods=['GET','POST'])
def update():
  if request.method == 'POST':
    userdata=dict(request.form)
    try:
      moduser(userdata)
      msg = "Update Success!!!"
      return json.dumps({"code" : 0,"result" : msg})
    except:
      errmsg = 'Update False...'
      print traceback.print_exc()
      return json.dumps({"code" : 1,"errmsg" : errmsg})
  else:
    if not session.get('username'):
      return redirect('/login')
    fields=['id','name','name_cn','email','mobile','role','status']
    try:
      data=seluser(fields,uid=request.args.get('uid'))
      uinfo=dict((k,data[i]) for i,k in enumerate(fields))
      return json.dumps(uinfo)
    except:
      errmsg = 'update failed'
      print traceback.print_exc()
      return json.dumps({"code" : 1,"errmsg" : errmsg})

@app.route('/deluser')
def deluser():
  if not session.get('username'):
    return redirect('/login')
  if session['role'] != "admin":
    errmsg = 'permission denied'
    return json.dumps({"code" : 1,"errmsg" : errmsg})
  try:
    uid=request.args.get('uid')
    res=killuser(uid)
    if res:
      return json.dumps({"code" : 1})
    return json.dumps({"code" : 0})
  except:
    print traceback.print_exc()
    return json.dumps({"code" : 1})
 
@app.route('/modpasswd', methods=['GET','POST'])
def modpasswd():
  if request.method == 'POST':
    data=dict((k,v[0])  for k,v in dict(request.form).items())    
    if not data['nepasswd'] or data['nepasswd'] != data['repasswd']:
      errmsg='You should input the same password...'
      return json.dumps({"code" : 1,"errmsg" : errmsg})
    data["nepasswd"] = hashlib.md5(data["nepasswd"]+salt).hexdigest()
    try:
      chgpass(data['nepasswd'],data['id'])
      msg='Password Change Success !!!'
      return json.dumps({"code" : 0,"result" : msg})
    except:
      errmsg='Password change faild...'
      print traceback.print_exc()
      return json.dumps({"code" : 1,"errmsg" : errmsg})
  else:
    if not session.get('username'):
      return redirect('/login')
    fields=['id','name','role']
    data=seluser(fields,uid=request.args.get('id'))
    uinfo=dict((k,data[i]) for i,k in enumerate(fields))
    return render_template('juser/passwd.html',user=uinfo)

