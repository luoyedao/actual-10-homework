# coding=utf8
from flask import Flask, redirect, request, render_template, session, jsonify
import mysql_info as mysql
import sys, os

reload(sys)
sys.setdefaultencoding('utf8')

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        d = dict((k, v[0]) for k, v in dict(request.form).iteritems())
        if mysql.check_users(d['username'], d['password']) == 0:
            session['username'] = d['username']
            session['role'] = mysql.get_one('role', 'name', d['username'])[0]

            if session['role'] == '1':
                mysql.insert_time(d['username'])
                return jsonify({'code': 0, 'result': 'login sucess'})
            else:
                mysql.insert_time(d['username'])
                return jsonify({'code': 0, 'result': 'login sucess'})
        else:
            return jsonify({'code': 1, 'errmsg': '用户名或密码错误'})
    else:
        return render_template('login.html')


@app.route('/index')
def index():
    if not session.get('username'):
        return redirect('/login')
    sess = dict(session)
    return render_template('index.html', sess=sess)


@app.route('/userlist/add', methods=['GET', 'POST'])
def add():
    if not session.get('username'):
        return redirect('/login')
    sess = dict(session)
    if request.method == 'POST':
        d_user = dict(request.form)
        d = {k: v[0] for k, v in d_user.iteritems()}
        if d['name'] == '' or d['password'] == '' or d['re_password'] == '' or d['email'] == '' or d['mobile'] == '':
            return jsonify({'code': 3, 'errmsg': '不能为空'})
        user_list = mysql.users_all()
        for user in user_list:
            if d['name'] in user['name']:
                return jsonify({'code': 2, 'errmsg': '用户已存在'})
        if d['password'] != d['re_password']:
            return jsonify({'code': 1, 'errmsg': '两次密码不相同'})
        else:
            mysql.insert_user(d)
            return jsonify({'code': 0, 'result': '添加用户成功'})
    else:
        return jsonify({'sess': sess})
        # return render_template('add.html', sess=sess)


@app.route('/userlist', methods=['GET', 'POST'])
def userlist():
    if not session.get('username'):
        return redirect('/login')
    sess = dict(session)
    if sess['role'] != '1' and sess['username']:
        users = mysql.user_one(sess['username'])
        return render_template('userlist.html', users=users, sess=sess)
    else:
        users = mysql.users_all()
        return render_template('userlist.html', users=users, sess=sess)


@app.route('/userlist/userup', methods=['GET', 'POST'])
def update():
    if not session.get('username'):
        return redirect('/login')
    sess = dict(session)
    ids = int(request.args.get('id'))
    users = mysql.upuser_dict(ids)
    if request.method == 'POST':
        d_user = {k: v[0] for k, v in dict(request.form).iteritems()}
        mysql.up_user(d_user, ids)
        return jsonify({'code': 0, 'result': '修改完成'})
    else:
        return jsonify({'users': users, 'sess': sess})


@app.route('/userlist/userdel', methods=['GET'])
def deleted():
    ids = int(request.args.get('id'))
    if ids:
        mysql.del_user(ids)
        return jsonify({'code': 0})
    else:
        return jsonify({'code': 1})
        # return redirect('/userlist')


@app.route('/userlist/upasswd', methods=['GET', 'POST'])
def upasswd():
    if not session.get('username'):
        return redirect('/login')
    ids = request.args.get('id')
    print ids
    if request.method == 'POST':
        d_pass = dict(request.form)
        if request.form.get('password')[0] == request.form.get('re_password')[0]:
            mysql.up_passwd(d_pass, ids)
            return jsonify({'code': 0, 'result': 'succe'})
        else:
            return jsonify({'code': 1, 'result': 'fail'})
    else:
        return jsonify({'ok': 'ko'})


@app.route('/logout')
def logout():
    if not session.get('username'):
        return redirect('/login')
    session.clear()
    return redirect('/login')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
