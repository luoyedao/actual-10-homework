#!/usr/bin/python
#coding:utf-8

from flask import render_template,request,redirect,session
from . import app
from db import get_idclist,add_idc,del_idc,update_idc,getidc
from hashlib import md5
import json


#机房列表
@app.route('/idc')
def idclist():
        #判断用户是否登录，如果没有登录就跳转到登录页
        if not session.get('name'):
                return redirect('/login')
        else:
                idc_items=["id","name","cabinets","hosts","contacts","telephone","remarks"]
                username=session.get("name")
                idclist=get_idclist(idc_items)
                print idclist
                return render_template("idclist.html",idcs=idclist,username=username)

#添加机房
@app.route("/addidc",methods=['GET','POST'])
def addidc():
        if request.method =="GET":
                username=session.get("name")
                return render_template("addidc.html",username=username)

#前端post请求，逻辑端通过request.form获取整个表单的值
        if request.method =="POST":
                idclist=dict((k,v[0]) for k,v in dict(request.form).items())
                if idclist["name"] in [ n.values()[0] for n in get_idclist(["name"]) ]:
                        errmsg = "idcname is exist"
                        return json.dumps({'code':'1','errmsg':errmsg})
                if not idclist["name"] or not idclist["telephone"]:
                        errmsg = "name and telephone is not empty"
                        return json.dumps({'code':'1','errmsg':errmsg})
                fields = ["name","cabinets","hosts","contacts","telephone","remarks"]
                values = [ '%s'%idclist[x] for x in fields]
                print values
                idcdict = dict([(k,values[i]) for i,k in enumerate(fields)])
                add_idc(idcdict)
                return json.dumps({'code':'0','result':"add sucess"})


#删除机房
@app.route("/delidc",methods=['POST'])
def delidc():
        if not session.get('name'):
                return redirect('/login')
#前端get请求，逻辑端通过request.args.get获取参数
        uid=request.args.get("uid")
        print uid
        del_idc(uid)
        return json.dumps({"code":0,"result":"delete idc success"})

#更新机房
@app.route("/updateidc",methods=['GET','POST'])
def updateidc():
        if not session.get('name'):
                return redirect('/login')
#通过id查询到要更新的数据，并渲染到更新页面
        if request.method =="GET":
                uid=request.args.get("uid")
                print uid
                idcinfo=getidc(uid)
                print idcinfo
                return json.dumps(idcinfo)
#获取到更新页面表单的值，然后提交更新
        if request.method =="POST":
                idcinfo=dict((k,v[0]) for k,v in dict(request.form).items())
		print idcinfo
                update_idc(idcinfo)
                return json.dumps({"code":0})

#服务器管理
@app.route('/server')
def server():
    return render_template("server.html")

#机柜管理
@app.route('/cabinet')
def cabinet():
    return render_template("cabinet.html")
