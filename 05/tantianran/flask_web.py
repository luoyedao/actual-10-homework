#!/usr/bin/env python
#coding: UTF-8
from flask import Flask,render_template,request,redirect
app = Flask(__name__)

@app.route('/')
def index():
    def psw():
        f = open('userpassword.txt')
        passwd = {}
        for i in f.readlines():
            tmp = i.split(':')
            passwd[tmp[0]] = tmp[1]
        f.close()
        return passwd
    username = request.args.get('login_name')
    password = request.args.get('login_pwd')
    if psw().has_key(username) == True:
        paw = psw()[username]
	if password in paw:
	    return render_template('login_complete.html')
        else:
	    return render_template('index.html',login_error = 'Password mistake')
    return render_template('index.html')
    

@app.route('/reg')
def reg():
    def psw():
        f = open('userpassword.txt')
        passwd = {}
        for i in f.readlines():
            tmp = i.split(':')
            passwd[tmp[0]] = tmp[1]
        f.close()
        return passwd
    user = request.args.get('reg_name')
    if psw().has_key(user) == True:
        return render_template('reg.html', reg_error = 'Sorry User name already exists.')
    passwd = request.args.get('reg_pwd')
    psw = request.args.get('confirm_pwd')
    if passwd != psw:
	return render_template('reg.html', reg_error = 'Sorry Passwords don\'t match, please try again')
    else:
        f = open('userpassword.txt','a+')
        f.write('%s:%s\n' % (user,passwd))
        f.close()
        return render_template('reg.html')

@app.route('/admin')
def admin():
    f = open('userpassword.txt')
    query_pws = {}
    for val in f.readlines():
        tmp = val.split(':')
        query_pws[tmp[0]] = tmp[1]
    name1 = request.args.get('query_name')
    pwd = query_pws.get(name1,None)
    usr = name1
    return render_template('admin.html',passwd = query_pws, pwd_data=pwd,user_data=usr)
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'),500
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081,debug=True)
