#!/usr/bin/env python
# -*- coding: utf-8 -*-

from public import *
from . import app
from db import idclist,idc_getone,idc_update,idc_check,idc_add,idc_del
from flask import request
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#显示IDC列表
@app.route('/idc')
@login_required
def idcs():
    idc_list = idclist()
    return my_render("idc.html",idc_list=idc_list)

#获取单个IDC信息
@app.route('/idcinfo')
@login_required
def oneinfo():
    id = request.args.get("id")
    info = idc_getone({"id":id})
    return json.dumps(info)

#更新IDC信息
@app.route('/idcupdate',methods=["POST"])
@login_required
def idcupdate():
    info = dict((k,v[0])for k,v in dict(request.form).items())
    idc_update(info)
    return json.dumps({"code":0})

#添加IDC
@app.route('/addidc',methods=["GET","POST"])
@login_required
def idcadd():
    if request.method == "GET":
        return my_render("addidc.html")
    else:
        data = dict((k,v[0]) for k,v in dict(request.form).items())
        if idc_check(data["name"]):
            idc_add(data)
            return json.dumps({"code":0,"result":"机房添加成功"})
        else:
            return json.dumps({"code":1,"errormsg":"机房已存在"})

#删除IDC
@app.route('/delidc')
@login_required
def idcdel():
    id = request.args.get("id")
    idc_del(id)
    return json.dumps({"code":0,"result":"机房删除成功"})