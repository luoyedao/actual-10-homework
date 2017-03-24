#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
import json
from flask import request
from public import *
from public import login_required
from db import *
from . import app,salt


@app.route('/')
@login_required
def index():
    return my_render("index.html")

@app.route('/userlist')
@login_required
def user_list():
    fields = ["id", "name", "name_cn", "mobile", "email", "role", "status"]
    data = userlist(fields)
    return my_render("userlist.html", users=data)

@app.route('/add',methods=["GET","POST"])
@login_required
def add():
    if request.method == "GET":
        return my_render("/add.html")
    else:
        addinfo = dict((k, v[0]) for k, v in dict(request.form).items())
        if getone({"name":addinfo["name"]}):
            return json.dumps({"code":1,"errmsg":"user is exist"})
        addinfo["password"] = hashlib.md5(addinfo["password"]+salt).hexdigest()
        adduser(addinfo)
        return json.dumps({"code":0,"result":"add user success"})

@app.route('/delete')
@login_required
def dele():
    uid = request.args.get("id")
    delete(uid)
    return json.dumps({"code":0,"result":"delete user success"})

@app.route('/update',methods=["GET","POST"])
@login_required
def up():
    if request.method == "GET":
        uid = request.args.get("id")
        userinfo = getone({"id":uid})
        return json.dumps(userinfo)
    else:
        userinfo = dict((k,v[0]) for k,v in dict(request.form).items())
        modfiy(userinfo)
        return json.dumps({"code":0,"result":"修改成功"})

@app.route('/modfpasswd',methods=["POST"])
@login_required
def uppasswd():
    data = dict((k,v[0]) for k,v in dict(request.form).items())
    print data
    if len(data) == 3:
        data["password"] = hashlib.md5(data["password"]+salt).hexdigest()
        modpasswd(data)
        return json.dumps({"code":0,"result":"密码修改成功"})
    elif len(data) == 4:
        dic = {}
        if hashlib.md5(data["password"]+salt).hexdigest() != getone({"name":data["name"]})["password"]:
            return json.dumps({"code":1,"errmsg":"密码错误"})
        dic["name"] = data["name"]
        dic["password"] = hashlib.md5(data["new_password"]+salt).hexdigest()
        modfiy(dic)
        return json.dumps({"code":0,"result":"密码修改成功"})

@app.route('/ucenter')
@login_required
def ucenter():
    username = session.get("username",None)
    userinfo = getone({"name":username})
    del userinfo["password"]
    del userinfo["status"]
    return my_render("ucenter.html", user=userinfo)