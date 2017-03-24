#!/usr/local/python/bin/python
#coding:utf-8

from flask import Flask,request,render_template,redirect
import MySQLdb as mysql
import json 
import time
import traceback

app = Flask(__name__)

conn=mysql.connect(user='reboot',host='127.0.0.1',passwd='reboot123',db='reboot10',charset='utf8')
conn.autocommit(True) 
cur = conn.cursor()

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        res = dict(request.form)
        data = dict([i,k[0]] for i,k in res.items())
        data['create_time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        fields = ['name','name_cn','mobile','email','role','status','password','create_time']
        if not data["name"] or not data["password"] or not data["role"]:
            errmsg = 'name or password not null'
            return render_template("register.html",result=errmsg)
        if data["password"] != data["repwd"]:
            errmsg = 'the two passwords you typed do not match'
            return render_template("register.html",result=errmsg)
        try:
            sql = 'INSERT INTO users (%s) VALUES (%s)' % (','.join(fields), ','.join(['"%s"' % data[x] for x in fields]))
            print sql
            cur.execute(sql)
            return redirect ('/userinfo?name=%s' % data['name'])
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
    print where['id']
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
        user = dict((k,res[i]) for i,k in enumerate(fields))
        return  render_template('index.html', user = user)
    except:
        errmsg  = "get one failed"
        print traceback.print_exc()
        return render_template("index.html",result=errmsg)

# 用户列表，生产环境中只有管理员才有这个权限，暂时不设置权限
@app.route('/userlist')
def userlist():
    users = []
    fields = ['id', 'name', 'name_cn', 'email', 'mobile'] 
    try:
        sql = "select %s from users" % ','.join(fields) 
        cur.execute(sql)
        result = cur.fetchall()
        users = [dict((k,row[i]) for i,k in enumerate(fields)) for row in result]
        return  render_template('userlist.html', users = users)
    except:
        errmsg = "select userlist failed" 
        print traceback.print_exc()
        return  render_template("userlist.html",result=errmsg)

@app.route('/update',methods=['GET','POST'])
def update():
    if request.method == "POST":
        print request.form,'update'          # 这是个高级写法，把请求内容直接搞成字典，课上会细讲,打印看看长啥样
        data = dict(request.form)   # 转为字典打印出来看张啥样
        print data                  # {'status': [u'0'], 'role': [u'admin'],....}
        conditions = [ "%s='%s'" %  (k,v[0]) for k,v in data.items()]
        sql = "update users set %s where id = %s" % (','.join(conditions),data['id'][0])
        print sql
        cur.execute(sql)
        return redirect('/userlist')
    else:
        id = request.args.get('id',None)
        if not id:
            errmsg = "must have a id"
        fields = ['id','name','name_cn','email','mobile']
        try:
            sql = "select %s from users where id = %s " % (','.join(fields),id)
            print sql
            cur.execute(sql)
            res = cur.fetchone()
            user = dict((k,res[i]) for i,k in enumerate(fields))
            return  render_template('update.html', user = user)
        except:
            errmsg = "get one failed"
            print traceback.print_exc()
            return  render_template("update.html",result=errmsg)

@app.route('/delete',methods=['GET'])
def delete():
    id = request.args.get('id',None)
    if not id:
        errmsg = "must have id" 
        return render_template("userlist.html",result=errmsg)
    try:
        sql = "delete from users where id = %s" % id
        cur.execute(sql)
        return redirect('/userlist')
    except:
        errmsg = "delete failed" 
        return render_template("userlist.html",result=errmsg)

@app.route('/login',methods=['GET'])
def login():
    return render_template('login.html')
@app.route('/login_process',methods=['GET','POST'])
def login_process():
    username = request.form.get('username')
    password = request.form.get('password')
    if not username and not password:
        errmsg = "must have username and passord"
        return render_template("login.html",result=errmsg)
    try:
        sql = "SELECT password FROM users WHERE name='%s';" % (username)
        cur.execute(sql)
        pwd = str(cur.fetchone()[0])
        if pwd == str(password):
            return 'login successfully'
        else:
            errmsg = 'wrong password'
            return render_template("login.html",result=errmsg)
    except:
        errmsg = 'wrong username, login failed'
        return render_template("login.html",result=errmsg)

if __name__ =='__main__':
    app.run(host='0.0.0.0',port=9099,debug=True)
