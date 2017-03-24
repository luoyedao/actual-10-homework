#!/usr/local/python/bin/python
#encoding
from flask import Flask,request,render_template,redirect
app = Flask(__name__)

def open_file(file_name):
    with open(file_name,'a+') as f:
        passwd = {}
        for line in f.readlines():
            tmp = line.rstrip('\n').split(":")
            passwd[tmp[0]] = tmp[1]
    return passwd
pwd=open_file('user.txt')

def write_file(passwd):
    with open('user.txt','w') as ff:
        for username,password in pwd.items():
            ff.write('%s:%s\n'%(username,password))
    return open_file('user.txt')

@app.route('/')
def index():
    return render_template('index.html',pwd=pwd)
@app.route('/choice')
def choice():
    action = request.args.get('choice')
    if action == 'login':
        return redirect('/login')
    elif action == 'register':
        return redirect('/register')
    elif action == 'deluser':
        return redirect('/deluser')
    else:
        return 'input failed , please try again'

@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/login_process')
def login_process():
    username = str(request.args.get('username'))
    password = str(request.args.get('password'))
    if pwd.has_key(username) == True:
        if str(password) == str(pwd[username]): 
            return 'login success!!!'
        else:
            return 'password failed!!!'
    else:
        return 'No such user'

@app.route('/register')
def register():
    return render_template('register.html')
@app.route('/register_process')
def register_process():
    username = str(request.args.get('username'))
    password = str(request.args.get('password'))
    if pwd.has_key(username) == True:
        return 'username exist, please reinput'
    else:
        pwd.setdefault(username,password)
        write_file(pwd)
        return  render_template('user.html',pwd=pwd)

@app.route('/deluser')
def deluser():
    return render_template('deluser.html')
@app.route('/deluser_process')
def deluser_process():
    username = str(request.args.get('username'))
    password = str(request.args.get('password'))
    if pwd.has_key(username) == True:
        if str(password) == str(pwd[username]):
            del pwd[username]
            write_file(pwd)
            return  render_template('user.html',pwd=pwd)
        else:
            return 'password error, please input again!'
    else:
        return 'username not exist, pleae input again!'

if __name__ =='__main__':
    app.run(host='0.0.0.0',port=9099,debug=True)
