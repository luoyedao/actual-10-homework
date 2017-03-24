from flask import Flask,request,render_template,redirect
import MySQLdb as mysql
import traceback

conn = mysql.connect(user='root',host='127.0.0.1',passwd='123456',db='reboot10',charset='utf8')
cur = conn.cursor()

#new app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

    


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
        data["repasswd"] = request.form.get('repasswd',None)
	fields = [name,name_cn,mobile,email,role,status,password]
	if not data[name] or not data[password] or not data[role]:
	    errmsg = 'name or password or role can not be null'
            return render_template('register.html', result = errmsg)
        if data[password] != data[repasswd]:
	    errmsg = 'password error'
            return render_template('register.html', result = errmsg)
	try:
	    sql = 'insert into users (%s) values (%s)' % (','.join(fields), ','.join(['"%s"' % data[x] for x in fields]))
	    cur.execute(sql) 
	    return redirect('/userinfo?name=%s' % data["name"])
	except:
	    errmsg = 'insert failed'
	    print traceback.print_exc()
            return render_template('register.html', result = errmsg)
    else:
            return render_template('register.html')


@app.route('/userinfo')
def userinfo():
    where = {}
    where['id'] = request.args.get('id',None)
    where['name'] = request.args.get('name',None)
    if not where['id'] and where['name']:
	errmsg  = 'must have a condition'
	return render_template('index.html', result = errmsg)
    if where['id'] and not where['name']:
	condition = 'id = "%(id)s"' % where
    if where['name'] and not where['id']:
	condition = 'name = "%(name)s"' % where
    fields = ['id', 'name', 'name_cn', 'email', 'mobile']
    try:
	sql = "select %s from users where %s" % (','.join(fields),condition)
	cur.execute(sql)
	res = cur.fetchone()
	user = {}
	for i,k in enumerate(fields):
	    user[k] = res[i]
	return render_template('index.html',user = user)
    except:
	errmsg = "get one failed"
	print traceback.print_exc()
	return render_template('index.html',result = errmsg)

@app.route('/update')
def update():
    


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9092,debug=True)
