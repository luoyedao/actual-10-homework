# coding=utf8
from flask import Flask, redirect, request, render_template, session, jsonify
import mysql_info as mysql
import sys, os

reload(sys)
sys.setdefaultencoding('utf8')

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route('/login', methods=['GET', 'POST'])
def login():
    all_error = 'Account or password error'
    if request.method == 'POST':
        d = dict((k, v[0]) for k, v in dict(request.form).iteritems())
        if mysql.check_users(d['username'], d['password']) == 0:
            session['username'] = d['username']
            session['role'] = mysql.get_one('role', 'name', d['username'])[0]
            if session['role'] == '1':
                mysql.insert_time(d['username'])
                return jsonify({'code': 'OK'})
            else:
                mysql.insert_time(d['username'])
                return jsonify({'code': 200})
        else:
            return jsonify({'code': 'error'})
    else:
        return render_template('login.html')


@app.route('/add', methods=['GET', 'POST'])
def add():
    if not session.get('username'):
        return redirect('/login')
    error = 'Account already exists'
    error1 = 'passwd error'
    error2 = 'User name and Chinese name can not be the same'
    if request.method == 'POST':
        d_user = dict(request.form)
        d = {k: v[0] for k, v in d_user.iteritems()}
        user_list = mysql.users_all()
        for user in user_list:
            if d['name'] in user['name']:
                return render_template('add.html', error=error)
        if d['password'] != d['re_password']:
            return render_template('add.html', error=error1)
        elif d['name'] == d['name_cn']:
            return render_template('add.html', error=error2)
        else:
            mysql.insert_user(d)
            return redirect('/userlist')
    else:
        return render_template('add.html')


@app.route('/userlist', methods=['GET', 'POST'])
def userlist():
    if not session.get('username'):
        return redirect('/login')
    sess = dict(session)
    if request.method == 'POST':
            sel = request.form['cats']
            users = mysql.get_all(sel,sess['role'])
            return render_template('userlist.html', users=users, sess=sess)
    else:
        if sess['role'] != '1' and sess['username']:
            users = mysql.user_one(sess['username'])
            return render_template('userlist.html', users=users, sess=sess)
        else:
            users = mysql.users_all()
            return render_template('userlist.html', users=users, sess=sess)


@app.route('/update', methods=['GET', 'POST'])
def update():
    if not session.get('username'):
        return redirect('/login')
    sess = dict(session)
    ids = int(request.args.get('id'))
    users = mysql.upuser_dict(ids)
    print users
    if request.method == 'POST':
        d_user = {k: v[0] for k, v in dict(request.form).iteritems()}
        print d_user
        mysql.up_user(d_user, ids)
        return redirect('/userlist')
    else:
        return render_template('update.html', users=users, sess=sess)


@app.route('/delete', methods=['GET', 'POST'])
def deleted():
    ids = int(request.args.get('id'))
    if ids:
        mysql.del_user(ids)
        return redirect('/userlist')
    else:
        return redirect('/userlist')


@app.route('/upasswd', methods=['GET', 'POST'])
def upasswd():
    if not session.get('username'):
        return redirect('/login')

    ids = request.args.get('id')
    if request.method == 'POST':
        d_pass = dict(request.form)
        if request.form.get('password') == request.form.get('re_password'):
            mysql.up_passwd(d_pass, ids)
            return redirect('/userlist?name=%s' % (mysql.get_one('name', 'id', ids)))
    else:
        return render_template('up_passwd.html')


@app.route('/logout')
def logout():
    if not session.get('username'):
        return redirect('/login')
    session.clear()
    return redirect('/login')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
