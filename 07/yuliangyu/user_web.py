#coding:utf-8

from flask import Flask,request,render_template,redirect
import MySQLdb as mysql
import json
import time
import traceback

conn=mysql.connect(user='root',host='127.0.0.1',passwd='123456',db='reboot10',charset='utf8')
conn.autocommit(True)
cur = conn.cursor()


app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/login')

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        data = dict(request.form)
        data["create_time"] = [time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))]
        # data = request.get_json()
	fields = ['name','name_cn','mobile','email','role','status','password','create_time']
	if not data["name"][0] or not data["password"][0] or not data["role"][0]:
	    errmsg = "name or password or role not null"
	    return render_template("register.html", result=errmsg)
	if data["password"][0] != data["repwd"][0]:
	    errmsg = "The two passwords you typed do not match"
	    return render_template("register.html", result=errmsg)
	try:    
	    sql = 'INSERT INTO users (%s) VALUES (%s)' % (','.join(fields), ','.join(['"%s"' % data[x][0] for x in fields]))
	    cur.execute(sql)
	    return redirect('/userinfo?name=%s' % data['name'][0])
	except:
	    errmsg = 'insert error'
	    print traceback.print_exc()
	    return render_template("register.html", result=errmsg)
    else:
	return render_template("register.html")

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
   #     user = {}
   #     for i,k in enumerate(fields):
   #         user[k]=res[i]
	user = dict((k,res[i]) for i,k in enumerate(fields))
        return  render_template('index.html', user = user)
    except:
        errmsg  = "get one failed"
        print traceback.print_exc()
        return render_template("index.html",result=errmsg)

@app.route('/userlist')
def userlist():
    users = []
    fields = ['id', 'name', 'name_cn', 'email', 'mobile']
    try:
        sql = "select %s from users" % ','.join(fields)
        cur.execute(sql)
        result = cur.fetchall()
#        for row in result:
#            user = {}
#            for i, k in enumerate(fields):
#                user[k] = row[i]
#            users.append(user)    
        users = [dict((k,row[i]) for i,k in enumerate(fields)) for row in result]
        return  render_template('userlist.html', users = users)
    except:
        errmsg = "select userlist failed"
        print traceback.print_exc()
        return  render_template("userlist.html",result=errmsg)
    
@app.route('/update', methods=['GET','POST'])
def update():
    if request.method == "POST":
	data = dict(request.form)
	condition = [ "%s='%s'" % (k,v[0]) for k,v in data.items() ]
	try:
	    sql = "update users set %s where id=%s" % (','.join(condition), data['id'][0])
	    cur.execute(sql)
	    return redirect('/userlist')
	except:
	    errmsg = "update user failed"
            print traceback.print_exc()
            return  render_template("update.html",result = errmsg)
    else:
	id = request.args.get('id')
	fields = ['id', 'name', 'name_cn', 'email', 'mobile']
	try:
  	    sql = "select %s from users where id = %s" %(','.join(fields), id)
	    cur.execute(sql)
	    res = cur.fetchone()
	    user = dict((k,res[i]) for i,k in enumerate(fields))
	    
	    return render_template('update.html', user = user)
	except:
	    errmsg = "select userinfo failed"
            print traceback.print_exc()
	    return render_template("update.html", result = errmsg)
    
@app.route('/delete', methods=['GET'])
def delete():
    id = request.args.get('id')
    try:
        sql = "delete from users where id = '%s'" % (id)
	cur.execute(sql)
	return redirect('/userlist')
    except:
	errmsg = 'delete user failed'
	print traceback.print_exc()
	return render_template("userlist.html", result = errmsg)

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
	name = request.form.get('name')
	password = request.form.get('password')
	sql_name = "select name from users where name = '%s'" % (name)
	cur.execute(sql_name)
	if not cur.fetchone():
	    errmsg = "login name error"
	    return render_template('login.html', result = errmsg)
	sql_pwd = "select password from users where name = '%s'" % (name)
	cur.execute(sql_pwd)
	res_pwd = cur.fetchone()
	if password != res_pwd[0]:
	    errmsg = "login password error"
	    return render_template('login.html', result = errmsg)
	
	return redirect('/userlist')
    else:
	return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9092,debug=True)
