#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-08-06 18:43:07
# @Author  : yang ke (jack_keyang@163.com)

from run import app
from flask import render_template,request,redirect,url_for
from api import get_userlist,add_user,del_user,getone,up_user

@app.route("/")
def index():
    field_lsit = ["id","name","name_cn","email","mobile","role","status"]
    userlist = get_userlist(field_lsit)
    return render_template("index.html",users = userlist)

@app.route("/adduser",methods=['GET','POST'])
def adduser():
    if request.method == "GET":
        return render_template("adduser.html")
    if request.method == "POST":
        name = request.form['username']
        name_cn = request.form['username_cn']
        passwd = request.form['password']
        re_passwd = request.form['re_password']
        email = request.form['email']
        mobile = request.form['mobile']
        role = request.form['role']
        statu = request.form['statu']
        uesr_list = get_userlist(["name"])
        if len(name) == 0 or len(name_cn) == 0 or len(passwd) == 0 or len(email) == 0 or len(mobile) == 0:
            msg = u"输入框不能为空"
            return render_template("adduser.html",msg=msg)
        if name in map(lambda x:x["name"],uesr_list):
            msg = u"用户已存在"
            return render_template("adduser.html",msg=msg)
        if passwd != re_passwd:
            msg = u"２次输入密码不同"
            return render_template("adduser.html",msg=msg)
        userinfo = [name,name_cn,passwd,email,mobile,role,statu]
        add_user(userinfo)
        return redirect("/")

@app.route("/userdel")
def userdel():
    uid = request.args.get("uid")
    del_user(uid)
    return redirect("/")

@app.route("/modfiy",methods=['GET','POST'])
def modfiy():
    if request.method == "GET":
        uid = request.args.get("uid")
        userinfo = getone(uid)
        return render_template("modfiy.html",user = userinfo)
    if request.method == "POST":
        userinfo = {}
        userinfo["name"] = request.form['name']
        userinfo["email"] = request.form['email']
        userinfo["mobile"] = request.form['mobile']
        userinfo["role"] = request.form['role']
        userinfo["status"] = request.form['statu']
        up_user(userinfo)
        return redirect("/")
