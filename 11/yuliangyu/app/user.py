from flask import Flask,request,render_template,session,redirect
from . import app
import traceback
import json 
import db
import hashlib

#app.secret_key = 'sldkfjljl'
salt = "aaaaa"

@app.route('/')
@app.route('/index')
def index():
    if not session.get('name',None):
	return redirect('/login')
    fields = ['id','name','name_cn','mobile','email','role','status']
    condition = 'name = "%(name)s"' % session
    print condition
    print session
    result = db.selectOne(fields,condition)
    print result
    user = dict((k,result[i]) for i,k in enumerate(fields))
    return  render_template('index.html', info = session, user = user)

@app.route('/userlist')
def userlist():
    if not session.get('name',None):
	return redirect('/login')
    fields = ['id','name','name_cn','mobile','email','role','status']
    table = 'users'
    result = db.selectAll(fields,table)
    data = [dict((k,row[i]) for i,k in enumerate(fields)) for row in result]
    return render_template('user/userlist.html',users=data,info=session)


@app.route('/add',methods=['GET','POST'])
def add_user():
    if not session.get('name',None):
        return redirect('/login')
    if session.get('role') != 'SU':
	return json.dumps({'code':0, 'result':'you are not admin, can not register user'})
    if request.method == 'POST':
        data = {}
        data = dict((k,v[0]) for k,v in dict(request.form).items())
	data['password'] = hashlib.md5(data['password']+salt).hexdigest()
        print data
        # data = request.get_json()
        fields = ['name','name_cn','password','mobile','email','role','status']
        if not data["name"]: 
	    return json.dumps({'code':1, 'result':'name not null'})
        try:
	    table = 'users'
            db.insert(fields,data,table)
	    return json.dumps({'code':0, 'result':'add user success'})
        except:
            print traceback.print_exc()
	    return json.dumps({'code':1, 'result':'name not null'})
    else:
        return render_template("user/adduser.html",info=session)

@app.route('/update', methods=['GET','POST'])
def update():
    table = 'users'
    if not session.get('name',None):
        return redirect('/login')
    if request.method == "POST":
        data = dict(request.form)
	data['password'][0] = hashlib.md5(data['password'][0]+salt).hexdigest()
	print data
        condition = [ "%s='%s'" % (k,v[0]) for k,v in data.items() ]
	print condition
        try:
            db.update(condition, data['id'][0], table)
	    return json.dumps({'code':0,'result':'update user success'})
        except:
            print traceback.print_exc()
	    return json.dumps({'code':1,'result':'update user failed'})
    else:
        id = request.args.get('id')
        fields = ['id', 'name', 'name_cn', 'email', 'mobile']
        try:
            res = db.selectId(fields,id,table)
            user = dict((k,res[i]) for i,k in enumerate(fields))
	    return json.dumps({'code':0, 'result':user})
        except:
            print traceback.print_exc()
	    return json.dumps({'code':1, 'result':'select userinfo failed'})

@app.route('/delete', methods=['GET'])
def delete():
    if not session.get('name',None):
        return redirect('/login')
    id = request.args.get('id')
    table = 'users'
    try:
        db.delete(id,table)
	return json.dumps({'code':0, 'result':'delete user success'})
    except:
        print traceback.print_exc()
	return json.dumps({'code':1, 'result':'delete user failed'})

@app.route('/chpwdoneself',methods=['POST'])
def chpwdoneself():
    if not session.get('name',None):
        return redirect('/login')
    if request.method == "POST":
        data = dict((k,v[0]) for k ,v in dict(request.form).items())
	fields = ['password']
	id = data['id']
        password = db.selectId(fields,id,'users')
        print data
        print password
        if data["oldpasswd"] != password[0]:
            return json.dumps({"code":1,"errmsg":"password is error"})
	try:
    	    db.updatepwd(data['newpasswd'],id)
	    return json.dumps({'code':0, 'result':'update password success'})
        except:
            print traceback.print_exc()
	    return json.dumps({'code':1, 'errmsg':'update password failed'})
    
