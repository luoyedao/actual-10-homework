#!/usr/bin/env python
#coding:utf-8
from flask import Flask,redirect,request,render_template,session
from db import *
import json

app=Flask(__name__)
app.secret_key='1qw2#ER$'


@app.route("/")
@app.route("/login",methods=['GET','POST'])
def login():
	if request.method =="GET":
		return render_template("login.html")
	if request.method =='POST':
		data = dict((k,v[0]) for k,v in dict(request.form).items())
		if not data.get("name",None) or not data.get("password",None):
            		errmsg = "username and password can not be empty"
			return json.dumps({'code':'1','errmsg':errmsg})
        	if data["name"] not in  [ n.values()[0] for n in get_userlist(["name"]) ]:
			namelist=[ n.values()[0] for n in get_userlist(["name"]) ]
            		errmsg = "username not exist"
			return json.dumps({'code':'1','errmsg':errmsg})
        	if data["password"] != checkuser(data["name"]):
            		errmsg = "password is error"
			return json.dumps({'code':'1','errmsg':errmsg})
		else:
			session['name']=data['name']
			return json.dumps({'code':'0','result':"login sucess"})

@app.route("/userlist")
def index():
	if not session.get('name'):
		return redirect('/login')
	data=["id","name","name_cn","email","mobile","role","status"]
	username=session.get("name")
	if username == "admin":
		userlist=get_userlist(data)
		return render_template("userlist.html",users=userlist,username=username)
	else:
		users=getone(username)
		return render_template("userinfo.html",users=users,username=username)

@app.route("/adduser",methods=['GET','POST'])
def adduser():
        if request.method =="GET":
                return render_template("register.html")
	if request.method =="POST":
		userlist=dict((k,v[0]) for k,v in dict(request.form).items())
		if userlist["name"] in [ n.values() for n in get_userlist(["name"]) ]:
			content = "username is exist"
			return json.dumps({'code':'1','errmsg':errmsg})
		if not userlist["name"] or not userlist["password"]:
			content = "username and password is not empty"
			return json.dumps({'code':'1','errmsg':errmsg})
		if userlist["password"] != userlist["re_password"]:
			content="password is error"
			return json.dumps({'code':'1','errmsg':errmsg})
		fields = ["name","name_cn","password","mobile","email","role","status"]
        	values = [ '%s'%userlist[x] for x in fields]
        	userdict = dict([(k,values[i]) for i,k in enumerate(fields)])
		add_user(userdict)	
		return json.dumps({'code':'0','result':"register sucess"})

@app.route("/deluser")
def deluser():
        if not session.get('name'):
                return redirect('/login')
	uid=request.args.get("uid")
	del_user(uid)
	return redirect("/userlist")

@app.route("/update",methods=['GET','POST'])
def updateuser():
        if not session.get('name'):
                return redirect('/login')
	if request.method =="GET":
		userinfo=getuser(request.args.get("uid"))
		return render_template("update.html",user=userinfo)
	if request.method =="POST":
		userinfo=dict((k,v[0]) for k,v in dict(request.form).items())
        	update_user(userinfo)
        	return redirect("/userlist")

@app.route("/modpasswd",methods=["GET","POST"])
def changepass():
	if request.method=="GET":
		return render_template("changepass.html")
	if request.method=="POST":
		passwd_info=dict((k,v[0]) for k,v in dict(request.form).items())
		if not passwd_info.get("password","None") or not passwd_info.get("oldpassword","None"):
			errmsg = "password can not be empty"
			return json.dumps({'code':'1','errmsg':errmsg})
		if passwd_info["oldpassword"] != checkuser(session.get("name")):
			oldpassword=checkuser(session.get("name"))
			errmsg= "your input oldpassword is error"
			return json.dumps({'code':'1','errmsg':errmsg})
		else:
			name=session.get("name")
			password=passwd_info["password"]
			modpasswd(password,name)
			return json.dumps({'code':'0','result':"change sucess"})

@app.route('/loginout')
def loginout():
	session.pop('name')
	return redirect('/login')

if __name__=="__main__":
        app.run(host="0.0.0.0",port=9092,debug=True)
