#!/usr/bin/env python
# coding:utf-8

from flask import Flask,request,render_template,redirect
app = Flask(__name__)
from user_func import *


@app.route('/submit')
def submit():
    name = request.args.get('name')
    pwd = request.args.get('password')
    repwd = request.args.get('repassword')
    user_dict = get_user()
    if pwd == repwd and name not in user_dict.keys():
        return "Submit success"
        add_user(name,pwd)
    else:
        return "Submit failed"


@app.route('/login')
def login():
    name = request.args.get('name')
    pwd = request.args.get('password')
    check_value=check_user(name,pwd)
    if check_value == 0:
        return "Login sucess"
    else:
        return "Login Failed"


@app.route('/')
def main():
    user_info = get_user()
    return render_template('main_05.html')

if __name__ =='__main__':
    app.run(host='0.0.0.0',port=8888,debug=True)
