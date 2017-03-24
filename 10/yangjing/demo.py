# coding:utf-8
from flask import Flask, request, redirect, render_template, session
from db import *
import json

app = Flask(__name__)
app.secret_key = '12312321321'


@app.route('/login', methods=('GET', 'POST'))
def login():
	if request.method == "GET":
		return render_template("login.html")
	if request.method == "POST":
		login_info = dict((k, v[0]) for k, v in dict(request.form).items())
		print login_info
		if not checkuser({"name": login_info["name"]}, "name"):
			return json.dumps({"tag": 1, "errmsg": "user is not exist"})
		if login_info["password"] != checkuser({'name': login_info["name"]})[0]:
			return json.dumps({"code": 1, "errmsg": "password error"})
		u_role = checkuser({"name": login_info["name"]}, "role")
		session["username"] = login_info["name"]
		session["role"] = u_role
		return json.dumps({"code": 0})


@app.route('/userlist/', methods=('GET', 'POST'))
def user_list():
	if request.method == 'GET':
		if not session.get('username', None):
			return redirect('/login')
		fields = ["id", "name", "name_cn", "mobile", "email", "role", "status"]
		data = userlist(fields)
		return render_template("userlist.html", users=data)


@app.route("/add", methods=["GET", "POST"])
def add_user():
	if not session.get('username', None):
		return redirect('/login')
	if request.method == 'GET':
		return render_template('add.html', info=session)
	if request.method == 'POST':
		data = dict((k, v[0]) for k, v in (dict(request.form)).items())
		if data['name'] in checkuser({'name': data['name']}, 'name'):
			return json.dumps({"code": 1, "errmsg": "username is exist"})
		adduser(data)
		return json.dumps({"code": 0, "result": "add user success"})


@app.route('/delete')
def del_user():
	if not session.get('username', None):
		return redirect('/login')
	uid = request.args.get('id')
	delete(uid)
	return json({"code": 0, "result": "delete user success"})


@app.route('/logout/')
def logout():
	if session.get('username'):
		session.pop('username', None)
		session.pop('role', None)
		session.pop('status', None)
	return redirect('/login')


@app.route('/')
@app.route('/index')
def index():
	if session.get('username'):
		return render_template('index.html')
	else:
		return redirect('/login')


@app.route('/userinfo/', methods=["GET", "POST"])
def info_user():
	if not session.get('username', None):
		return redirect('/login')
	if request.method == "GET":
		uid = request.args.get("id")
		userinfo = getone(uid)
		print userinfo
	# return json.dumps(userinfo)
	return render_template("update.html", user=userinfo)


@app.route('/modify/', methods=["GET", "POST"])
def modify_user():
	if not session.get('username', None):
		return redirect('/login')
	if request.method == "GET":
		uid = request.args.get("id")
		info = getone(uid)
		return json.dumps(info)
	if request.method == "POST":
		info = {k: v[0] for k, v in dict(request.form).iteritems()}
		print info
		modfiy(info)
		return redirect('/userlist/')







@app.route('/test/')
def test():
	return render_template("json.html")


# @app.route('/userlist/')
# def user_list():
# 	return render_template('userlist.html')
#
#
# @app.route('/idc')
# def idc():
# 	return render_template('idc.html')
#
#
# @app.route('/rack')
# def cabinet():
# 	return render_template('rack.html')
#
#
# @app.route('/server')
# def server():
# 	return render_template('server.html')


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)
