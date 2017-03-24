#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-08-13 18:59:13
# @Author  : yang ke (jack_keyang@163.com)
# test

from run import app
from flask import render_template,request,redirect,session
from db import adduser,userlist,delete,getone,modfiy,checkuser,modpasswd
from functools import wraps
import json
import commands
import os
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
        if not checkuser({"name":login_info["name"]},"name"):
            errmsg = "user is not exist"
            data = json.dumps({"tag":0,"msg":errmsg})
            return data
        if login_info["password"] != checkuser({'name':login_info["name"]})[0]:
            errmsg = "password error"
            data = json.dumps({"tag":0,"msg":errmsg})
            return data
        else:
            u_role = checkuser({"name":login_info["name"]},"role")
            session["username"] = login_info["name"]
            session["role"] = u_role
            data = json.dumps({"tag":1})
            return data

@app.route("/")
@login_required
def index():
    username = session.get("username")
    return render_template("index.html", username=username)

@app.route("/userlist/")
@login_required
def user_list():
    fields = ["id","name","name_cn","mobile","email","role","status"]
    data = userlist(fields)
    return render_template("userlist.html",users = data)

@app.route("/adduser",methods=["GET","POST"])
@login_required
def add_user():
    if request.method == "GET":
        return render_template("adduser.html")
    if request.method == "POST":
         data = dict((k,v[0]) for k,v in dict(request.form).items())
         print data
         print checkuser({"name":data["name"]},"name")
         if data["name"] in checkuser({"name":data["name"]},"name"):
            errmsg = "username is exist"
            return json.dumps({"tag":1,"msg":errmsg})
         adduser(data)
         return json.dumps({"tag":0})

@app.route("/delete")
@login_required
def del_user():
    uid = request.args.get("id")
    delete(uid)
    return redirect("/userlist")

@app.route("/update",methods=["GET","POST"])
@login_required
def update():
    if request.method == "GET":
        uid = request.args.get("id")
        userinfo = getone(uid)
        return render_template("update.html",user=userinfo)
    if request.method == "POST":
        userinfo = dict((k,v[0]) for k,v in dict(request.form).items())
        if not userinfo["password"]:
            userinfo.pop("password")
        print userinfo
        modfiy(userinfo)
        return redirect("/userlist")

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

@app.route("/skin_config/")
def skin_config():
    return render_template("skin_config.html")

@app.route("/logout/")
def logout():
    session.pop('role',None)
    session.pop('username', None)
    return redirect("/login")

