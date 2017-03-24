#!/usr/bin/env python
# -*- coding: utf-8 -*-

from public import *
from db import server_list,cab_name,server_add,server_check,server_getone,server_up,server_del
from . import app
from flask import request
import json

@app.route('/server')
@login_required
def server():
    serverlist = server_list()
    return my_render("server.html",servers=serverlist)

@app.route('/addserver',methods=["GET","POST"])
@login_required
def add_server():
    if request.method == "GET":
        cab_info = cab_name()
        return my_render('addserver.html',cabinfo = cab_info)
    else:
        data = dict((k,v[0]) for k,v in dict(request.form).items())
        if server_check({"hostname":data["hostname"]}) != 0:
            return json.dumps({"code":1,"errmsg":"主机名已存在"})
        if server_check({"lan_ip":data["lan_ip"]}) != 0:
            return json.dumps({"code":1,"errmsg":"内网IP已存在"})
        if server_check({"wan_ip":data["wan_ip"]}) != 0:
            return json.dumps({"code":1,"errmsg":"外网IP已存在"})
        server_add(data)
        return json.dumps({"code":0,"result":"服务器添加成功"})

@app.route('/upserver',methods=["GET","POST"])
@login_required
def up_server():
    if request.method == "GET":
        id = request.args.get("id")
        serinfo = server_getone(id)
        cabinfo = cab_name()
        data = {"server":serinfo,"cab":cabinfo}
        return json.dumps(data)
    else:
        data = dict((k,v[0])for k,v in dict(request.form).items())
        server_up(data)
        return json.dumps({"code":0,"result":"服务器信息修改成功"})

@app.route('/delserver')
@login_required
def del_server():
    id = request.args.get("id")
    server_del(id)
    return json.dumps({"code":0,"result":"服务器删除成功"})