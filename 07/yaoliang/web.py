#!/usr/bin/python
#coding:utf-8

from flask import Flask,render_template,request
import db

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='GET':
        return render_template('login.html')
    else:
 	name = request.form.get('name')
 	password = request.form.get('password')

	d = {}
        for i in db.userlist():
	    d[i['name']] = i['password']
	if name=='admin' and d[name]==password:
	    return render_template('userlist.html',users = db.userlist())
	elif name in d and d[name]==password:
	    return render_template('userone.html',user = db.userlist(name))
	else:
	    return render_template('error.html')

@app.route('/listone',methods=['POST'])
def listone():
    name = request.form.get('name')
    return render_template('listone.html',user = db.userlist(name))

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='GET':
	return render_template('register.html')
    else:
	data = dict(request.form)
	repassword = data.pop('repassword')
        conditions = [ "%s='%s'" %  (k,v[0]) for k,v in data.items()]

	if data['password'][0]!=repassword[0]:
	    errmsg = 'The two passwords you typed do not match'
	    return render_template('register.html',result = errmsg)
        try:
            db.register(conditions)
            return render_template('register_ok.html')
	except:
            errmsg = "insert failed" 
            return render_template("register.html",result=errmsg)

@app.route('/modify_pwd',methods=['GET','POST'])
def modify_pwd():
    if request.method == 'GET':
        id = request.args.get('id')
	return render_template('modify_pwd.html',user = db.update_list(id))
    else:
	data = dict(request.form)
	
	if data['newpassword'][0] != data['renewpassword'][0]:
	    errmsg = 'The two passwords you typed do not match'
	    return render_template('modify_pwd.html',result = errmsg)
	try:    
            condition = [ "%s='%s'" %  ('password',v[0]) for k,v in data.items() if k == 'newpassword']
            db.update(condition,data['id'][0])
	    return render_template('userone.html',user = db.update_list(data['id'][0]))
	except:
            errmsg = "modify failed" 
	    return render_template('modify_pwd.html',result = errmsg)

@app.route('/modify_pwd_all',methods=['GET','POST'])
def modify_pwd_all():
    if request.method == 'GET':
        id = request.args.get('id')
	return render_template('modify_pwd_all.html',user = db.update_list(id))
    else:
	data = dict(request.form)
	
	if data['newpassword'][0] != data['renewpassword'][0]:
	    errmsg = 'The two passwords you typed do not match'
	    return render_template('modify_pwd_all.html',result = errmsg)
	try:    
            condition = [ "%s='%s'" %  ('password',v[0]) for k,v in data.items() if k == 'newpassword']
            db.update(condition,data['id'][0])
	    return render_template('userlist.html',users = db.userlist())
	except:
            errmsg = "modify failed" 
	    return render_template('modify_pwd_all.html',result = errmsg)

@app.route('/delete')
def delete():
    id = request.args.get('id')
    db.deluser(id)
    return render_template('userlist.html',users = db.userlist())


@app.route('/updateone',methods=['GET','POST'])
def updateone():
    if request.method=='GET':
        id = request.args.get('id')
	return render_template('updateone.html',user = db.update_list(id))
    else:
	data = dict(request.form)
        conditions = [ "%s='%s'" %  (k,v[0]) for k,v in data.items()]
        db.update(conditions,data['id'][0])

	return render_template('userone.html',user = db.update_list(data['id'][0]))

@app.route('/update',methods=['GET','POST'])
def update():
    if request.method=='GET':
        id = request.args.get('id')
	return render_template('update.html',user = db.update_list(id))
    else:
	data = dict(request.form)
        conditions = [ "%s='%s'" %  (k,v[0]) for k,v in data.items()]
        db.update(conditions,data['id'][0])

        return render_template('userlist.html',users = db.userlist())

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8888,debug=True)
