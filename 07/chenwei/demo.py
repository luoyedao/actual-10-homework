#coding:utf-8

from flask import Flask,request,render_template,redirect,session
#import MySQLdb as mysql
import json
import time
import traceback
from db import ulist,getone,modify,insert,delete,userinfo

#conn=mysql.connect(user='root',host='127.0.0.1',passwd='123456',db='reboot10',charset='utf8')
#conn.autocommit(True)
#cur = conn.cursor()

app = Flask(__name__)
app.secret_key = 'zYpRh/QxW3c=' # 可使用os.urandom()来生成


@app.route('/userinfo')
def userinfo():
    if not session.get('name',None):
	return redirect('login')
    where = {}
    where['id'] = request.args.get('id',None)
    where['name'] = request.args.get('name',None)
    if not where['id'] and not where['name']:
	errmsg = 'must have a where'
	return render_template('index.html',result = errmsg)
    if where['id'] and not where['name']:
	condition = 'id = "%(id)s"' % where
    if where['name'] and not where['id']:
	condition = 'name = "%(name)s"' % where
    fields = ['id', 'name', 'name_cn', 'email', 'mobile']
'''
    try:
	sql = 'select %s from users where %s' % (','.join(fields),condition)
	cur.execute(sql)
	res = cur.fetchone()
	user = dict((k,res[i]) for i,k in enumerate(fields))
	return render_template('index.html',user = user)
    except:
	errmsg = 'get on failed'
	print traceback.print_exc()
	return render_template("index.html",result=errmsg)
'''
    user = userinfo(fields,condition)
    return render_template('index.html',user = user)


@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
	data={}
        data["name"]=request.form.get('name',None)
        data["name_cn"]=request.form.get('name_cn',None)
        data["password"]=request.form.get('password',None)
        data["repwd"]=request.form.get('repwd',None)
        data["email"]=request.form.get('email',None)
        data["mobile"]=request.form.get('mobile',None)
        data["role"]=request.form.get('role',None)
        data["status"]=request.form.get('status',None)
        data["create_time"]=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
	#data = dict((k,v[0]) for k,v in dict(request.form).items())
	fields = ['name','name_cn','mobile','email','role','status','password','create_time']
	if not data['name'] or not data['password'] or not data['role']:
	    errmsg = 'name or password or role not null'
	    return render_template('register.html',result=errmsg)
	if data['password'] != data['repwd']:
	    errmsg = 'The two passwords you tpyed do not match!!!'
	    return render_template('register.html',result=errmsg)
'''
	try:
	    sql = 'INSERT INTO users (%s) VALUES (%s)' % (','.join(fields), ','.join(['"%s"' % data[x] for x in fields]))
	    cur.execute(sql)
	    return redirect('/userinfo?name=%s' % data['name'])
	except:
	    errmsg = 'insert failed'
	    print traceback.print_exc()
	    return render_template('register.html',result=errmsg)
'''
	data = insert(fields)
	return redirect('/userinfo?name=%s' % data['name'])
    else:
        return render_template("register.html")

@app.route('/userlist')
def userlist():
    if not session.get('name',None):
	return redirect('login')
    users = []
    fields = ['id','name','name_cn','email','mobile']
'''
    try:
	sql = 'select %s from users'% ','.join(fields)
	cur.execute(sql)
	result = cur.fetchall()
	users = [dict((k,row[i]) for i,k in enumerate(fields)) for row in result]
	return render_template('userlist.html',users = users )
    except:
	errmsg = 'select userlist failed'
	print traceback.print_exc()
	return render_templated('userlist.html',result = errmsg)
'''
    users = u_list(fields)
    return render_template('userlist.html',users = users )

@app.route('/delete',methods=['GET'])
def delete():
    if not session.get('name',None):
	return redirect('login')
    id = request.args.get('id',None)
    if not id:
	errmsg = 'must have id '
	return render_template('userlist.html',result = errmsg)
'''
    try:
	sql = 'delete from users where id = %s' % id
	cur.execute(sql)
	return redirect('/userlist')
    except:
	errmsg = 'delete failed '
	print traceback.print_exc()
	return render_template('userlist.html',result = errmsg)
'''
    delete(id)
    return redirect('/userlist')


@app.route('/update',methods=['POST','GET'])
def update():
    if not session.get('name',None):
	return redirect('login')
    if request.method == 'POST':
	data = dict(request.form)
'''
	condition = ["%s='%s'" % (k,v[0]) for k,v in data.items()]
	sql = 'update users set %s where id = %s' % (','.join(condition),data['id'][0])
	cur.execute(sql)
'''
	modify(data)	
	return redirect('/userlist')
    else:
	id = request.args.get('id',None)
	if not id:
	    errmsg = 'must have id'
	    return render_template('update.html',result=errmsg)
	fields = ['id', 'name', 'name_cn', 'email', 'mobile']
'''
	try:
	    sql = 'select %s from users where id = %s ' % (','.join(fields),id)
	    cur.execute(sql)
	    res = cur.fetchone()
	    user = dict((k,res[i]) for i,k in enumerate(fields))
	    return render_template('update.html', user = user)
	except:
	    errmsg = 'get on failed'
	    print traceback.print_exc()
	    return render_template('update.html',result = errmsg)
'''
	user = getone(id)
	return render_template('update.html', user = user)


@app.route('/')
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
	data = dict((k,v[0]) for k,v in dict(request.form).items())
	# data = {k:v[0] for k,v in dict(request.form).items()}
	print data.get('name')
        if not data.get('name',None) or not data.get('password',None):
	    errmsg = 'name or password not null'
	    return render_template('login.html',result = errmsg)

	fields = ['name','password']
'''
	sql = 'select %s from users where name="%s"'%(','.join(fields),data['name'])
	cur.execute(sql)
	res = cur.fetchone()
'''
	if not u_list(['name']):
	    errmsg = '%s is not exist'%data['name']
	    return render_template('login.html',result = errmsg)
	user = {}
	user = dict((k,res[i]) for i,k in enumerate(fields))
	if user['password'] != data['password']:
	    errmsg = 'password is wrong'
	    return render_template('login.html',result = errmsg)
	else:
	    session['name'] = data['name'] # 将name记录到session中，生成session
	    return redirect('/userlist')
    else:
	return render_template('login.html')

@app.route('/loginout')
def loginout():
    session.pop('name') # 删除session中的name
    return redirect('/login')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9092,debug=True)



