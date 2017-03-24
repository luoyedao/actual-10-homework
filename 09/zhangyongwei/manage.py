#coding: utf-8
from datetime import datetime
import time
from flask import Flask, render_template, redirect, request, session
import db
import json
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')

app = Flask(__name__)
app.secret_key=os.urandom(32)

@app.route('/')
def index():
    return redirect('/login/')

@app.route('/logout/')
def logout():
    session.clear()
    return redirect('/')


@app.route('/login/', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if db.auth_user(username, password):
            session['username'] = username
            return redirect('/users/')
        return render_template('login.html', errormsg='Account or passowrd error!')
    return render_template('login.html')


@app.route('/users/')
def user_list():
    user_list = db.user_list()
    user_login = {'user':session.get('username')}
    return render_template('users.html', users=user_list, session = user_login)

@app.route('/users/regedit/')
def user_regedit():
    return render_template('user_create.html')


@app.route('/users/change_pass/', methods=['POST', 'GET'])
def change_pass():
    if request.method == 'GET':
        name = request.args.get('name')
        return render_template('change_pass.html', name=name, session={'user': session.get('username')})
    else:
        login_name = session.get('username')
        name = request.form.get('name')
        old_pass = request.form.get('old_pass')
        new_pass = request.form.get('new_pass')
        status = db.change_pass(login_name, name, old_pass, new_pass)
        if status == "1":
            return redirect('/users/')
        else:
            return render_template('change_pass.html', name=name, status=status)


@app.route('/users/add/', methods=['POST','GET'])
def users_add():
    user_data = request.form.to_dict()
    user_data['create_time'] = datetime.now()
    user_data['last_time'] = datetime.now()
    error = db.user_regedit_check(user_data)
    if error['status'] == 0:
        db.user_add(user_data)
    return json.dumps(error)


@app.route('/users/update/', methods=['GET', 'POST'])
def users_update():
    if request.method == 'POST':
        user_data = request.form.to_dict()
        db.user_update(user_data)
        return json.dumps({"status":0, "msg":"update success!"})
        # return redirect('/users/')
    id = request.args.get('id')
    user = db.get_user_by_id(id)
    return render_template('user_modify.html', user=user, session={'user': session.get('username')})


@app.route('/users/delete/', methods=['GET'])
def users_delete():
    id = request.args.get('id')
    if db.user_del(id):
        return redirect('/users/')
    return 'del user failed!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)