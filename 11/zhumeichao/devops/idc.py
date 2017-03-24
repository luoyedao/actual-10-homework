#!/usr/bin/env python
#coding:utf-8

import time
import json
import traceback
from . import app
from flask import request,render_template,redirect,session
from cdbapi import *

@app.route('/idc')
def idc():
  if not session.get('username'):
    return redirect('/login')
  fields=['id','name','name_cn','address','linkman','phone','num']
  data=c_sel(fields,tb="idc")
  return render_template("cmdb/idc.html",idcinfo=data)

@app.route('/addidc',methods = ['POST'])
def addidc():
  data=dict((k,v[0]) for k,v in dict(request.form).items()) #无序的数据
  data['create_time']=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
  data['mod_time']=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
  fields=['name','name_cn','address','linkman','phone','num','create_time','mod_time']
  try:
    res=c_add(fields,data,tb="idc")
    if res:
      msg = 'add success'
      return json.dumps({'code' : 0,'result' : msg})
  except:
    msg = 'add failed'
    print traceback.print_exc()
    return json.dumps({'code' : 1,'result' : msg})

@app.route('/editidc',methods = ['GET','POST'])
def editidc():
  if request.method == "GET":
    if not session.get('username'):
      return redirect('/login')
    fields=['id','name','name_cn','address','linkman','phone','num']
    data=c_sel(fields,cid=request.args.get('cid'),tb="idc")  #select 出来的数据是无序的，需要用fields来一一对应
    info=dict((k,data[i]) for i,k in enumerate(fields))
    return json.dumps(info)
  if request.method == "POST":
    if not session.get('username'):
      return redirect('/login')
    try:
      data=dict(request.form) #无序，update无需有序
      now=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
      data['mod_time']=[unicode(now)]
      c_edit(data,tb="idc")
      return json.dumps({'code' : 0})
    except:
      print traceback.print_exc()
      return json.dumps({'code' : 1})

@app.route('/delidc')
def delidc():
  try:
    cid=request.args.get('cid')
    c_del(cid,tb="idc")
    return json.dumps({'code' : 0})
  except:
    print traceback.print_exc()
    return json.dumps({'code' : 1})

