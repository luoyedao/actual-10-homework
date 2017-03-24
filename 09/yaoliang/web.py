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

@app.route('/user')
def user():
    name = session.get('name')
    return render_template('userlist.html',username = name)

@app.route('/userlist')
def userlist():
    if session.get('role')=='admin':
        users = db.userlist()
        return json.dumps({'code':0,'result':users,'name':session.get('name')})
    elif session.get('role')=='user': 
        user = db.userlist(session.get('name'))
        return json.dumps({'code':1,'result':user,'name':session.get('name')})
    else:
        return redirect('/')

#@app.route('/listone',methods=['POST'])
#def listone():
#    name = request.form.get('name')
#    return render_template('listone.html',user = db.userlist(name))

@app.route('/modpwd_msg')
def modpwd_msg():
    name = request.args.get('name')
    user = db.userlist(name)
    if session.get('role') == 'admin':
	return json.dumps({'code':0,'result':user})
    else:
	return json.dumps({'code':2,'result':user})

@app.route('/modpwd',methods=['GET','POST'])
def modpwd():
    if not session.get('name'):
	return redirect('/')
    if request.method=='GET':
	sesname = session.get('name')
	name = request.args.get('name')
	if not name:
	    name = sesname
	return render_template('modpwd.html',username = sesname,name = name)
    else:
	data = dict(request.form)
	if data['newpassword'][0] != data['renewpassword'][0]:
	    errmsg = 'The two passwords you entered do not match'
      	    return json.dumps({'code':'1','errmsg':errmsg})
	if not data['password'][0] or not data['newpassword'][0] or not data['renewpassword'][0]:
	    errmsg = 'password can not be null'
      	    return json.dumps({'code':'1','errmsg':errmsg})
	try:
            condition = [ "%s='%s'" %  ('password',v[0]) for k,v in data.items() if k == 'newpassword']
	    sesname = session.get('name')
	    print db.userlist(sesname)
	    if session.get('role') == 'admin':
                db.update(condition,data['id'][0])
        	return json.dumps({'code':'0','result':'modify completed!'})
 	    elif session.get('role') == 'user':
	        if data['password'][0] == db.userlist(sesname)['password']:
        	    return json.dumps({'code':'0','result':'modify completed!'})
        	return json.dumps({'code':'1','errmsg':'wrong old password'})
	    else:
	        return redirect('/')
	except:
            errmsg = "modify failed" 
	    return json.dumps({'code':'1','errmsg':errmsg})

@app.route('/delete')
def delete():
    if session.get('role') != 'admin':
	return redirect('/')
    name = request.args.get('name')
    db.deluser(name)
    return redirect('/user')


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
	return redirect('/')
    if request.method=='GET':
        sesname = session.get('name')
	name = request.args.get('name')
	if not name:
	    name = sesname
	return render_template('update.html',username = sesname,name = name)
    else:
	data = dict(request.form)
        conditions = [ "%s='%s'" %  (k,v[0]) for k,v in data.items()]
	if session.get('role') == 'admin':
	    if data['password'][0]:
        	db.update(conditions,data['id'][0])
                return json.dumps({'code':0,'result':'update completed!'})
            return json.dumps({'code':1,'errmsg':'password can not be null!'})
	elif session.get('role') == 'user':
            db.update(conditions,data['id'][0])
            return json.dumps({'code':0,'result':'update completed!'})
	else:
	    return redirect('/')

@app.route('/loginout')
def loginout():
    session.pop('role')
    session.pop('name')
    return render_template('login.html')

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8888,debug=True)
