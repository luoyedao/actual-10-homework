#coding:utf-8

from flask import Flask,request,render_template,redirect
import MySQLdb as mysql
import json
import time
import traceback

conn=mysql.connect(user='root',host='127.0.0.1',passwd='Scmadmin!@#4',db='reboot10',charset='utf8')
conn.autocommit(True)
cur = conn.cursor()


app = Flask(__name__)

@app.route('/')
def users():
    return redirect('/login')


@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        # data =  {}
        # data["name"] = request.form.get('name',None)
        # data["name_cn"] = request.form.get('name_cn',None)
        # data["mobile"] = request.form.get('mobile',None)
        # data["email"] = request.form.get('email',None)
        # data["role"] = request.form.get('role',None)
        # data["status"] = request.form.get('status',None)
        # data["password"] = request.form.get('password',None)
        # data["repwd"] = request.form.get('repwd',None)
        res = dict(request.form)
        data = dict([i,k[0]] for i,k in res.items())
        data["create_time"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

        print data
        fields = ['name','name_cn','mobile','email','role','status','password','create_time']
        if not data['name'] or not data['password'] or not data['role']:
            errmsg = 'anme or password or role not null'
            return render_template("register.html",result=errmsg)

        if data["password"] != data["repwd"]:
            errmsg = 'The two passwords you typed do not match'
            return render_template("register.html",result=errmsg)
        try:
            sql = 'INSERT INTO users (%s) VALUES (%s)' % (','.join(fields),','.join('"%s"' % data[x] for x in fields))
            cur.execute(sql)
            return redirect('/userinfo?name=%s' % data['name'])
        except:
            errmsg = 'insert failed'
            print traceback.print_exc()
            return render_template("register.html",result=errmsg)

    else:
        return render_template("register.html")

@app.route('/userlist')
def userlist():
    users = []
    fields = ['id','name','name_cn','email','mobile']
    try:
        sql = "select %s from users" % ','.join(fields)
        cur.execute(sql)
        result = cur.fetchall()
        for row in result:
            user = {}
            for i, k in enumerate(fields):
                user[k] = row[i]
            users.append(user)
        return render_template('userlist.html',users = users)
    except:
        errmsg = "select userlist failed"
        print traceback.print_exc()
        return render_template("userlist.html",result=errmsg)

@app.route('/userinfo')
def userinfo():
    where = {}
    where['id'] = request.args.get('id',None)
    where['name'] = request.args.get('name',None)
    if not where['id'] and not where['name']:
        errmsg = "must have a where"
        return  render_template('index.html',result = errmsg)
    if where['id'] and not where['name']:
        condition = 'id = "%(id)s"' % where
    if where['name'] and not where['id']:
        condition = 'name ="%(name)s"' % where
    fields = ['id','name','name_cn','email','mobile']
    try:
        sql = "select %s from users where %s" % (','.join(fields), condition)
        cur.execute(sql)
        res = cur.fetchone()
        user = {}
        for i, k in enumerate(fields):
            user[k] = res[i]
        return render_template('index.html', user=user)
    except:
        errmsg = "get one failed"
        print traceback.print_exc()
        return render_template("index.html", result=errmsg)

@app.route('/login',methods=['GET','POST'])
def login():


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9092,debug=True)