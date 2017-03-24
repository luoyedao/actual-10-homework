#!/usr/bin/env python
# -*- coding: utf-8 -*-

from public import *
from . import app
from db import cab_list,cab_getone,idc_name,cab_update,cab_del,cab_add
from flask import request
import json

@app.route('/cabinet')
@login_required
def cabinet():
    cablist = cab_list()
    return my_render("cabinet.html",cabinets=cablist)

@app.route('/cabinfo')
@login_required
def cabinfo():
    id = request.args.get("id")
    cab_info = cab_getone(id)
    idc_info = idc_name()
    return json.dumps({"cab":cab_info,"idc":idc_info})

@app.route('/cabupdate',methods=["POST"])
@login_required
def cabupdate():
    data = dict((k,v[0]) for k,v in dict(request.form).items())
    cab_update(data)
    return json.dumps({"code":0})

@app.route('/delcab')
def delcab():
    id = request.args.get("id")
    cab_del(id)
    return json.dumps({"code":0,"result":"机柜删除成功"})

@app.route('/addcabinet',methods=["GET","POST"])
def addcab():
    if request.method == "GET":
        idc_info = idc_name()
        return my_render('addcab.html',idcinfo=idc_info)
    else:
        data = dict((k,v[0]) for k,v in dict(request.form).items())
        cab_add(data)
        return json.dumps({"code":0,"result":"机柜添加成功"})