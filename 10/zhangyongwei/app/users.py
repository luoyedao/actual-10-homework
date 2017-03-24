#coding: utf-8
from datetime import datetime
import time
from flask import Flask, render_template, redirect, request, session
from . import app
import db
import json
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# app = Flask(__name__)
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
            session['role'] = db.get_user_role(username)
            return redirect('/user_center/')
        return render_template('login.html', errormsg='Account or passowrd error!')
    return render_template('login.html')


@app.route('/users/')
def user_list():
    user_list = db.user_list()
    return render_template('users.html', users=user_list)

@app.route('/user_center/')
def user_center():
    user = db.user_info(session.get('username'))
    return render_template('user_center.html', user=user)

@app.route('/users/regedit/')
def user_regedit():
    user_login = {'user':session.get('username')}
    return render_template('user_create.html', session = user_login)


@app.route('/users/chpwdadmin/', methods=['POST'])
def chpwdadmin():
    userinfo = request.form.to_dict()
    data = db.change_pass_admin(userinfo['username'],userinfo['newpasswd'])
    return json.dumps(data)

@app.route('/users/chpwdoneself/', methods=['POST'])
def chpwdoneself():
    userinfo = request.form.to_dict()
    data = db.change_pass(session['username'],userinfo['username'],userinfo['oldpasswd'],userinfo['newpasswd'])
    return json.dumps(data)


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
    if request.method == 'GET':
        id = request.args.get('id')
        user = db.get_user_by_id(id)
        user.pop('create_time')
        user.pop('last_time')
        return json.dumps(dict(user))
    else:
        userinfo = request.form.to_dict()
        data = db.user_update(userinfo['name'], userinfo)
        return json.dumps(data)


@app.route('/users/updateoneself/', methods=['GET', 'POST'])
def updateoneself():
    userinfo = request.form.to_dict()
    user_data = dict({'name_cn': userinfo['name_cn'], 'email':userinfo['email'], 'mobile': userinfo['mobile']})
    data = db.user_update_oneself(userinfo['name'], user_data)
    return json.dumps(data)


@app.route('/users/delete/', methods=['GET'])
def users_delete():
    id = request.args.get('id')
    if db.user_del(id):
        return redirect('/users/')
    return 'del user failed!'
#
#
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)