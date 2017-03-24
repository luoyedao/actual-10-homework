#!/usr/bin/env python
#coding=utf-8

from flask import Flask,render_template,request,redirect
from usermod import userlist,adduser,userlogin,deluser

users="user.txt"
app=Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def index():
  return render_template('index.html')

@app.route('/login')
def login():
  uinfo=userlist(users)
  user = request.args.get('username')
  passwd = request.args.get('password')
  error=userlogin(uinfo,user,passwd)
  if error == 0:
    return redirect('/userinfo')
  else:
    return render_template('index.html',loginfo=error)

@app.route('/userinfo')
def info():
  uinfo=userlist(users)
  name=request.args.get('username')
  if name in uinfo:
    return render_template('userlist.html',users={name:uinfo[name]})
  return render_template('userlist.html',users=uinfo)

@app.route('/zhuce')
def zhuce(): 
  uinfo=userlist(users)
  name=request.args.get('user')
  pwd1=request.args.get('pwd1')
  pwd2=request.args.get('pwd2')
  out=adduser(uinfo,users,name,pwd1,pwd2)
  return render_template('zhuce.html',loginfo=out)

@app.route('/delete')
def delete():
  uinfo=userlist(users)
  name=request.args.get('delname')
  deluser(uinfo,users,name)
  return redirect('/userinfo')

if __name__ == '__main__':
  app.run(host="0.0.0.0",port=8090,debug=True)
