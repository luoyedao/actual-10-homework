#coding: utf-8
from datetime import datetime
from flask import Flask, render_template, redirect, request
import db

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/login/')


@app.route('/login/')
def login():
    return render_template('login.html')


@app.route('/login_required/', methods=['POST','GET'])
def login_required():
    username = request.form.get('username')
    password = request.form.get('password')
    if db.auth_user(username, password):
        return redirect('/users/')
    return redirect('/login/')


@app.route('/users/')
def user_list():
    user_list = db.user_list()
    return render_template('users.html', users=user_list)


@app.route('/users/regedit/')
def user_regedit():
    return render_template('user_create.html')


@app.route('/users/add/', methods=['POST','GET'])
def users_add():
    params = request.form
    username = params.get('username')
    password = params.get('password')
    name_cn = params.get('name_cn')
    email = params.get('email')
    mobile = params.get('mobile')
    role = params.get('role')
    status = params.get('status')
    create_time = datetime.now()
    last_time = datetime.now()
    if db.user_regedit_check(username,password,name_cn,email,mobile,role,status,create_time,last_time):
        if db.user_add(username,password,name_cn,email,mobile,role,status,create_time,last_time):
            return redirect('/users')
    return redirect('/users/regedit/')


@app.route('/users/modify/', methods=['GET'])
def users_modify():
    id = request.args.get('id')
    user = db.get_user_by_id(id)
    return render_template('user_modify.html', user=user)


@app.route('/users/update/', methods=['GET', 'POST'])
def users_update():
    params = request.form
    password = params.get('password')
    name_cn = params.get('name_cn')
    email = params.get('email')
    mobile = params.get('mobile')
    role = params.get('role')
    status = params.get('status')
    db.user_update(password,name_cn,email,mobile,role,status)
    return redirect('/users/')

@app.route('/users/delete/', methods=['GET'])
def users_delete():
    id = request.args.get('id')
    if db.user_del(id):
        return redirect('/users/')
    return 'del user failed!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)