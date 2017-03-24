#!/usr/bin/env python
#@The author: toby (15915822634@139.com)
#@Date: 2016-08-09

from flask import render_template,request,redirect
from run import app
from work import adduser,getuser,queryuser,deluser,queryuserid,Updateuser,check_loginname

@app.route('/', methods=['GET','POST'])
def loging():
    if request.method == "POST":
	login_username = request.form.get('login_username')
	login_password = request.form.get('login_password')
	if check_loginname(login_username) == True:
	    userdict = queryuser(login_username)
	    if userdict['role'] == 'admin':
		return redirect('/admin')
            if login_username == userdict['name']:
	        if login_password == userdict['password']:
		    return render_template('login_complete.html',username=userdict['name'])
	        else:
		    return render_template('login.html',login_error='Password error')
	else:	
	    return render_template('login.html',login_error='User not found')
    else:
	return render_template('login.html')

@app.route('/admin', methods=['GET','POST'])
def admin():
    if request.method == "POST":
	deluser(request.form.get('del_name'))
	queryname = request.form.get('query_name')
	query_info = queryuser(queryname)
        return render_template('admin.html',userinfo=getuser(),queryinfo=query_info)
    else:
	queryname = request.args.get('query_name')
	query_info = queryuser(queryname)
	return render_template('admin.html',userinfo=getuser(),queryinfo=query_info)
	
@app.route('/reguser', methods=['GET','POST'])
def reguser():
    if request.method == "POST":
        reg_name = request.form.get('reg_name')
	if reg_name == '':
	    return render_template('reguser.html', error='User name cannot be empty')
	reg_password = request.form.get('reg_password')
        repeat_password = request.form.get('repeat_password')
	if repeat_password != reg_password:
	    return render_template('reguser.html', error='Passwords don\'t match')
	reg_name_cn = request.form.get('reg_name_cn')
	if reg_name_cn == '':
	    return render_template('reguser.html', error='Chinese name cannot be empty')
	reg_email = request.form.get('reg_email')
	if reg_email == '':
	    return render_template('reguser.html', error='Email cannot be empty')
	reg_mobile = request.form.get('reg_mobile')
	if reg_mobile == '':
	    return render_template('reguser.html', error='mobile cannot be empty')
	reg_role = request.form.get('reg_role')
	if reg_role == '':
	    return render_template('reguser.html', error='role cannot be empty')
	else:
	    adduser(reg_name,reg_name_cn,reg_password,reg_email,reg_mobile,reg_role)
	    query_info = queryuser(reg_name)
	    return render_template('reg_complete.html',queryinfo=query_info)
    else:
        return render_template('reguser.html')

@app.route('/updateuser', methods=['GET','POST'])
def updateuser():
    userdata = Updateuser()
    if request.method == "POST":
	userid = request.form.get('userid')
	get_userid = request.form.get('get_userid')
	reg_name = request.form.get('reg_name')
	reg_name_cn = request.form.get('reg_name_cn')
	reg_password = request.form.get('reg_password')
        repeat_password = request.form.get('repeat_password')
	if repeat_password != reg_password:
	    return render_template('updateuser.html',queryinfo=queryuserid(userid), info='Passwords don\'t match')
	reg_email = request.form.get('reg_email')
	reg_mobile = request.form.get('reg_mobile')
	reg_role = request.form.get('reg_role')
	if userdata.setuserinfo(reg_name,reg_name_cn,reg_password,reg_email,reg_mobile,reg_role,get_userid) == False:
	    return render_template('updateuser.html',queryinfo=queryuserid(userid))
	else:
	    return render_template('updateuser.html',queryinfo=queryuserid(userid),info='Good! Update complete...')
    else:
	return render_template('updateuser.html')

@app.route('/userchange', methods=['GET','POST'])
def userchange():
    if request.method == "POST":
	chage = Updateuser()
	default_username = request.form.get('default_username')
	default_password = request.form.get('default_password')
	new_password = request.form.get('new_password')
	repeat_password = request.form.get('repeat_password')
	if check_loginname(default_username) == True:
	    userdict = queryuser(default_username)
	    if default_username == userdict['name']:
	        if default_password == userdict['password']:
		    if repeat_password == new_password:
		        chage.chagepasswd(default_username,new_password)
		        return render_template('userchange.html',change_complete='Password modification completed')
		    else:
		        return render_template('userchange.html',error='Passwords don\'t match')
	        else:
		    return render_template('userchange.html',error='Password error')
	else:
	    return render_template('userchange.html', error='User name Error')
    else:
        return render_template('userchange.html')
