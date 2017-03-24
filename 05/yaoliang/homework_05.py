#!/usr/bin/python
#coding:utf-8

from flask import Flask,request,render_template,redirect
app=Flask(__name__)

def open_file(filename):
    with open(filename) as fo:
        d = {}
        for user in fo:
            user_name = user.strip('\n').split(':')[0]
            user_passwd = user.strip('\n').split(':')[1]
            d[user_name] = user_passwd
        return d

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index_exec')
def index_exec():
    func = request.args.get('function')

    if func=='register':
        return redirect('/useradd')
    elif func=='login':    
        return redirect('/login')
    else:
	return 'choose one from login or register'

@app.route('/useradd')
def useradd():
    return render_template('register.html')

@app.route('/useradd_exec')
def useradd_exec():
    name = request.args.get('name')
    passwd = request.args.get('password')

    d = open_file('user.txt')

    if name and passwd and name not in d.keys():
        with open('user.txt','a+') as fo:
            fo.write('%s:%s\n'%(name,passwd))
        return 'registration completed'
    else:
        return 'Something Wrong'

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login_exec')
def login_exec():
    name = request.args.get('name')
    passwd = request.args.get('password')

    d = open_file('user.txt')

    if name not in d.keys():
	return 'no such user'
    elif name=='admin' and d[name]==passwd:
	return redirect('/admin')
    elif name!='admin' and d[name]==passwd:
	return 'login successfully'
    else:
	return 'username or password wrong'

@app.route('/admin')
def admin():
    names = open_file('user.txt')
    return render_template('user.html',names=names)

@app.route('/delete')
def delete():
    names = open_file('user.txt')
    user = request.args.get('user')
    names.pop(user)
    with open('user.txt','w') as fo:
        for i in names.keys():
            fo.write('%s:%s\n'%(i,names[i]))

    return render_template('user.html',names=names)

if __name__=='__main__':
    app.run(host='0.0.0.0',port='8888')

