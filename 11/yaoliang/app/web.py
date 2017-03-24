#!/usr/bin/python
#coding:utf-8

from flask import render_template,request,redirect,session
from . import app
from hashlib import md5
import json
import db

salt = '890iop*()'
fields_user = ['id','name','name_cn','password','email','mobile','role','status']

@app.route('/')
@app.route('/index/')
def index():
    sesname = session.get('name')
    if not sesname:
	return redirect('/login')
    role = session.get('role')
    return render_template('index.html',role=role)


@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    else:
	name = request.form.get('name')
	password = md5(request.form.get('password')+salt).hexdigest()
	print password

	d = {}
        for i in db.list('users',fields_user):
	    d[i['name']] = [i['password'],i['role'],i['id'],i['status']]
        if not name or not password:
	    errmsg = 'name or password not be null'
	    return json.dumps({'code':'1','errmsg':errmsg})
	elif d[name][3] != 0:
	    return json.dumps({'code':'1','errmsg':'user is locked'})

	elif name in d and d[name][0]==password:
	    session['name']=name
	    session['role']=d[name][1]
	    session['id']=d[name][2]
            return json.dumps({'code':'0','result':'login success'})
	else:
	    errmsg = 'name or password wrong'
	    return json.dumps({'code':'1','errmsg':errmsg})

@app.route("/userlist/")
def userlist():
    if not session.get('name'):
	return render_template('login.html')
    role = session.get('role')
    if role == 'admin':
	users = db.list('users',fields_user)
	return render_template("userlist.html",users = users,role = role)
    else:
        user = db.list('users',fields_user,session.get('id'))
        return render_template("userself.html",user = user,role = role)

@app.route("/userself/")
def userself():
    if not session.get('name'):
	return render_template('login.html')
    role = session.get('role')
    id = session.get('id')
    user = db.list('users',fields_user,id)
    return render_template("userself.html",user = user,role = role)

@app.route("/useradd/",methods=['GET','POST'])
def useradd():
    if not session.get('name'):
	return redirect('/login')
    if request.method == 'GET':
	return render_template('add.html',role = session.get('role'))
    if request.method == 'POST':
	l = []
	data = dict((k,v[0]) for k,v in dict(request.form).items())
	data['password'] = md5(request.form.get('password')+salt).hexdigest()

	for i in db.list('users',fields_user):
	    l.append(i['name'])
	if not data['name']:
	    return json.dumps({'code':1,'errmsg':'name can not be null'})
	elif not data['name_cn']:
	    return json.dumps({'code':1,'errmsg':'chinese name can not be null'})
	elif not data['password']:
	    return json.dumps({'code':1,'errmsg':'password can not be null'})
	elif data['name'] not in l:
	    conditions = [ "%s='%s'" %  (k,v) for k,v in data.items()]
	    db.add('users',conditions)
	    return json.dumps({'code':0,'result':'add user success'})
	return json.dumps({'code':1,'errmsg':'username is exist'})

@app.route('/modpwd/',methods=['POST'])
def modpwd():
    if not session.get('name'):
	return redirect('/login')
    data = dict(request.form)
    if 'password' in data.keys():
	if not data['password'][0] or not data['newpassword'][0] or not data['renewpassword'][0]:
	    errmsg = 'password can not be null'
	    return json.dumps({'code':'1','errmsg':errmsg})
    else:
	if not data['newpassword'][0] or not data['renewpassword'][0]:
	    errmsg = 'password can not be null'
	    return json.dumps({'code':'1','errmsg':errmsg})

    try:
	condition = [ "%s='%s'" %  ('password',md5(v[0]+salt).hexdigest()) for k,v in data.items() if k == 'newpassword']
	id = session.get('id')
	if session.get('role') == 'admin':
	    db.update('users',condition,data['id'][0])
	    return json.dumps({'code':'0','result':'modify completed!'})
	else:
	    if md5(data['password'][0]+salt).hexdigest() == db.list('users',fields_user,id)['password']:
		db.update('users',condition,data['id'][0])
		return json.dumps({'code':'0','result':'modify completed!'})
	    return json.dumps({'code':'1','errmsg':'wrong old password'})
    except:
	errmsg = "modify failed" 
	return json.dumps({'code':'1','errmsg':errmsg})

@app.route('/delete/',methods=['POST'])
def delete():
    if session.get('role') != 'admin':
	return redirect('/login')
    id = request.form.get('id')
    db.delete('users',id)
    return json.dumps({'code':0,'result':'delete success!'})


@app.route('/update_msg/')
def update_msg():
    id = request.args.get('id')
    user = db.list('users',fields_user,id)
    if session.get('role') == 'admin':
	return json.dumps({'code':0,'result':user})
    else:
	return json.dumps({'code':2,'result':user})

@app.route('/update/',methods=['GET','POST'])
def update():
    if not session.get('name'):
	return redirect('/login')
    data = dict((k,v[0]) for k,v in dict(request.form).items())
    conditions = [ "%s='%s'" %  (k,v) for k,v in data.items()]
    db.update('users',conditions,data['id'])
    return json.dumps({'code':0,'result':'update completed!'})

@app.route('/logout/')
def loginout():
    if session:
	session.pop('role')
	session.pop('name')
	return redirect('/login')
    return redirect('/login')
