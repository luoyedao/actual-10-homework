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


#注册， 记添加用户， 第一次请求获取注册页面。 用GET 请求， 点击表单按钮提交用POST方式。 执行SQL 插入数据， 注册成功
#则跳转到个人信息页面， 失败则在注册页面打印错误信息。
@app.route('/register', methods=['GET], 'POST])
def register():
    if request.method == 'PSOT':
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
                                                                                                            if not data["name"] or not data["password"] or not data["role"]
                                                                                                                        errmsg = 'name or password or role not null'
                                                                                                                                    return render_template("register.html", resut=errmsg)
                                                                                                                                            if data["password"] != data["repwd"]:
                                                                                                                                                        errmsg = 'the two password ou tpe do not match'
                                                                                                                                                                    return render_template("register.html", result=errmsg)
                                                                                                                                                                            try:
                                                                                                                                                                                        sql = 'insert Into User (%s) VALUES (%s)' %','.join(fields), ','.join(['"%s"' %data[x] for x in fields]))
                                                                                                                                                                                                    cur.execute(sql)
                                                                                                                                                                                                                return redirect('/userinfo?name=%s' %data['name'])
                                                                                                                                                                                                                        except:
                                                                                                                                                                                                                                    errmsg = "insert failed"
                                                                                                                                                                                                                                                print traceback.print_exc()
                                                                                                                                                                                                                                                            return render_template('register.html', result = errmsg )



