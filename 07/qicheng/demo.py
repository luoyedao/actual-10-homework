#!/bin/env python
#encoding:utf-8

from flask import Flask,request,render_template,redirect
import MySQLdb as mysql
import json 
import time
import traceback
import db



conn=mysql.connect(user='root',host='127.0.0.1',passwd='123456',db='reboot10',charset='utf8')
conn.autocommit(True) 
cur = conn.cursor()


app = Flask(__name__) 



# '''打开用户登录页面
# '''
@app.route('/')                                     #将url path=/的请求交由index函数处理
def index():
    return render_template('login.html')            #加载login.html模板，并返回页面内容



'''用户登录信息检查
'''
@app.route('/login/', methods=['GET', 'POST'])            #将url path=/login/的post请求交由login函数处理
def login():
	if request.method == "POST":
		name = request.form.get('name')     #接收用户提交的数据
		password = request.form.get('password')
		print name and password
		if db.auth_user(name, password):
			return redirect('/userlist')
		return redirect('/login/')
	else:
		return render_template('login.html')


   #注册，添加用户，第一次请求获取注册页面，用get请求，点击表单提交用post方式，执行sql插入数据，注册成功。
   #则跳转到个人信息页面，失败则在注册的页面打印错误信息

@app.route('/register',methods=['GET','POST'])
def register():
	if request.method == 'POST':
		data = {}
		data["name"] = request.form.get('name',None)
		data["name_cn"] = request.form.get('name_cn',None)
		data["mobile"] = request.form.get('mobile',None)
		data["email"] = request.form.get('email',None)
		data["role"] = request.form.get('role',None)
		data["status"] = request.form.get('status',None)
		data["password"] = request.form.get('password',None)
		data["repwd"] = request.form.get('repwd',None)
		data["create_time"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
		print data
		fields = ['name','name_cn','mobile','email','role','status','password','create_time']
		#验证name 或者password或者role不能为空#
		if not data["name"] or not data["password"] or not data["role"]:
			errmsg = 'name or password or role not null'
			return render_template("register.html",result=errmsg)

		if data["password"] != data["repwd"]:
			errmsg = 'The two passwords you typed do not match'
			return render_template("register.html",result=errmsg)
		try:
			sql = 'insert into users(%s) values (%s)' % (','.join(fields), ','.join(['"%s"' % data[x] for x in fields]))
			print sql
			cur.execute(sql)
			return redirect('/userinfo?name=%s' % data['name'])
		except:
			errmsg = "insert failed"
			print traceback.print_exc()
			return render_template("register.html",result=errmsg)
	else:
		return render_template("register.html")

#用户列表，生产环境中只有管理员才有这个权限
@app.route('/userlist')
def userlist():
	users = []
	fields = ['id', 'name', 'name', 'name_cn', 'email', 'mobile']
	try:
		sql = "select %s from users" % ','.join(fields)
		cur.execute(sql)
		result = cur.fetchall()
		for row in result:
			user = {}
			for i, k in enumerate(fields):
				user[k] = row[i]
			users.append(user)
		return render_template('userlist.html', users = users)
	except:
		errmsg = "select userlist failed"
		print traceback.print_exc()
		return render_template("userlist.html",result=errmsg)

#先查询该条数据，渲染到html页面上#
@app.route('/update',methods=['GET','POST'])
def update():
	if request.method == "POST":
		print request.form
		data = dict(request.form)
		print data
		conditions = [ "%s='%s'" % (k,v[0]) for k,v in data.items()]
		sql = "update users set %s where id = %s" % (','.join(conditions),data['id'][0])
		print sql
		cur.execute(sql)
		return redirect('/userlist')
	else:
		id = request.args.get('id',None)
		if not id:
			errmsg = "must have id"
			return render_template("update.html",result=errmsg)
		fields = ['id', 'name', 'name_cn', 'email', 'mobile']
		try:
			sql = "select %s from users where id = %s " % (','.join(fields),id)
			cur.execute(sql)
			res = cur.fetchone()
			user = {}
			for i,k in enumerate(fields):
				user[k]=res[i]
			return render_template('update.html', user = user)
		except:
			errmsg = "get one failed"
			print traceback.print_exc()
			return render_template("update.html",result=errmsg)
	# 	userinfo=getuser(uid)
	# 	return render_template("update.html",user=userinfo)
	# if request.method == 'POST':
	# 	userinfo={}
	# 	userinfo=["name"] = request.form['name']
	# 	userinfo=["name_cn"] = request.form['name_cn']
	# 	userinfo=["email"] = request.form['email']
	# 	userinfo=["mobile"] = request.form['mobile']
	# 	userinfo=["role"] = request.form['role']
	# 	userinfo=["status"] = request.form['status']
	# 	update_user(userinfo)
	# 	return redirect("/userlist")


# @app.route('/update', methods=['GET', 'POST'])
# def update():
#     if request.method == 'POST':
#         user_data = request.form.to_dict()
#         db.user_update(user_data)
#         return redirect('/userlist')
#     id = request.args.get('id')
#     user = db.get_user_by_id(id)
#     return render_template('update.html', user=user)


@app.route('/delete', methods=['GET'])
def delete():
	id = request.args.get('id')
	if db.user_del(id):
		return redirect('/userlist')
	return 'del user failed'

@app.route('/userinfo')
def userinfo():
    where = {}
    where['id'] = request.args.get('id',None)
    where['name'] = request.args.get('name',None)
    if not where['id']  and not where['name']:
        errmsg  = "must hava a where"
        return render_template('index.html', result = errmsg )
    if where['id'] and not where['name']:
       condition = 'id = "%(id)s"' % where
    if where['name'] and not where['id']:
       condition = 'name = "%(name)s"' % where
    fields = ['id', 'name', 'name_cn', 'email', 'mobile'] 
    try:
        sql = "select %s from users where %s" % (','.join(fields),condition)
        cur.execute(sql)
        res = cur.fetchone()
        # user = {}
        # for i,k in enumerate(fields):    
        #     user[k]=res[i]   
        #字典2.0
        user = dict((k, res[i]) for i,k in enumerate(fields))
        #字典3.0
        # users = [dict((k, row[i]) for i,k in enumerate(fields)) for row in res]
        return  render_template('index.html', user=user)
    except:
        errmsg  = "get one failed"
        print traceback.print_exc()
        return render_template("index.html",result=errmsg)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=9092,debug=True) 
