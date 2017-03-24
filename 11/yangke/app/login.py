#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
import json

from flask import request

from public import *
from public import login_required
from db import *
from . import app,salt


@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        login_info = dict((k, v[0]) for k, v in dict(request.form).items())
        login_info["password"] = hashlib.md5(login_info["password"]+salt).hexdigest()
        result = getone({"name": login_info["name"]})
        if not getone({"name":login_info["name"]}):
            return json.dumps({"code": 0, "result":"用户不存在"})
        if login_info["password"] != getone({'name': login_info["name"]})["password"]:
            return json.dumps({"code": 0, "result":"密码错误"})
        if result["status"] != "0":
            return json.dumps({"code":0,"result":'用户被锁定'})

        session["role"] = result["role"]
        session["username"] = login_info["name"]
        return json.dumps({"code": 1,"result":"登陆成功"})

@app.route("/logout/")
@login_required
def logout():
    session.pop("username",None)
    session.pop("role",None)
    return redirect("/login")