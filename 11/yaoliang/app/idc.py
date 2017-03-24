#!/usr/bin/python
#coding:utf-8

from flask import render_template,request,redirect,session
from . import app
import json
import db

fields_idc=['id','name','name_cn','address','adminer','phone','num']

@app.route('/idc/')
def idc():
    if not session.get('name'):
	return render_template('login.html')
    role = session.get('role')
    idcs = db.list('idc',fields_idc)
    return render_template("idclist.html",idcs = idcs,role = role)

@app.route('/idc_msg/')
def idc_msg():
    if not session.get('name'):
	return render_template('login.html')
    idcs = db.list('idc',fields_idc)
    return json.dumps({'result':idcs}) 

@app.route("/idcadd/",methods=['GET','POST'])
def idcadd():
    if not session.get('name'):
	return redirect('/login')
    if request.method == 'GET':
	return render_template('idcadd.html',info = session,role = session.get('role'))
    if request.method == 'POST':
	data = dict((k,v[0]) for k,v in dict(request.form).items())
	print data
	l = []

	for i in db.list('idc',fields_idc):
	    l.append(i['name'])
	if not data['name']:
	    return json.dumps({'code':1,'errmsg':'name can not be null'})
	elif data['name'] not in l:
	    conditions = [ "%s='%s'" %  (k,v) for k,v in data.items()]
	    db.add('idc',conditions)
	    return json.dumps({'code':0,'result':'add idc success'})
	return json.dumps({'code':1,'errmsg':'idc name is exist'})

@app.route('/idc_update_msg/')
def idc_update_msg():
    id = request.args.get('id')
    idc = db.list('idc',fields_idc,id)
    return json.dumps({'code':0,'result':idc})

@app.route('/idc_update/',methods=['GET','POST'])
def idc_update():
    if not session.get('name'):
	return redirect('/login')
    data = dict((k,v[0]) for k,v in dict(request.form).items())
    conditions = [ "%s='%s'" %  (k,v) for k,v in data.items()]
    db.update('idc',conditions,data['id'])
    return json.dumps({'code':0,'result':'update completed!'})

@app.route('/idc_delete/',methods=['POST'])
def idc_delete():
    if session.get('role') != 'admin':
	return redirect('/login')
    id = request.form.get('id')
    db.delete('idc',id)
    return json.dumps({'code':0,'result':'delete success!'})
