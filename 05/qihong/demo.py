#!/bin/env python
#coding:utf-8

from flask import Flask,request,render_template,redirect
import MySQLdb as mysql
import json 
import time
import traceback

conn=mysql.connect(user='reboot',host='127.0.0.1',passwd='reboot123', db='reboot10', charset='utf8') 
conn.autocommit(True)
cur = conn.cursor()


app = Flask(__name__)
# 册页面。 用GET 请求， 点击表单按钮提交用POST方式。 执行SQL 插入数据， 注册成功
#则跳转到个人信息页面， 失败则在注册页面打印错误信息。
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = {}
        data["name"] = request.form.get('name', None)
        data["name_cn"] = request.form.get('name_cn', None)
        data["mobile"] = request.form.get('mobile', None)
        data["email"] = request.form.get('email', None)
        data["role"] = request.form.get('role', None)
        data["status"] = request.form.get('status', None)
        data["password"] = request.form.get('password', None)
        data["repwd"] = request.form.get('repwd', None)
        data["create_time"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        print data
        fields = ['name', 'name_cn', 'mobile', 'email', 'role', 'status', 'password', 'create_time']
        if not data["name"] or not data["password"] or not data["role"]:
            errmsg = 'name or password or role not null'
            return render_template("register.html", resut=errmsg)
        if data["password"] != data["repwd"]:
            errmsg = 'the two password ou tpe do not match'
            return render_template("register.html", result=errmsg)
        try:
            sql = 'insert Into User (%s) VALUES (%s)' %(','.join(fields), ','.join(['"%s"' %data[x] for x in fields]))
            print sql
            cur.execute(sql)
            return redirect('/userinfo?name=%s' %data['name'])
        except:
            errmsg = "insert failed"
            print traceback.print_exc()
            return render_template('register.html', result = errmsg)
    else:
        return render_template("register.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9092,debug=True)
