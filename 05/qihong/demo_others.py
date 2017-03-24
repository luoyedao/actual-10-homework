#!/bin/env python
#encoding:utf-8

from flask import Flask,request,render_template,redirect
import MySQLdb as mysql
import json 
import time
import traceback

conn=mysql.connect(user='reboot',host='127.0.0.1',passwd='reboot123',db='reboot10',charset='utf8')
conn.autocommit(True) 
cur = conn.cursor()


app = Flask(__name__) 
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
        user = {}
        for i,k in enumerate(fields):    
            user[k]=res[i]   
        return  render_template('index.html', user = user)
    except:
        errmsg  = "get one failed"
        print traceback.print_exc()
        return render_template("index.html",result=errmsg)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9092,debug=True)
