#coding:utf-8
from flask import Flask,request,render_template,  redirect,session
from db import * 
import json 

app = Flask(__name__)

app.secret_key = "UIsadl;oi3&*(&9023sd"

@app.route('/login', methods=["GET","POST"])
def login():
    # 用户第一次打开登录页面为GET请求，返回一个空的登录页
    if request.method == "GET":
        return render_template("login.html")
    # 如果用户点击按钮，提交post请求，表明已经填写了用户名和密码，则获取表单的值，然后判断用户密码是否正确
    # 如果不正确则输出错误信息到前端jQuery，如果正确则创建session，并返回正确码code到前端jquery
    if request.method == "POST":
        login_info = dict((k,v[0]) for k,v in dict(request.form).items())
        if not checkuser({"name":login_info["name"]},"name"):
            return json.dumps({"code":1,"errmsg":"user is not exist"})
        if login_info["password"] != checkuser({'name':login_info["name"]})[0]:
            return json.dumps({"code":1,"errmsg":"password error"})
        u_role = checkuser({"name":login_info["name"]},"role")
        session["username"] = login_info["name"]
        session["role"] = u_role
        return  json.dumps({"code":0,'result':'login success'})
       
@app.route("/logout/")
def logout():
    if session.get('username'):
        session.pop('role',None)
        session.pop('username', None)
    return redirect("/login")

@app.route('/')
@app.route('/index')
def index():
   if not session.get('username',None):
        return redirect("/login")
   return  render_template('index.html',info=session)

@app.route('/userlist')
def user_list():
    if not session.get('username',None):
        return redirect("/login")
    fields = ["id","name","name_cn","mobile","email","role","status"]
    data = userlist(fields)
    return  render_template('userlist.html',users=data,info=session)


@app.route("/add",methods=["GET","POST"])
def add_user():
    if not session.get('username',None):
        return redirect("/login")
    if request.method == "GET":
        return render_template("add.html",info=session)
    if request.method == "POST":
         data = dict((k,v[0]) for k,v in dict(request.form).items())
         if data["name"] in checkuser({"name":data["name"]},"name"):
            return json.dumps({"code":1,"errmsg":"username is exist"})
         adduser(data)
         return json.dumps({"code":0,"result":"add user success"})

@app.route("/delete")
def del_user():
    if not session.get('username',None):
        return redirect("/login")
    uid = request.args.get("id")
    delete(uid)
    return json.dumps({"code":0,"result":"delete user success"})


'''
@app.route('/idc')
def idc():
    return  render_template('idc.html')

@app.route('/cabinet')
def cabinet():
    return  render_template('cabinet.html')

@app.route('/server')
def server():
    return  render_template('server.html')
'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090,debug=True)
