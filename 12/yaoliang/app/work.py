#!/usr/bin/python
#coding:utf-8

from flask import render_template,request,redirect,session
from . import app
from config import * 
from utils import login_request
import json
import db
import time
#from utils import myMail

app.config.from_object(Table)
app.config.from_object(MyEmail)
fields_work = app.config.get('FIELDS_WORK')  
fields_user = app.config.get('FIELDS_USER')  
localemail = app.config.get('LOCAL_EMAIL')
passwd = app.config.get('LOCAL_PASSWD')
ISOTIMEFORMAT='%Y-%m-%d %X'

@app.route('/worklist/')
@login_request.login_request
def worklist():
    role = session.get('role')
    works = db.list('work',fields_work)
    list_works = []
    for work in works:
        if int(work['work_status']) == 0:
	    list_works.append(work)
    return render_template("/work/worklist.html",works = list_works,role = role)

@app.route('/workhistory/')
@login_request.login_request
def workhistory():
    role = session.get('role')
    works = db.list('work',fields_work)
    history_works = []
    for work in works:
        if int(work['work_status']) != 0:
    	    history_works.append(work)
    return render_template("/work/workhistory.html",works = history_works,role = role)

@app.route("/workadd/",methods=['GET','POST'])
@login_request.login_request
def workadd():
    name = session.get('name')
    id = session.get('id')
    if request.method == 'GET':
	return render_template('/work/workadd.html',info = session,role = session.get('role'))
    else:
	data = dict((k,v[0]) for k,v in dict(request.form).items())
	data['des_name'] = name

	if not data['operate']:
	    return json.dumps({'code':1,'errmsg':'work description can not be null'})
	conditions = [ "%s='%s'" %  (k,v) for k,v in data.items()]
	db.add('work',conditions)

#	# 获取申请人email地址
#        user = db.list('users',fields_user,id)
#	# 从用户列表获取邮箱账号和密码(暂时没有)
#        email,passwd = user['email'],user['password']
#	# 发送邮件(需要发件人账号密码，密码，收件人，正文)
#        myMail.mymail(email,passwd,localemail,data)

	return json.dumps({'code':0,'result':'apply work success'})

# 获取工单状态
@app.route('/work_status/')
@login_request.login_request
def work_status():
    id = request.args.get('id')
    work = db.list('work',fields_work,id)
    operate = work['operate']
    work_status = work['work_status']
    return json.dumps({'code':0,'result1':operate,'result2':work_status})

# 修改工单状态
''' 
{'0':'未处理','1':'处理中','2':'完成'}
'''
@app.route('/update_status/',methods=['POST'])
@login_request.login_request
def update_status():
    data = dict((k,v[0]) for k,v in dict(request.form).items())
    res = {}
    if data['work_status'] == '1':
	data['handle_name'] = session.get('name')
#	# 获取申请人email地址
#        user = db.list('users',fields_user,session.get('id'))
#        email = user['email']
#        res['operate'] = 'Consent to apply'
#        res['work'] = 'Consent to apply'
#	# 发送邮件
#	myMail.mymail(localemail,passwd,email,res)
    else:
	data['handle_time'] = time.strftime(ISOTIMEFORMAT,time.localtime())
#	myMail.mymail()

    conditions = [ "%s='%s'" %  (k,v) for k,v in data.items()]
    db.update('work',conditions,data['id'])
    return json.dumps({'code':0,'result':'execute completed!'})

