#!/usr/bin/env python
# Program:
#	This program is the The routing function
# Author:   Tantianran    15915822634@139.com
# last modification time:  /2016/08/26    
# Version:  v1.1

# Import time module
import time

# Import need to use the module
from db import get_user_name,check_login_name,get_user_all,del_by_id,update_user_data,get_by_id,add_set_user,update_user_lasttime
from flask import render_template,request,redirect,session
from run import app
import json
app.secret_key="!q2@1w#E3$4R5T^y&uI8(oe)2d*%"

# '''Exit xu cancellation function'''
@app.route('/loginout')
def loginout():
    session.pop('name')
    return redirect('/login')

# '''Routing function is used to login'''
@app.route('/')
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == "POST":
	data = dict((k,v[0]) for k,v in dict(request.form).items())
	if not data.get('name',None) or not data.get('password',None):
	    errmsg = "name and password not null"
	    return json.dumps({'code':'1','errmsg':errmsg})
	if not check_login_name(data['name']):
	    errmsg = "user does not exist"
	    return json.dumps({'code':'1','errmsg':errmsg})
	if data['password'] != get_user_name(data['name'])['password']:
	    errmsg = "password error!"
	    return json.dumps({'code':'1','errmsg':errmsg})
	if get_user_name(data['name'])['status'] == 0:
	    errmsg = "Your account has been locked"
	    return json.dumps({'code':'1','errmsg':errmsg})
	else:
	    date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
	    update_user_lasttime(date,data['name'])
	    session['name'] = data['name']
	    session['role'] = get_user_name(data['name'])['role']
	    session['status'] = get_user_name(data['name'])['status']
	    role = session.get('role',None)
	    names = session.get('name',None)
	    status = session.get('status',None)
	    return json.dumps({'code':'0','roles':role,'name':names,'statu':status})
    else:
	return render_template('login.html')

@app.route('/admin')
def index():
    if not session.get('name',None) or session.get('role',None) != 'admin':
	return redirect('/login')
    names = session.get('name',None)
    roles = session.get('role',None)
    del_by_id(request.args.get('id'))
    return render_template('index.html',users=get_user_all(), name=names,role=roles)

# '''Only the administrator can add users'''
@app.route('/admin/adduser/', methods=['GET','POST'])
def adduser():
    if not session.get('name',None) or session.get('role',None) != 'admin':
        return redirect('/login')
    if request.method == "POST":
	userdict = dict((k,v[0]) for k,v in dict(request.form).items())
	if not userdict.get('name',None):
	    errmsg = "sorry, please fill out the information"
	    return json.dumps({'code':'1','errmsg':errmsg})
        else:
	    add_set_user(','.join(['"%s"' % (v[0]) for k,v in dict(request.form).items()]))
	    return json.dumps({'code':'0','errmsg':"Users to add success"})
    else:
	names = session.get('name',None)
	return render_template('adduser.html',name=names)

@app.route('/admin/update', methods=['GET','POST'])
def update():
    if not session.get('name',None) or session.get('role',None) != 'admin':
        return redirect('/login')
    if request.method == "POST":
	userdict = dict(request.form)
	userlist = ["%s='%s'" % (k,v[0]) for k,v in userdict.items()]
	update_user_data(','.join(userlist),userdict['id'][0])
        return json.dumps({'code':'0','errmsg':"update sucess"})
    else:
	roles = session.get('role',None)
	names = session.get('name',None)
	return render_template('update.html',user=get_by_id(request.args.get('id')),role=roles,name=names)

@app.route('/admin/chagepasswd', methods=['GET','POST'])
def chagepasswd():
    if not session.get('name',None) or session.get('role',None) != 'admin':
        return redirect('/login')
    if request.method == "POST":
	userdict = dict(request.form)
	new_password = ["%s='%s'" % (k,v[0]) for k,v in userdict.items()][1]
	update_user_data(new_password,userdict['id'][0])
	return json.dumps({'code':'0','errmsg':"chage password sucess"})
    else:
	roles = session.get('role',None)
	names = session.get('name',None)
        return render_template('admin_passwd.html',user=get_by_id(request.args.get('id')),name=names,role=roles)

@app.route('/user')
def user():
    if not session.get('name',None) or session.get('role',None) != 'user':
	return redirect('/login')
    names = session.get('name',None)
    roles = session.get('role',None)
    return render_template('user.html',user=get_user_name(names), name=names,role=roles)

@app.route('/user/update', methods=['GET','POST'])
def user_update():
    if not session.get('name',None) or session.get('role',None) != 'user':
        return redirect('/login')
    if request.method == "POST":
	userdict = dict(request.form)
	userlist = ["%s='%s'" % (k,v[0]) for k,v in userdict.items()]
	update_user_data(','.join(userlist),userdict['id'][0])
        return json.dumps({'code':'0','errmsg':"update sucess"})
    else:
	roles = session.get('role',None)
	names = session.get('name',None)
	return render_template('user_update.html',user=get_by_id(request.args.get('id')),role=roles,name=names)

@app.route('/user/chagepasswd', methods=['GET','POST'])
def userchagepasswd():
    if not session.get('name',None) or session.get('role',None) != 'user':
        return redirect('/login')
    if request.method == "POST":
	userdict = dict(request.form)
	if userdict['def_passwd'][0] != get_by_id(request.form.get('id'))['password']:
	    errmsg = "password error!"
	    return json.dumps({'code':'1','errmsg':errmsg})
        if userdict['rep_passwd'][0] != userdict['password'][0]:
	    errmsg = "the two passwords don't match"
	    return json.dumps({'code':'1','errmsg':errmsg})
	else:
	    new_password = ["%s='%s'" % (k,v[0]) for k,v in userdict.items()][1]
	    update_user_data(new_password,userdict['id'][0])
	    return json.dumps({'code':'0','errmsg':"chage password sucess"})
    else:
	roles = session.get('role',None)
	names = session.get('name',None)
        return render_template('user_passwd.html',user=get_by_id(request.args.get('id')),name=names,role=roles)











