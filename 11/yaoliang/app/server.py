#!/usr/bin/python
#coding:utf-8

from flask import render_template,request,redirect,session
from . import app
import json
import db

fields_server=['id','hostname','lan_ip','wan_ip','cabinet_id','op','phone']
fields_cabinet=['id','name','idc_id','u_num','power']

@app.route('/server/')
def server():
    if not session.get('name'):
	return render_template('login.html')
    role = session.get('role')
    servers = db.list('server',fields_server)
    for i in servers:
	cabinet = db.list('cabinet',fields_cabinet,i['cabinet_id'])
	i['cabinet_id'] = cabinet['name']

    return render_template("serverlist.html",servers = servers,role = role)


@app.route("/serveradd/",methods=['GET','POST'])
def serveradd():
    if not session.get('name'):
	return redirect('/login')
    if request.method == 'GET':
	return render_template('serveradd.html',info = session,role = session.get('role'))
    if request.method == 'POST':
	data = dict((k,v[0]) for k,v in dict(request.form).items())
	l = []

	for i in db.list('server',fields_server):
	    l.append(i['hostname'])
	if not data['hostname']:
	    return json.dumps({'code':1,'errmsg':'hostname can not be null'})
	elif data['hostname'] not in l:
	    conditions = [ "%s='%s'" %  (k,v) for k,v in data.items()]
	    db.add('server',conditions)
	    return json.dumps({'code':0,'result':'add server success'})
	return json.dumps({'code':1,'errmsg':'server name is exist'})

@app.route('/server_update_msg/')
def server_update_msg():
    id = request.args.get('id')
    server = db.list('server',fields_server,id)
    return json.dumps({'code':0,'result':server})

@app.route('/server_update/',methods=['GET','POST'])
def server_update():
    if not session.get('name'):
	return redirect('/login')
    data = dict((k,v[0]) for k,v in dict(request.form).items())
    conditions = [ "%s='%s'" %  (k,v) for k,v in data.items()]
    db.update('server',conditions,data['id'])
    return json.dumps({'code':0,'result':'update completed!'})

@app.route('/server_delete/',methods=['POST'])
def server_delete():
    if session.get('role') != 'admin':
	return redirect('/login')
    id = request.form.get('id')
    db.delete('server',id)
    return json.dumps({'code':0,'result':'delete success!'})
