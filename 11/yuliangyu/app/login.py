from flask import Flask,request,render_template,session,redirect
from . import app
import traceback
import json 
import db
import hashlib

#app.secret_key = 'sldkfjljl'
salt = "aaaaa"

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        data = dict((k,v[0]) for k,v in dict(request.form).items())
        if not data.get('name',None) or not data.get('password',None):
	    return json.dumps({'code':1,'errmsg':'name or password empty'})
        fields = ['name','password','role']
        condition = 'name = "%(name)s"' % data
        res = db.selectOne(fields,condition)
        if not res:
	    return json.dumps({'code':1,'result':'name not exist'})
        user = dict((k,res[i]) for i,k in enumerate(fields))
	data['password'] = hashlib.md5(data['password']+salt).hexdigest()
	print data['password']
	print user['password']
        if data['password'] != user['password']:
	    return json.dumps({'code':1, 'result':'password error'})

        session['name'] = user['name']
        session['role'] = user['role']

	return json.dumps({'code':0, 'result':'login success'})
    else:
        return render_template('login.html')

@app.route('/logout', methods=['GET'])
def logout():
    session.pop('name')
    session.pop('role')
    return redirect('/login')
