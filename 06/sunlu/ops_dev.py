# coding=utf8
from flask import Flask, redirect, request, render_template, sessions, jsonify
import mysql_info as mysql
import sys

reload(sys)
sys.setdefaultencoding('utf8')

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    all_error = 'Account or password error'
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if mysql.check_users(username, password) == 0:
            if mysql.get_one('role', 'name', username)[0] == '1':
                mysql.insert_time(username)
                return redirect('/userlist')
            else:
                mysql.insert_time(username)
                return redirect('/userlist?name=%s' % (username))
        else:
            return render_template('index.html', error=all_error)
    else:
        return render_template('index.html')


@app.route('/add', methods=['GET', 'POST'])
def add():
    error = 'Account already exists'
    error1 = 'passwd error'
    if request.method == 'POST':
        d_user = dict(request.form)
        d = {k: v[0] for k, v in d_user.iteritems()}
        user_list = mysql.users_all()
        for user in user_list:
            if d['name'] in user['name']:
                return render_template('add.html', error=error)
        if d['password'] != d['re_password']:
            return render_template('add.html', error=error1)
        else:
            if d['role'] == '1':
                mysql.insert_user(d)
                return redirect('/userlist')
            else:
                mysql.insert_user(d)
                return redirect('/userlist?name=%s' % (d['name']))
    else:
        return render_template('add.html')


@app.route('/userlist', methods=['GET', 'POST'])
def userlist():
    if request.method == 'POST':
        sel = request.form['cats']
        users = mysql.get_all(sel)
        return render_template('userlist.html', users=users)
    else:
        names = request.args.get('name')
        if names:
            users = mysql.user_one(names)
            return render_template('userlist.html', users=users)
        else:
            users = mysql.users_all()
            return render_template('userlist.html', users=users)


@app.route('/update', methods=['GET', 'POST'])
def update():
    ids = int(request.args.get('id'))
    users = mysql.upuser_dict(ids)
    if request.method == 'POST':
        d = dict(request.form)
        d_user = {k: v[0] for k, v in d.iteritems()}
        mysql.up_user(d_user, ids)
        return redirect('/userlist?id=%s' % (ids))
    else:
        return render_template('update.html', users=users)


@app.route('/delete', methods=['GET','POST'])
def deleted():
    ids = int(request.args.get('id'))
    if ids:
        mysql.del_user(ids)
        return redirect('/userlist')
    else:
        return redirect('/userlist')


@app.route('/upasswd', methods=['GET','POST'])
def upasswd():
    ids = request.args.get('id')
    if request.method == 'POST':
        d_pass = dict(request.form)
        if request.form.get('password') == request.form.get('re_password'):
            mysql.up_passwd(d_pass,ids)
            return redirect('/userlist?name=%s' % (mysql.get_one('name', 'id', ids)))
    else:
        return render_template('up_passwd.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8051, debug=True)
