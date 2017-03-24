#!/usr/bin/python
#coding:utf-8

from flask import Flask,render_template,request,redirect,session
import json
import db

app = Flask(__name__)
app.secret_key='\xd1\xfe\xfb\x7fH\xbf\xc8Q\x17-\xab\xc6\x80u2\xc2\xb6\n9\x00\x87\xa7\xa75'

@app.route('/',methods=['GET','POST'])
def index():
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

@app.route('/userlist')
def userlist():
    if session.get('role')=='admin':
	return render_template('userlist.html',users = db.userlist(),username = session.get('name'))
    elif session.get('role')=='user':
	return render_template('userone.html',user = db.userlist(session.get('name')),username = session.get('name'))
    else:
        return redirect('/')

@app.route('/listone',methods=['POST'])
def listone():
    name = request.form.get('name')
    return render_template('listone.html',user = db.userlist(name))

@app.route('/modify_pwd',methods=['GET','POST'])
def modify_pwd():
    if not session.get('name'):
	return redirect('/')
    if request.method == 'GET':
        id = request.args.get('id')
	return render_template('modify_pwd.html',user = db.update_list(id))
    else:
	data = dict(request.form)
	
	if data['newpassword'][0] != data['renewpassword'][0]:
	    errmsg = 'The two passwords you typed do not match'
      	    return json.dumps({'code':'1','errmsg':errmsg})
	if not data['password'][0] or not data['newpassword'][0] or not data['renewpassword'][0]:
	    errmsg = 'password can not be null'
      	    return json.dumps({'code':'1','errmsg':errmsg})
	try:
            condition = [ "%s='%s'" %  ('password',v[0]) for k,v in data.items() if k == 'newpassword']
            db.update(condition,data['id'][0])
	    if session.get('role'):
        	return json.dumps({'code':'0','result':'modify success!'})
	    else:
	        return redirect('/')
	except:
            errmsg = "modify failed" 
	    return json.dumps({'code':'1','errmsg':errmsg})

@app.route('/delete')
def delete():
    if session.get('role') != 'admin':
	return redirect('/')
    id = request.args.get('id')
    db.deluser(id)
    return render_template('userlist.html',users = db.userlist(),username = session.get('name'))

@app.route('/update',methods=['GET','POST'])
def update():
    if not session.get('name'):
	return redirect('/')
    if request.method=='GET':
        id = request.args.get('id')
	return render_template('update.html',user = db.update_list(id))
    else:
	data = dict(request.form)
        conditions = [ "%s='%s'" %  (k,v[0]) for k,v in data.items()]
	if session.get('role'):
            db.update(conditions,data['id'][0])
            return json.dumps({'code':'0','result':'modify success!'})
	else:
	    return redirect('/')

@app.route('/loginout')
def loginout():
    session.pop('role')
    session.pop('name')
    return render_template('login.html')

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8888,debug=True)
