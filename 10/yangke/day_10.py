from flask import Flask
from flask import redirect,render_template,session,request
from db import *
import json

app = Flask(__name__)
app.secret_key = "dfahiu2jf"



@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        login_info = dict((k, v[0]) for k, v in dict(request.form).items())
        if not getone({"name":login_info["name"]}):
            return json.dumps({"code": 0, "result":"user is not exist"})
        if login_info["password"] != getone({'name': login_info["name"]})["password"]:
            return json.dumps({"code": 0, "result":"password error"})

        u_role = getone({"name":login_info["name"]})["role"]
        session["username"] = login_info["name"]
        session["role"] = u_role
        return json.dumps({"code": 1,"result":"login success"})


@app.route('/')
def index():
    if not session.get("username",None):
        return redirect("/login")
    return render_template("index.html",info=session)

@app.route('/userlist')
def user_list():
    if not session.get("username",None):
        return redirect("/login")
    fields = ["id", "name", "name_cn", "mobile", "email", "role", "status"]
    data = userlist(fields)
    return render_template("userlist.html", users=data, info=session)

@app.route('/add',methods=["GET","POST"])
def add():
    if request.method == "GET":
        return render_template("add.html",info=session)
    else:
        addinfo = dict((k, v[0]) for k, v in dict(request.form).items())
        if getone({"name":addinfo["name"]}):
            return json.dumps({"code":1,"errmsg":"user is exist"})
        adduser(addinfo)
        return json.dumps({"code":0,"result":"add user success"})

@app.route('/delete')
def dele():
    if not session.get("username",None):
        return redirect("/login")
    uid = request.args.get("id")
    delete(uid)
    return json.dumps({"code":0,"result":"delete user success"})

@app.route('/update',methods=["GET","POST"])
def up():
    if request.method == "GET":
        uid = request.args.get("id")
        userinfo = getone({"id":uid})
        return json.dumps(userinfo)
    else:
        userinfo = dict((k,v[0]) for k,v in dict(request.form).items())
        modfiy(userinfo)
        return json.dumps({"code":0})

@app.route('/modfpasswd',methods=["POST"])
def uppasswd():
    data = dict((k,v[0]) for k,v in dict(request.form).items())
    if len(data) == 3:
        if data["password"] != data["re_password"]:
            return json.dumps({"code":1,"errmsg":"The tow password is different"})
        data.pop("re_password")
        print data
        modpasswd(data)
        return json.dumps({"code":0,"result":"Successful modification"})
    elif len(data) == 4:
        dic = {}
        if data["password"] != getone({"name":data["name"]})["password"]:
            return json.dumps({"code":1,"errmsg":"The password is error"})
        elif data["new_password"] != data["re_password"]:
            return json.dumps({"code":1,"errmsg":"The tow password is different"})
        dic["name"] = data["name"]
        dic["password"] = data["new_password"]
        modfiy(dic)
        return json.dumps({"code":0,"result":"Successful modification"})

@app.route('/ucenter')
def ucenter():
    username = session.get("username",None)
    userinfo = getone({"name":username})
    del userinfo["password"]
    return render_template("ucenter.html",uinfo=userinfo,info=session)

@app.route('/idc')
def idc():
    return render_template("idc.html",info=session)

@app.route('/server')
def server():
    return render_template("server.html",info=session)

@app.route('/cabinet')
def cabinet():
    return render_template("cabinet.html",info=session)

@app.route('/logout/')
def logout():
    session.pop("username",None)
    session.pop("role",None)
    return redirect("/login")

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8000,debug=True)
