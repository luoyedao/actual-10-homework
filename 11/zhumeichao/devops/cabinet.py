#!/usr/bin/env python
#coding:utf-8

import time
import json
import traceback
from . import app
from flask import request,render_template,redirect,session
from cdbapi import *

@app.route('/cabinet')
def cabinet():
  if not session.get('username'):
    return redirect('/login')
  fields=['id','name','idc_name','u_num','power']
  data=c_sel(fields,tb="cabinet")
  data2=c_sel(fields=['name'],tb="idc")
  return render_template("cmdb/cabinet.html",cabinfo=data,idcname=data2)

@app.route('/addcab',methods = ['POST'])
def addcab():
  data=dict((k,v[0]) for k,v in dict(request.form).items()) #无序的数据
  data['create_time']=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
  data['mod_time']=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
  fields=['name','idc_name','u_num','power','create_time','mod_time']
  try:
    res=c_add(fields,data,tb="cabinet")
    if res:
      msg = 'add success'
      return json.dumps({'code' : 0,'result' : msg})
  except:
    msg = 'add failed'
    print traceback.print_exc()
    return json.dumps({'code' : 1,'result' : msg})

@app.route('/editcab',methods = ['GET','POST'])
def editcab():
  if request.method == "GET":
    if not session.get('username'):
      return redirect('/login')
    fields=['id','name','idc_name','u_num','power']
    data=c_sel(fields,tb="cabinet",cid=request.args.get('cid'))  #select 出来的数据是无序的，需要用fields来一一对应
    info=dict((k,data[i]) for i,k in enumerate(fields))
    return json.dumps(info)
  if request.method == "POST":
    if not session.get('username'):
      return redirect('/login')
    try:
      data=dict(request.form) #无序，update无需有序
      now=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
      data['mod_time']=[unicode(now)]
      c_edit(data,tb="cabinet")
      return json.dumps({'code' : 0})
    except:
      print traceback.print_exc()
      return json.dumps({'code' : 1})

@app.route('/delcab')
def delcab():
  try:
    cid=request.args.get('cid')
    c_del(cid,tb="cabinet")
    return json.dumps({'code' : 0})
  except:
    print traceback.print_exc()
    return json.dumps({'code' : 1})

