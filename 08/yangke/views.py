#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-08-13 18:59:13
# @Author  : yang ke (jack_keyang@163.com)

from run import app
from flask import render_template,request,redirect,session
from db import adduser,userlist,delete,getone,modfiy,checkuser,modpasswd
from functools import wraps
import json

def login_required(func):
    @wraps(func)
    def deco(*args,**kwargs):
        if not session.get('username'):
            return redirect("/login")
        else:
            return func(*args,**kwargs)
    return deco

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        login_info = dict((k,v[0]) for k,v in dict(request.form).items())
        if not login_info["name"] or not login_info["password"]:
            errmsg = "username or password or role not null"
            data = json.dumps({"tag":0,"msg":errmsg})
            return data
        if login_info["name"] not in [ n.values()[0] for n in userlist(["name"]) ]:
            errmsg = "user is not exist"
            data = json.dumps({"tag":0,"msg":errmsg})
            return data
        if login_info["password"] != checkuser({'name':login_info["name"]}):
            errmsg = "password error"
            data = json.dumps({"tag":0,"msg":errmsg})
            return data
        else:
            u_role = [ u['role'] for u in userlist(["name","role"]) if u['name'] == login_info["name"] ][0]
            session["username"] = login_info["name"]
            session["role"] = u_role
            data = json.dumps({"tag":1})
            return data

@app.route("/")
@login_required
def index():
    fields = ["id","name","name_cn","mobile","email","role","status"]
    username = session.get("username")
    u_role = session.get("role")
    if u_role == "admin":
        data = userlist(fields)
        return render_template("index.html",users = data, username=username)
    else:
        uid = [ u['id'] for u in userlist(['id','name']) if u['name'] == username ][0]
        data = getone(uid)
        return render_template("self.html",users = data, username=username)

@app.route("/adduser",methods=["GET","POST"])
@login_required
def add_user():
    if request.method == "GET":
        return render_template("adduser.html")
    if request.method == "POST":
        data = dict((k,v[0]) for k,v in dict(request.form).items())
        print data
        print [ n.values() for n in userlist(["name"]) ]
        if data["name"] in [ n.values()[0] for n in userlist(["name"]) ]:
            errmsg = "username is exist"
            rdata = json.dumps({"tag":0,"msg":errmsg})
            return rdata
        if not data["name"] or not data["password"] or not data["role"]:
            errmsg = "username or password or role not null"
            rdata = json.dumps({"tag":0,"msg":errmsg})
            return rdata
        if data["password"] != data["re_password"]:
            errmsg = "The two passwords you typed do not match"
            rdata = json.dumps({"tag":0,"msg":errmsg})
            return rdata
       
        fields = ["name","name_cn","password","mobile","email","role","status"]
        values = [ '%s'%data[x] for x in fields]
        userdic = dict([(k,values[i]) for i,k in enumerate(fields)])
        adduser(userdic)
        rdata = json.dumps({"tag":1})
        return rdata

@app.route("/delete")
@login_required
def del_user():
    uid = request.args.get("uid")
    delete(uid)
    return "ok"

@app.route("/update",methods=["GET","POST"])
@login_required
def update():
    if request.method == "GET":
        uid = request.args.get("id")
        userinfo = getone(uid)
        return render_template("modfiy.html",user=userinfo)
    if request.method == "POST":
        userinfo = dict((k,v[0]) for k,v in dict(request.form).items())
        print userinfo
        modfiy(userinfo)
        return "ok"

@app.route("/cgpassword",methods=["GET","POST"])
@login_required
def cgpasswd():
    if request.method == "GET":
        uid = request.args.get("id")
        return render_template("cgpasswd.html",uid=uid)
    if request.method == "POST":
        passwd_dic = dict((k,v[0]) for k ,v in dict(request.form).items())
        password = checkuser({"id":passwd_dic["id"]})
        print passwd_dic
        print password
        if passwd_dic["o_password"] != password:
            errmsg = "password is error"
            data = json.dumps({"tag":0,"msg":errmsg})
            return data
        if passwd_dic["n_password"] != passwd_dic["r_password"]:
            errmsg = "The two passwords you typed do not match"
            data = json.dumps({"tag":0,"msg":errmsg})
            return data
        pw_data={"id":passwd_dic['id'],"password":passwd_dic['n_password']}
        modpasswd(pw_data)
        data=json.dumps({"tag":1})
        return data

@app.route("/logout")
def logout():
    session.pop('role',None)
    session.pop('username', None)
    return redirect("/login")
