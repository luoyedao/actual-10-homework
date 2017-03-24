#!/usr/bin/env python
#coding:utf-8
from flask import Flask,redirect,request,render_template,url_for
from users import get_userlist,getuser,add_user,del_user,update_user

app=Flask(__name__)

@app.route("/")
def userlist():
	user_items=["id","name","name_cn","email","mobile","role","status"]
	userlist=get_userlist(user_items)
	return render_template("userlist.html",users=userlist)


@app.route("/adduser",methods=['GET','POST'])
def adduser():
	if request.method =="GET":
		return render_template("adduser.html")
#前端post请求，逻辑端通过request.form获取整个表单的值
	if request.method =="POST":
		name=request.form['username']
		name_cn=request.form['username_cn']
		passwd=request.form['password']
		repasswd=request.form['re_password']
		email=request.form['email']
		mobile=request.form['mobile']
		role=request.form['role']
		status=request.form['status']
		userlist=get_userlist(["name"])
		print userlist
		if len(name)==0 or len(name_cn)==0 or len(passwd) == 0 or len(email) == 0 or len(mobile) == 0:
			content="这个值不能为空"
			return render_template("adduser.html",content=content)

		if name in map(lambda x:x["name"],userlist):
			content=u"用户已存在"
			return render_template("adduser.html",content=content)
		if passwd !=repasswd:
			content=u"您输入的两次密码不一致，请重新输入!"
			return render_template("adduser.html",content=content)
		userinfo=[name,name_cn,passwd,email,mobile,role,status]
		add_user(userinfo)	
		return redirect("/")

@app.route("/deluser")
def deluser():
#前端get请求，逻辑端通过request.args.get获取参数
	uid=request.args.get("uid")
	print uid
	del_user(uid)
	return redirect("/")

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
        	return redirect("/")
		
	

if __name__=="__main__":
	app.run(host="0.0.0.0",port=8888,debug=True)
