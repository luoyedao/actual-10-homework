#!/usr/bin/env python
#coding:utf-8

import time
import json
import traceback
from . import app
from flask import request,render_template,redirect,session
from cdbapi import *

@app.route('/server')
def server():
  if not session.get('username'):
    return redirect('/login')
  fields=['id','name','lan_ip','wan_ip','cabinet_name','op','phone']
  data=c_sel(fields,tb="server")
  data2=c_sel(fields=['name'],tb="cabinet")
  return render_template("cmdb/server.html",serinfo=data,cabname=data2)

@app.route('/addser',methods = ['POST'])
def addser():
  data=dict((k,v[0]) for k,v in dict(request.form).items()) #无序的数据
  data['create_time']=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
  data['mod_time']=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
  fields=['name','lan_ip','wan_ip','cabinet_name','op','phone','create_time','mod_time']
  try:
    res=c_add(fields,data,tb="server")
    if res:
      msg = 'add success'
      return json.dumps({'code' : 0,'result' : msg})
  except:
    msg = 'add failed'
    print traceback.print_exc()
    return json.dumps({'code' : 1,'result' : msg})

@app.route('/editser',methods = ['GET','POST'])
def editser():
  if request.method == "GET":
    if not session.get('username'):
      return redirect('/login')
    fields=['id','name','lan_ip','wan_ip','cabinet_name','op','phone']
    data=c_sel(fields,tb="server",cid=request.args.get('cid'))  #select 出来的数据是无序的，需要用fields来一一对应
    info=dict((k,data[i]) for i,k in enumerate(fields))
    return json.dumps(info)
  if request.method == "POST":
    if not session.get('username'):
      return redirect('/login')
    try:
      data=dict(request.form) #无序，update无需有序
      now=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
      data['mod_time']=[unicode(now)]
      c_edit(data,tb="server")
      return json.dumps({'code' : 0})
    except:
      print traceback.print_exc()
      return json.dumps({'code' : 1})

@app.route('/delser')
def delser():
  try:
    cid=request.args.get('cid')
    c_del(cid,tb="server")
    return json.dumps({'code' : 0})
  except:
    print traceback.print_exc()
    return json.dumps({'code' : 1})

