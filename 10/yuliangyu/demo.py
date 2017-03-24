from flask import Flask,request,render_template,session,redirect
import traceback
import json 
from db import *
import user_db

app = Flask(__name__)

app.secret_key = 'sldkfjljl'

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        data = dict((k,v[0]) for k,v in dict(request.form).items())
        if not data.get('name',None) or not data.get('password',None):
	    return json.dumps({'code':1,'errmsg':'password error'})
        fields = ['name','password','role']
        condition = 'name = "%(name)s"' % data
        res = user_db.selectOne(fields,condition)
        if not res:
	    return json.dumps({'code':1,'result':'name not exist'})
        user = dict((k,res[i]) for i,k in enumerate(fields))
        if data['password'] != user['password']:
	    return json.dumps({'code':1, 'result':'password error'})

        session['name'] = user['name']
        session['role'] = user['role']

	return json.dumps({'code':0, 'result':'login success'})
    else:
        return render_template('login.html')


@app.route('/')
@app.route('/index')
def index():
    if not session.get('name',None):
	return redirect('/login')
    return  render_template('index.html')

@app.route('/userlist')
def userlist():
    if not session.get('name',None):
	return redirect('/login')
    fields = ['id','name','name_cn','mobile','email','role','status']
    table = 'users'
    result = user_db.selectAll(fields,table)
    data = [dict((k,row[i]) for i,k in enumerate(fields)) for row in result]
    return render_template('userlist.html',users=data,info=session)

#@app.route('/add',methods=['GET','POST'])
#def add_user():
#    if not session.get('name',None):
#	return redirect('/login')
#    if request.method == 'GET':
#	return render_template('add.html',info=session)
#    if request.method == 'POST':
#	data = dict((k,v[0]) for k,v in dict(request.form).items())
#	if data['name'] in checkuser({'name':data['name']},'name'):
#	    return json.dumps({'code':1,'errmsg':'username is exist'})
#	adduser(data)
#	return json.dumps({'code':0,'result':'add user success'})

@app.route('/add',methods=['GET','POST'])
def add_user():
    if not session.get('name',None):
        return redirect('/login')
    if session.get('role') != 'admin':
	return json.dumps({'code':0, 'result':'you are not admin, can not register user'})
    if request.method == 'POST':
        data = {}
        data = dict((k,v[0]) for k,v in dict(request.form).items())
        print data
        # data = request.get_json()
        fields = ['name','name_cn','mobile','email','role','status']
        if not data["name"]: 
	    return json.dumps({'code':1, 'result':'name not null'})
        try:
	    table = 'users'
            user_db.insert(fields,data,table)
	    return json.dumps({'code':0, 'result':'add user success'})
        except:
            print traceback.print_exc()
	    return json.dumps({'code':1, 'result':'name not null'})
    else:
        return render_template("add.html",info=session)

@app.route('/update', methods=['GET','POST'])
def update():
    table = 'users'
    if not session.get('name',None):
        return redirect('/login')
    if request.method == "POST":
        data = dict(request.form)
	print data
        condition = [ "%s='%s'" % (k,v[0]) for k,v in data.items() ]
        try:
            user_db.update(condition, data['id'][0], table)
	    return json.dumps({'code':0,'result':'update user success'})
        except:
            print traceback.print_exc()
	    return json.dumps({'code':1,'result':'update user failed'})
    else:
        id = request.args.get('id')
        fields = ['id', 'name', 'name_cn', 'email', 'mobile']
        try:
            res = user_db.selectId(fields,id,table)
            user = dict((k,res[i]) for i,k in enumerate(fields))
	    return json.dumps({'code':0, 'result':user})
        except:
            print traceback.print_exc()
	    return json.dumps({'code':1, 'result':'select userinfo failed'})

@app.route('/delete', methods=['GET'])
def delete():
    if not session.get('username',None):
        return redirect('/login')
    id = request.args.get('id')
    table = 'users'
    try:
        user_db.delete(id,table)
	return json.dumps({'code':0, 'result':'delete user success'})
    except:
        print traceback.print_exc()
	return json.dumps({'code':1, 'result':'delete user failed'})

@app.route('/logout', methods=['GET'])
def logout():
    session.pop('name')
    session.pop('role')
    return redirect('/login')

    
@app.route('/idc')
def idc():
    if not session.get('name',None):
	return redirect('/login')
    fields = ['id','name','isp','contact','mobile','address']
    table = 'idc'
    result = user_db.selectAll(fields,table)
    data = [dict((k,row[i]) for i,k in enumerate(fields)) for row in result]
    return render_template('idc.html',idcs=data,info=session)

@app.route('/addidc',methods=['GET','POST'])
def addidc():
    if not session.get('name',None):
        return redirect('/login')
#    if session.get('role') != 'admin':
#        errmsg = "you are not admin, can not register idc"
#	return json.dumps({'code':1,'errmsg':'you are not admin, can not add idc'})
    if request.method == 'POST':
        data = {}
        data = dict((k,v[0]) for k,v in dict(request.form).items())
        print data
        # data = request.get_json()
        fields = ['name','isp','contact','mobile','address']
	table = 'idc'
        if not data["name"]:
            errmsg = "name null"
            return render_template("idc.html", result=errmsg)
        try:
            user_db.insert(fields,data,table)
	    return json.dumps({'code':0,'result':'add idc success'})
        except:
            print traceback.print_exc()
	    return json.dumps({'code':1,'errmsg':'add idc error'})
    else:
        return render_template("addidc.html")

@app.route('/delidc',methods=['GET'])
def delidc():
#    if not session.get('username',None):
#        return redirect('/login')
    id = request.args.get('id')
    print id
    table = 'idc'
    try:
        user_db.delete(id,table)
	return json.dumps({'code':0, 'result':'delete idc success'})
    except:
        print traceback.print_exc()
	return json.dumps({'code':1, 'result':'delete idc failed'})
    

@app.route('/updateidc', methods=['GET','POST'])
def updateidc():
    table = 'idc'
    if not session.get('name',None):
        return redirect('/login')
    if request.method == "POST":
        data = dict(request.form)
	print data
	print data['id'][0]
        condition = [ "%s='%s'" % (k,v[0]) for k,v in data.items() ]
	print condition
        try:
            user_db.update(condition, data['id'][0], table)
	    return json.dumps({'code':0,'result':'update idc success'})
        except:
            print traceback.print_exc()
	    return json.dumps({'code':1,'result':'update idc failed'})
    else:
        id = request.args.get('id')
        fields = ['id','name','isp','contact','mobile','address']
        try:
            res = user_db.selectId(fields,id,table)
            idc = dict((k,res[i]) for i,k in enumerate(fields))
	    print idc
	    return json.dumps({'code':0, 'result':idc})
        except:
            print traceback.print_exc()
	    return json.dumps({'code':1, 'result':'select idcinfo failed'})

@app.route('/server')
def server():
    
    return render_template('server.html')
    
'''
@app.route('/userlist')
def userlist():
    return  render_template('userlist.html')

@app.route('/idc')
def idc():
    return  render_template('idc.html')

@app.route('/cabinet')
def cabinet():
    return  render_template('cabinet.html')

@app.route('/server')
def server():
    return  render_template('server.html')
'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090,debug=True)
