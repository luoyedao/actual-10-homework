#!/usr/bin/python
#coding:utf-8

from flask import Flask,render_template,request,redirect,session
import json
import db
import idcdb

app = Flask(__name__)
app.secret_key='\xd1\xfe\xfb\x7fH\xbf\xc8Q\x17-\xab\xc6\x80u2\xc2\xb6\n9\x00\x87\xa7\xa75'

@app.route('/')
@app.route('/index')
def index():
    sesname = session.get('name')
    if not sesname:
	return redirect('/login')
    return render_template('index.html')


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    else:
	name = request.form.get('name')
	password = request.form.get('password')

	d = {}
        for i in db.userlist():
	    d[i['name']] = [i['password'],i['role']]
	if name in d and d[name][0]==password:
	    session['name']=name
	    session['role']=d[name][1]
            return json.dumps({'code':'0','result':'login success'})

        elif not name or not password:
	    errmsg = 'name or password not be null'
	    return json.dumps({'code':'1','errmsg':errmsg})
	else:
	    errmsg = 'name or password wrong'
	    return json.dumps({'code':'1','errmsg':errmsg})

@app.route("/userlist/")
def userlist():
    if not session.get('name'):
	return render_template('login.html')
    role = session.get('role')
    if role == 'admin':
	users = db.userlist()
	return render_template("userlist.html",users = users,role = role)
    else:
        user = db.userlist(session.get('name'))
	info = 'you are not admin'
        return render_template("userself.html",user = user,role = role,info = info)

@app.route("/userself/")
def userself():
    if not session.get('name'):
	return render_template('login.html')
    role = session.get('role')
    name = session.get('name')
    user = db.userlist(session.get('name'))
    return render_template("userself.html",user = user,role = role)

@app.route("/add",methods=['GET','POST'])
def add():
    if not session.get('name'):
	return redirect('/login')
    if request.method == 'GET':
	return render_template('add.html',info = session)
    if request.method == 'POST':
	l = []
	data = dict((k,v[0]) for k,v in dict(request.form).items())
	for i in db.userlist():
	    l.append(i['name'])
	if not data['name']:
	    return json.dumps({'code':1,'errmsg':'name can not be null'})
	elif not data['name_cn']:
	    return json.dumps({'code':1,'errmsg':'chinese name can not be null'})
	elif not data['password']:
	    return json.dumps({'code':1,'errmsg':'password can not be null'})
	elif data['name'] not in l:
	    conditions = [ "%s='%s'" %  (k,v) for k,v in data.items()]
	    db.useradd(conditions)
	    return json.dumps({'code':0,'result':'add user success'})
	return json.dumps({'code':1,'errmsg':'username is exist'})

@app.route('/modpwd',methods=['POST'])
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

    if data['newpassword'][0] != data['renewpassword'][0]:
	errmsg = 'The two passwords you entered do not match'
	return json.dumps({'code':'1','errmsg':errmsg})
    try:
	condition = [ "%s='%s'" %  ('password',v[0]) for k,v in data.items() if k == 'newpassword']
	sesname = session.get('name')
	if session.get('role') == 'admin':
	    db.update(condition,data['id'][0])
	    return json.dumps({'code':'0','result':'modify completed!'})
	else:
	    if data['password'][0] == db.userlist(sesname)['password']:
		db.update(condition,data['id'][0])
		return json.dumps({'code':'0','result':'modify completed!'})
	    return json.dumps({'code':'1','errmsg':'wrong old password'})
    except:
	errmsg = "modify failed" 
	return json.dumps({'code':'1','errmsg':errmsg})

@app.route('/delete',methods=['POST'])
def delete():
    if session.get('role') != 'admin':
	return redirect('/login')
    id = request.form.get('id')
    db.deluser(id)
    return json.dumps({'code':0,'result':'delete success!'})


@app.route('/update_msg')
def update_msg():
    name = request.args.get('name')
    user = db.userlist(name)
    if session.get('role') == 'admin':
	return json.dumps({'code':0,'result':user})
    else:
	return json.dumps({'code':2,'result':user})

@app.route('/update',methods=['GET','POST'])
def update():
    if not session.get('name'):
	return redirect('/login')
    data = dict((k,v[0]) for k,v in dict(request.form).items())
    conditions = [ "%s='%s'" %  (k,v) for k,v in data.items()]
    db.update(conditions,data['id'])
    return json.dumps({'code':0,'result':'update completed!'})


@app.route('/idc/')
def idc():
    if not session.get('name'):
	return render_template('login.html')
    role = session.get('role')
    idcs = idcdb.idclist()
    return render_template("idclist.html",idcs = idcs,role = role)

@app.route("/idcadd",methods=['GET','POST'])
def idcadd():
    if not session.get('name'):
	return redirect('/login')
    if request.method == 'GET':
	return render_template('idcadd.html',info = session)
    if request.method == 'POST':
	data = dict((k,v[0]) for k,v in dict(request.form).items())
	l = []

	for i in idcdb.idclist():
	    l.append(i['name'])
	if not data['name']:
	    return json.dumps({'code':1,'errmsg':'name can not be null'})
	elif not data['idc_supplier']:
	    return json.dumps({'code':1,'errmsg':'idc supplier name can not be null'})
	elif not data['idc_address']:
	    return json.dumps({'code':1,'errmsg':'idc address can not be null'})
	elif not data['operation']:
	    return json.dumps({'code':1,'errmsg':'operation can not be null'})
	elif data['name'] not in l:
	    conditions = [ "%s='%s'" %  (k,v) for k,v in data.items()]
	    idcdb.idcadd(conditions)
	    return json.dumps({'code':0,'result':'add idc success'})
	return json.dumps({'code':1,'errmsg':'idc name is exist'})

@app.route('/idc_update_msg')
def idc_update_msg():
    id = request.args.get('id')
    idc = idcdb.idclist(id)
    return json.dumps({'code':0,'result':idc})

@app.route('/idc_update',methods=['GET','POST'])
def idc_update():
    if not session.get('name'):
	return redirect('/login')
    data = dict((k,v[0]) for k,v in dict(request.form).items())
    if not data['idc_supplier']:
	return json.dumps({'code':1,'errmsg':'idc supplier name can not be null'})
    elif not data['idc_address']:
	return json.dumps({'code':1,'errmsg':'idc address can not be null'})
    elif not data['operation']:
	return json.dumps({'code':1,'errmsg':'operation can not be null'})
    conditions = [ "%s='%s'" %  (k,v) for k,v in data.items()]
    idcdb.update(conditions,data['id'])
    return json.dumps({'code':0,'result':'update completed!'})

@app.route('/idc_delete',methods=['POST'])
def idc_delete():
    if session.get('role') != 'admin':
	return redirect('/login')
    id = request.form.get('id')
    idcdb.delidc(id)
    return json.dumps({'code':0,'result':'delete success!'})

@app.route('/cabinet')
def cabinet():
    return render_template('cabinet.html')

@app.route('/server')
def server():
    return render_template('server.html')

@app.route('/logout/')
def loginout():
    if session:
	session.pop('role')
	session.pop('name')
	return redirect('/login')
    return redirect('/login')
    

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8888,debug=True)
