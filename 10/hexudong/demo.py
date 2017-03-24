#coding:utf-8
from run import app
from flask import Flask,render_template,request,redirect,session
import json 
from functools import wraps
from db import *


def login_required(func):
    @wraps(func)
    def deco(*args,**kwargs):
        if not session.get('username'):
            return redirect("/login")
        else:
            return func(*args,**kwargs)
    return deco

@app.route('/login',methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        login_info = dict((k,v[0]) for k,v in dict(request.form).items())
        if not checkuser({"name":login_info["name"]},"name"):
            return json.dumps({"code":0,"errmsg":"user is not exit"})
        if login_info["password"] != checkuser({'name':login_info["name"]})[0]:
            return json.dumps({"code":0,"errmsg":"password error"})
        else:
            u_role = checkuser({"name":login_info["name"]},"role")
            session["username"] = login_info["name"]
            session["role"] = u_role
            return json.dumps({"code":0,'result':'login success'})

@app.route("/")
@app.route("/index")
@login_required
def index():
    return render_template('index.html',info=session)

@app.route('/userlist')
@login_required
def user_list():
    fields = ["id","name","name_cn","mobile","email","role","status"]
    data = userlist(fields)
    me_role = session["role"]
    print me_role
    return render_template("userlist.html",users = data,me_role=me_role,info=session)

@app.route("/add",methods=["GET","POST"])
@login_required
def add_user():
    if request.method == "POST":
        data=dict((k,v[0]) for k,v in dict(request.form).items())
        if data["name"] in checkuser({"name":data["name"]},"name"):
            return json.dumps({"code":1,"errmsg":"username is exist"})
        adduser(data)
        return json.demps({"code":0,"result":"add user success"})
    else:
        return render_template("add.html",info=session)

@app.route("/userinfo")
@login_required
def userinfo():
    where ={}
    where['id'] = request.args.get('data-id',None)
    data=Getone(where['id'])
    print data
    return render_template('userlist.html',user = data)

@app.route("/delete")
@login_required
def del_user():
    uid = request.args.get("id")
    delete(uid)
    return json.dumps({"code":0,"result":"delete user success"})

@app.route('/idc')
@login_required
def idc():
    fields = ["id","name","number","person","phone","xxx"]
    data = Userlist_idc(fields)
    print data
    me_role = session["role"]
    print me_role
    return render_template("idc.html",users = data,me_role=me_role,info=session)

@app.route('/cabinet')
@login_required
def cabinet():
    return render_template("cabinet.html",info=session)

@app.route('/server')
@login_required
def server():
    return render_template("server.html",info=session)

@app.route("/logout/")
def logout():
    session.pop('role',None)
    session.pop('username', None)
    return redirect("/login")
