#coding:utf-8

from flask import Flask,request,render_template,redirect,session
import json
import time
import traceback
import user_db



app = Flask(__name__)
app.secret_key = "sdferwq"

@app.route('/')
def index():
    return redirect('/login')

@app.route('/register',methods=['GET','POST'])
def register():
    if not session.get('name',None):
	return redirect('/login')
    if session.get('role') != 'admin':
	errmsg = "you are not admin, can not register user"
	return render_template('userlist.html', result = errmsg)
    if request.method == 'POST':
	data = {}
        data = dict((k,v[0]) for k,v in dict(request.form).items())
        data["create_time"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
	print data
        # data = request.get_json()
	fields = ['name','name_cn','mobile','email','role','status','password','create_time']
	if not data["name"] or not data["password"] or not data["role"]:
	    errmsg = "name or password or role not null"
	    return render_template("register.html", result=errmsg)
	if data["password"] != data["repwd"]:
	    errmsg = "The two passwords you typed do not match"
	    return render_template("register.html", result=errmsg)
	try:    
	    user_db.insert(fields,data)
	    return redirect('/userinfo?name=%s' % data['name'])
	except:
	    errmsg = 'insert error'
	    print traceback.print_exc()
	    return render_template("register.html", result=errmsg)
    else:
	return render_template("register.html")

@app.route('/userinfo')
def userinfo():
    if not session.get('name',None):
	redirect('/login')
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
	res = user_db.selectOne(fields,condition)
	user = dict((k,res[i]) for i,k in enumerate(fields))
        return  render_template('index.html', user = user)
    except:
        errmsg  = "get one failed"
        print traceback.print_exc()
        return render_template("index.html",result=errmsg)

@app.route('/userlist')
def userlist():
    if not session.get('name',None):
	return redirect('/login')
    users = []
    fields = ['id', 'name', 'name_cn', 'email', 'mobile']
    try:
        role = session['role']
        if role != 'admin':
	    condition = 'name = "%s"' % session.get('name',None)
	    result = user_db.selectOne(fields,condition)
	    users = [dict((k,result[i]) for i,k in enumerate(fields))]
	else:
	    result = user_db.selectAll(fields)
            users = [dict((k,row[i]) for i,k in enumerate(fields)) for row in result]
        return  render_template('userlist.html', users = users)
    except:
        errmsg = "select userlist failed"
        print traceback.print_exc()
        return  render_template("userlist.html",result=errmsg)
    
@app.route('/update', methods=['GET','POST'])
def update():
    if not session.get('name',None):
	return redirect('login.html')
    if request.method == "POST":
	data = dict(request.form)
	condition = [ "%s='%s'" % (k,v[0]) for k,v in data.items() ]
	try:
	    user_db.update(condition, data['id'][0])
	    return redirect('/userlist')
	except:
	    errmsg = "update user failed"
            print traceback.print_exc()
            return  render_template("update.html",result = errmsg)
    else:
	id = request.args.get('id')
	fields = ['id', 'name', 'name_cn', 'email', 'mobile']
	try:
	    res = user_db.selectId(fields,id)
	    user = dict((k,res[i]) for i,k in enumerate(fields))
	    
	    return render_template('update.html', user = user)
	except:
	    errmsg = "select userinfo failed"
            print traceback.print_exc()
	    return render_template("update.html", result = errmsg)
    
@app.route('/delete', methods=['GET'])
def delete():
    if not session.get('name',None):
	return redirect('/login')
    id = request.args.get('id')
    try:
	user_db.delete(id)
	return redirect('/userlist')
    except:
	errmsg = 'delete user failed'
	print traceback.print_exc()
	return render_template("userlist.html", result = errmsg)

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
	data = dict((k,v[0]) for k,v in dict(request.form).items())
	if not data.get('name',None) or not data.get('password',None):
	    errmsg = "name or password not null"
	    return render_template('login.html', result = errmsg)
	fields = ['name','password','role']
	condition = 'name = "%(name)s"' % data
	res = user_db.selectOne(fields,condition)
	if not res:
	    errmsg = "%s does not exit" % data['name']
	    return render_template('login.html', result = errmsg)
	user = dict((k,res[i]) for i,k in enumerate(fields))
	if data['password'] != user['password']:
	    errmsg = "password is wrong"
	    return render_template('login.html', result = errmsg)

	session['name'] = user['name']
	session['role'] = user['role']
	
	return redirect('/userlist')
    else:
	return render_template('login.html')

@app.route('/logout', methods=['GET'])
def logout():
    session.pop('name')
    session.pop('role')
    return redirect('/login')

    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9092,debug=True)
