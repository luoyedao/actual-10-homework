#!/usr/bin/env python
#coding=utf-8

from flask import Flask,request,render_template,redirect,session
import time
import traceback
import json
from dbapi import *

app=Flask(__name__)

@app.route('/')
def usermgr():
  return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
  if request.method == 'POST':
    uinfo=dict((k,v[0]) for k,v in dict(request.form).items())
    if not uinfo.get('user',None) or not uinfo.get('pass',None):
      errmsg = 'please input username and password...'
      return render_template('login.html',result=errmsg)
    fields=['id','name','password','role']
    res=seluser(fields,name=uinfo['user'])
    if not res:
      errmsg = '%s not exist..please create it' %(uinfo['user'])
      return render_template('login.html',result=errmsg)
    udata=dict((k,res[i]) for i,k in enumerate(fields))
    if uinfo['pass'] != udata['password']:
      errmsg = 'password not true...'
      return render_template('login.html',result=errmsg)
    else: 
      return redirect('/userinfo?id=%s&role="%s"' %(udata['id'],udata['role']))
  else:
    return render_template('login.html')

@app.route('/userinfo')
def userinfo():
  data = {}
  data['id'] = request.args.get('id',None)
  data['name'] = request.args.get('name',None)
  data['role'] = request.args.get('role',None)
  fields=['id','name','name_cn','email','mobile','role','status','create_time','last_time']
  if not data['id'] and not data['name']:
    return redirect('/login')
  if data['role'] == '"admin"':
    return redirect('/userlist?role="admin"')
  if data['id'] and not data['name']:
    result=seluser(fields,uid=data['id'])
  if data['name'] and not data['id']:
    result=seluser(fields,name=data['name'])
  uinfo=dict((k,result[i]) for i,k in enumerate(fields))
  return render_template('userinfo.html',user=uinfo)

@app.route('/oneuser')
def oneuser():
  uname=request.args.get('user')
  if not uname:
    return redirect('/userlist?role="admin"') 
  fields=['id','name','name_cn','email','mobile','role','status','create_time','last_time']
  result=seluser(fields,name=uname)
  uinfo=dict((k,result[i]) for i,k in enumerate(fields))
  return render_template('userlist.html',user=uinfo)

@app.route('/userlist')
def userlist():
  data = {}
  data['id'] = request.args.get('id',None)
  data['name'] = request.args.get('name',None)
  data['role'] = request.args.get('role',None)
  if not data['role'] and not data['name'] and not data['id']:
    return redirect('/login')
  if data['role'] == '"admin"':
    fields=['id','name','name_cn','email','mobile','role','status','create_time','last_time']
    result=seluser(fields)
    return render_template('userlist.html',users=result)
  if data['id'] and not data['name']:
    return redirect('/userinfo?id=%s' % data['id'])
  if data['name'] and not data['id']:
    return redirect('/userinfo?name="%s"' % data['name'])

@app.route('/register',methods=['GET','POST'])
def register():
  if request.method == 'POST':
    reginfo={}
    reginfo["name"]=request.form.get('name',None)
    reginfo["name_cn"]=request.form.get('name_cn',None)
    reginfo["password"]=request.form.get('passwd',None)
    reginfo["passre"]=request.form.get('passre',None)
    reginfo["email"]=request.form.get('email',None)
    reginfo["mobile"]=request.form.get('mobile',None)
    reginfo["role"]=request.form.get('role',None)
    reginfo["status"]=request.form.get('status',None)
    reginfo["create_time"]=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    reginfo["last_time"]=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    fields=['name','name_cn','password','email','mobile','role','status','create_time','last_time']
    if not reginfo["name"] or not reginfo["password"] or not reginfo["email"]:
      errmsg = 'please input username,password,email at least!'
      return render_template("register.html",result=errmsg)     
    if reginfo["password"] != reginfo["passre"]:
      errmsg = 'password not match,please retry input'
      return render_template("register.html",result=errmsg)     
    try:
      res=adduser(fields,reginfo)
      if res:
        uinfo=dict((k,res[i]) for i,k in enumerate(fields))
        return redirect('/userinfo?name=%s&role="%s"' %(uinfo['name'],uinfo['role']))
    except:
      errmsg = 'register failed'
      print traceback.print_exc()
      return render_template("register.html",result=errmsg)     
  else:
    return render_template('register.html')

@app.route('/update',methods=['GET','POST'])
def update():
  if request.method == 'POST':
    userdata=dict(request.form)
    try:
      moduser(userdata)
      return redirect('/userinfo?id=%s&role="%s"'%(userdata['id'][0],userdata['role'][0]))
    except:
      errmsg = 'update failed'
      print traceback.print_exc()
      return render_template('update.html',result=errmsg)
  else:
    userid=request.args.get('id')
    fields=['id','name','name_cn','email','mobile','role','status']
    data=seluser(fields,uid=userid)
    uinfo=dict((k,data[i]) for i,k in enumerate(fields))
    return render_template('update.html',user=uinfo)

@app.route('/deluser')
def deluser():
  userid=request.args.get('id')
  try:
    killuser(userid)
    return redirect('/userlist?role="admin"')
  except:
    print traceback.print_exc()
    return redirect('/userlist?role="admin"')
 
@app.route('/modpasswd',methods=['GET','POST'])
def modpasswd():
  if request.method == 'POST':
    data=dict((k,v[0])  for k,v in dict(request.form).items())    
    if not data['passwd'] or not data['passmd'] or not data['passrd']:
      errmsg='you should input full password...'
      return render_template('modpasswd.html',result=errmsg)
    if data['passmd'] != data['passrd']:
      errmsg='you should input tow same password...'
      return render_template('modpasswd.html',result=errmsg)
    try:
      chgpass(data['passmd'],data['id'])
      return redirect('/userinfo?id=%s' % data['id'])
    except:
      errmsg='password change faild...'
      print traceback.print_exc()
      return render_template('modpasswd.html',user=data,result=errmsg)
  else:
    user={}
    user['id']=request.args.get('id')
    return render_template('modpasswd.html',user=user)

if __name__ == '__main__':
  app.run(host='0.0.0.0',port=2000,debug=True)

