#!/usr/bin/env python
#coding:utf-8
from flask import Flask,redirect,request,render_template
from db import get_userlist,getuser,add_user,del_user,update_user,checkuser

app=Flask(__name__)


@app.route("/")
def users():
	return redirect("/login")


@app.route("/userlist")
def index():
	user_items=["id","name","name_cn","email","mobile","role","status"]
	userlist=get_userlist(user_items)
	return render_template("userlist.html",users=userlist)

@app.route("/login",methods=['GET','POST'])
def login():
	if request.method =="GET":
		return render_template("login.html")
	if request.method =='POST':
		login_info = dict((k,v[0]) for k,v in dict(request.form).items())
		print login_info
		if not login_info.get("name",None) or not login_info.get("password",None):
            		errmsg = "username and password can not be empty"
            		return render_template("login.html",result=errmsg)
#把数据库中所有的name拿出来存为一个list
        	if login_info["name"] not in  [ n.values()[0] for n in get_userlist(["name"]) ]:
			namelist=[ n.values()[0] for n in get_userlist(["name"]) ]
			print namelist
			print login_info["name"]
            		errmsg = "username not exist"
            		return render_template("login.html",result=errmsg)
        	if login_info["password"] != checkuser(login_info["name"]):
            		errmsg = "password is error"
            		return render_template("login.html",result=errmsg)
		else:
	    		return redirect("/userlist")
	
@app.route("/adduser",methods=['GET','POST'])
def adduser():
        if request.method =="GET":
                return render_template("register.html")

#前端post请求，逻辑端通过request.form获取整个表单的值
	if request.method =="POST":
		userlist=dict((k,v[0]) for k,v in dict(request.form).items())
		if userlist["name"] in [ n.values() for n in get_userlist(["name"]) ]:
			content = "username is exist"
			return render_template("register.html",content=content)
		if not userlist["name"] or not userlist["password"]:
			content = "username and password is not empty"
			return render_template("register.html",content=content)
		if userlist["password"] != userlist["re_password"]:
			content="password is error"
			return render_template("register.html",content=content)
		fields = ["name","name_cn","password","mobile","email","role","status"]
        	values = [ '%s'%userlist[x] for x in fields]
		print values
#[u'weixiaobao', u'weixiaobao', u'123', u'123123', u'123113', u'ops', u'0']
        	userdict = dict([(k,values[i]) for i,k in enumerate(fields)])
		print userdict
#{'status': u'0', 'name': u'weixiaobao', 'mobile': u'123123', 'name_cn': u'weixiaobao', 'role': u'ops', 'password': u'123', 'email': u'123113'}
		add_user(userdict)	
		return redirect("/login")


@app.route("/deluser")
def deluser():
#前端get请求，逻辑端通过request.args.get获取参数
	uid=request.args.get("uid")
	print uid
	del_user(uid)
	return redirect("/userlist")

@app.route("/update",methods=['GET','POST'])
def updateuser():
#通过id查询到要更新的数据，并渲染到更新页面
	if request.method =="GET":
		uid=request.args.get("uid")
		print uid
		userinfo=getuser(uid)
		return render_template("update.html",user=userinfo)
#获取到更新页面表单的值，然后提交更新
	if request.method =="POST":
		userinfo={}
        	userinfo["name"] = request.form['name']
		userinfo["name_cn"] = request.form['name_cn']
        	userinfo["email"] = request.form['email']
       	 	userinfo["mobile"] = request.form['mobile']
        	userinfo["role"] = request.form['role']
        	userinfo["status"] = request.form['status']
        	update_user(userinfo)
        	return redirect("/userlist")




if __name__=="__main__":
        app.run(host="0.0.0.0",port=8888,debug=True)
