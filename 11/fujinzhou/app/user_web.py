#!/usr/bin/python
#coding:utf-8

from flask import render_template,request,redirect,session
from . import app
from db import get_userlist,getuser,add_user,del_user,update_user,checkuser,getone,modpasswd
import json
import hashlib

salt="www.123"

# 欢迎页面

@app.route("/")
@app.route("/index")
def index():
        username=session.get("name")
        if not username:
                return redirect("/login")
        return render_template("index.html",username=username)

# 登录

@app.route("/login",methods=['GET','POST'])
def login():
        if request.method =="GET":
                return render_template("login.html")
        if request.method =='POST':
                login_info = dict((k,v[0]) for k,v in dict(request.form).items())
                login_info['password']=hashlib.md5(login_info['password']+salt).hexdigest()
                name=login_info["name"]
                userlists=getone(name)
                print userlists
                if not login_info.get("name",None) or not login_info.get("password",None):
                        errmsg = "username and password can not be empty"
                        return json.dumps({'code':'1','errmsg':errmsg})
#把数据库中所有的name拿出来存为一个list
                if login_info["name"] not in  [ n.values()[0] for n in get_userlist(["name"]) ]:
                        namelist=[ n.values()[0] for n in get_userlist(["name"]) ]
                        print namelist
                        print login_info["name"]
                        errmsg = "username not exist"
                        return json.dumps({'code':'1','errmsg':errmsg})
                if login_info["password"] != checkuser(login_info["name"]):
                        errmsg = "password is error"
                        return json.dumps({'code':'1','errmsg':errmsg})
                if int(userlists['status'])==1:
                        return json.dumps({'code':'1','errmsg':"账户被锁定"})

#判断session中的用户名与表单里面的用户名是否相同
                session['name']=login_info['name']
                return json.dumps({'code':'0','result':"login sucess"})

#用户列表

@app.route("/userlist")
def userlist():
#判断用户是否登录，如果没有登录就跳转到登录页
        if not session.get('name'):
                return redirect('/login')
        user_items=["id","name","name_cn","email","mobile","role","status"]
        username=session.get("name")
        if username == "admin":
                userlist=get_userlist(user_items)
                return render_template("userlist.html",users=userlist,username=username)


#个人信息

@app.route("/userinfo")
def userinfo():
        if not session.get('name'):
                return redirect('/login')
        user_items=["id","name","name_cn","email","mobile","role","status"]
        username=session.get("name")
        if username==session.get('name'):
                users=getone(username)
                return render_template("userinfo.html",users=users,username=username)


#添加用户
@app.route("/adduser",methods=['GET','POST'])
def adduser():
        if request.method =="GET":
                username=session.get("name")
                return render_template("register.html",username=username)

#前端post请求，逻辑端通过request.form获取整个表单的值
        if request.method =="POST":
                userlist=dict((k,v[0]) for k,v in dict(request.form).items())
                userlist['password']=hashlib.md5(userlist['password']+salt).hexdigest()
                userlist['re_password']=hashlib.md5(userlist['re_password']+salt).hexdigest()
                if userlist["name"] in [ n.values()[0] for n in get_userlist(["name"]) ]:
                        errmsg = "username is exist"
                        return json.dumps({'code':'1','errmsg':errmsg})
                if not userlist["name"] or not userlist["password"]:
                        errmsg = "username and password is not empty"
                        return json.dumps({'code':'1','errmsg':errmsg})
                if userlist["password"] != userlist["re_password"]:
                        errmsg="password is error"
                        return json.dumps({'code':'1','errmsg':errmsg})
                fields = ["name","name_cn","password","mobile","email","role","status"]
                values = [ '%s'%userlist[x] for x in fields]
                userdict = dict([(k,values[i]) for i,k in enumerate(fields)])
                add_user(userdict)
                return json.dumps({'code':'0','result':"register sucess"})

#删除用户

@app.route("/deluser",methods=['POST'])
def deluser():
        if not session.get('name'):
                return redirect('/login')
#前端get请求，逻辑端通过request.args.get获取参数
        uid=request.args.get("uid")
        print uid
        del_user(uid)
        return json.dumps({"code":0,"result":"delete user success"})


#更新用户

@app.route("/update",methods=['GET','POST'])
def updateuser():
        if not session.get('name'):
                return redirect('/login')
#通过id查询到要更新的数据，并渲染到更新页面
        if request.method =="GET":
                uid=request.args.get("uid")
                print uid
                userinfo=getuser(uid)
                print userinfo
                return json.dumps(userinfo)
#获取到更新页面表单的值，然后提交更新
        if request.method =="POST":
                userinfo=dict((k,v[0]) for k,v in dict(request.form).items())
		print userinfo
                update_user(userinfo)
                return json.dumps({"code":0})


#修改密码

@app.route("/modpasswd",methods=["POST"])
def changepass():
        if request.method=="POST":
                passwd_info=dict((k,v[0]) for k,v in dict(request.form).items())
                print passwd_info
                if len(passwd_info) == 3:
                        if passwd_info["password"] != passwd_info["re_password"]:
                                return json.dumps({"code":1,"errmsg":"The tow password is different"})
                if not passwd_info.get("password","None") or not passwd_info.get("re_password","None"):
                        errmsg = "password can not be empty"
                        return json.dumps({'code':'1','errmsg':errmsg})
                else:
                        uid=passwd_info["id"]
                        password=passwd_info["password"]
                        modpasswd(password,uid)
                        return json.dumps({'code':'0','result':"change sucess"})

#退出


@app.route('/loginout')
def loginout():
#session是一个大字典，把当前页面对应的session移除
        session.pop('name')
	return redirect('/login')
