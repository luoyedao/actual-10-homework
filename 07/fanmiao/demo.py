#coding:utf-8

from flask import Flask,request,render_template,redirect
import MySQLdb as mysql
import json 
import time
import traceback

conn=mysql.connect(user='root',host='127.0.0.1',passwd='yy7943RMB',db='reboot10',charset='utf8')
conn.autocommit(True) 
cur = conn.cursor()


app = Flask(__name__)

@app.route('/register',methods=['GET','POST'])
def register():
	if request.method == 'POST':
		res =dict(request.form)
		data=dict([i,k[0]] for i,k in res.items())
		data["create_time"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) 
		fields = ['name','name_cn','mobile','email','role','status','password','create_time']
		if not data["name"] or not data["password"] or not data["role"]:
			errmsg = 'name or password or role not null'
			return render_template("register.html",result=errmsg)
		if data["password"] != data["repwd"]:
			errmsg = 'The two passwords you typed do not match'
			return render_template("register.html",result=errmsg)
		try:
			sql = 'INSERT INTO users (%s) VALUES (%s)' % (','.join(fields),','.join(['"%s"' % data[x] for x in fields]))
			print sql
			cur.execute(sql)
			return redirect('/userinfo?name=%s' % data['name'])
		except:
			errmsg = "insert failed"
			print traceback.print_exc()
			return render_template("register.html",result=errmsg)
	else:
		return render_template("register.html")

@app.route('/userinfo')
def userinfo():
	where = {}
	where['id'] = request.args.get('id',None)
	where['name'] = request.args.get('name',None)
	if not where['id'] and not where ['name']:
		errmsg = "must have a where"
		return render_template('index.html',result = errmsg)
	if where['id'] and not where['name']:
		condition = 'id = "%(id)s"' % where
	if where['name'] and not where['id']:
		condition = 'name = "%(name)s"' % where
	fields = ['id','name','name_cn','email','mobile']
	try:
		sql = "select %s from users where %s" %(','.join(fields),condition)
		cur.execute(sql)
		res = cur.fetchone()
		user=dict((k,res[i]) for i,k in enumerate(fields))
		return render_template('index.html',user=user)
	except:
		errmsg = "get one failed"
		print traceback.print_exc()
		return render_template('index.html',result=errmsg)


@app.route('/userlist')
def userlist():
	users=[]
	fields= ['id', 'name', 'name_cn', 'email', 'mobile']
	try:
		sql = "select %s from users" % ','.join(fields)
		cur.execute(sql)
		result=cur.fetchall()
		users=[dict((k,row[i]) for i,k in enumerate(fields)) for row in result]
		return  render_template('userlist.html', users = users) 
	except:
		errmsg = "select userlist failed"
        	print traceback.print_exc()
        	return  render_template("userlist.html",result=errmsg)   

@app.route('/update',methods=['GET','POST'])
def update():
	if request.method=="POST":
		data=dict(request.form)
		conditions = ["%s='%s'" % (k,v[0]) for k,v in data.items()]
		sql = "update users set %s where id = %s" % (','.join(conditions),data['id'][0])  
		cur.execute(sql) 
		return redirect('/userlist')
	else:
		id = request.args.get('id',None)
		if not id:
			errmsg = "must hava id"
			return render_template("updata.html",result=errmsg)
		fields = ['id','name','name_cn','email','mobile']
		try:
			sql = "select %s from users where id = %s" % (','.join(fields),id)
			cur.execute(sql)
			res = cur.fetchone()
			user=dict((k,res[i]) for i,k in enumerate(fields))
			return render_template('update.html',user=user)
		except:
			errmsg = "get one failed"
			print traceback.print_exc()
			return render_template("update.html",result=errmsg)

@app.route('/delete',methods=['GET'])
def delete():
	id = request.args.get('id',None)
	if not id:
		errmsg="must have id"
		return render_template("userlist.html",result=errmsg)
	try:
		sql = "delete from users where id = %s" % id
		cur.execute(sql)
		return redirect('/userlist')
	except:
		errmsg="delete failed"
		return render_template("userlist.html",result=errmsg)
	

@app.route('/login',methods=['GET','POST'])
def login():
	if request.method=='GET':
		return render_template('login.html')
	else:
		name=request.form.get('name')
		password=request.form.get('password')
		fields = ['id','name','password','name_cn','email','mobile']
	        sql= "select %s from users where name='%s'" % (','.join(fields),name)	 
		cur.execute(sql)
		res=cur.fetchone()
		print "-----------"
		print res
		if res == None:
			errmsg="user not found"
			return render_template('login.html',result=errmsg)
		elif name=="admin" and password==res[2]:
			return redirect('/userlist')
		elif password==res[2]:
			user=dict((k,res[i]) for i,k in enumerate(fields))		
			return render_template('userlistone.html',user=user)
#			return redirect('/userinfo',name=name)
		else:
			errmsg="wrong password "
			return render_template('login.html',result=errmsg)
		
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9001,debug=True)  

