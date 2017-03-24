#coding=UTF-8
from flask import Flask,request,render_template,redirect
from main import get_user,add_user,del_user

app = Flask(__name__)


@app.route('/')
def index():
	names=get_user()
	return render_template('index.html',names=names)

@app.route('/useradd')
def adduser():
	name = request.args.get('name')
	pwd = request.args.get('password')
	if name not in get_user():
		add_user(name,pwd)
	else:
	return redirect("/")
		
@app.route('/deluser')
def deluser():
	name=request.args.get('name')
	if name in get_user():
		del_user(name)
		return redirect("/")
	else:
		print "用户不存在" 

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=9092,debug=True)
