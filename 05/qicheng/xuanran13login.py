#!/bin/env python
#encoding:utf-8

from flask import Flask,request,render_template,redirect,session
import util

app = Flask(__name__)
util.update_data()
app.secret_key='asjkdhk1241231fdsa781238fdsafad81329??=-123'

@app.route('/login')
def login():
	if 'user' in session:
		return redirect('/')
	else:
		return render_template('login.html')

@app.route('/loginaction',methods=['post'])
def loginaction():
	user = request.form.get('user')
	pwd = request.form.get('pwd')
	if user=='admin' and pwd=='admin':
		session['user'] = 'admin'
		return redirect('/')
	else:
		return 'not allowed'


@app.route('/logout')
def logout():
	session.pop('user')
	return redirect('/login')

@app.route('/')
def index():
	if 'user' in session:
		return render_template("13login.html",userlist=util.file_data.items())
	else:
		return redirect('/login')

@app.route('/adduser',methods=['post'])
def adduser():
	user = request.form.get('user')
	pwd = request.form.get('pwd')
	print '%s:%s'%(user,pwd)
	if user in util.file_data:
		return 'user %s already exists'%(user)
	else:
		util.file_data[user] = pwd
		util.update_file()
		return redirect('/')

@app.route('/deluser')
def deluser():
	user = request.args.get('user')
	print user
	print util.file_data
	if user in util.file_data:
		util.file_data.pop(user)
		util.update_file()
		return redirect('/')
	else:
		return 'user %s not exists'%(user)

if __name__=='__main__':
	app.run(host='0.0.0.0',port=9094,debug=True)