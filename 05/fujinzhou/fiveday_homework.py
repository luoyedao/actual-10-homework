#!/usr/bin/env python
#coding:utf-8
from flask import Flask,redirect,request,render_template
from file import userinfo,checkinfo,adduser,deluser
app=Flask(__name__)

@app.route("/")
def index():
	names=userinfo()
	print names
	return render_template("index.html",nameinfo=names)

@app.route("/adduser")
def add_user():
	name=request.args.get("username")
	password=request.args.get("password")
	if not checkinfo(name,password):
		return "用户和密码不存在"

	if name in userinfo():
		return "用户名已存在"
	adduser(name,password)
	return redirect("/")

@app.route("/deluser")
def del_user():
	name=request.args.get("username")
	if name in userinfo():
		deluser(name)
		return redirect("/")
	else:
		return "用户名不存在"



if __name__=="__main__":
	app.run(host="0.0.0.0",port=8888,debug=True)
