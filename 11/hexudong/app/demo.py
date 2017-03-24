#coding:utf-8
from run import app
from flask import Flask,render_template,request,redirect,session
import json 
from functools import wraps
from db import *
import hashlib

salt = "qwe"

def login_required(func):
    @wraps(func)
    def deco(*args,**kwargs):
        if not session.get('username'):
            return redirect("/login")
        else:
            return func(*args,**kwargs)
    return deco


@app.route("/")
@app.route("/index")
@login_required
def index():
    if not session.get('username',None):
        return redirect("/login")
    result = getone({'name':session['username']})
    return render_template('index.html',info=session,user=result)

@app.route('/userlist')
@login_required
def user_list():
    fields = ["id","name","name_cn","mobile","email","role","status"]
    data = userlist(fields)
    #result = getone({'name':session['username']})
    role = session['role']
    #role = getone({'name':session['username']})
    print role
    return render_template("userlist.html",users = data,me_role=role,info=session)

@app.route("/add",methods=["GET","POST"])
@login_required
def add_user():
    if request.method == "POST":
        data=dict((k,v[0]) for k,v in dict(request.form).items())
        data['password']=hashlib.md5(data['password']+salt).hexdigest()
        #if data["name"] in checkuser({"name":data["name"]},"name"):
        #    return json.dumps({"code":1,"errmsg":"username is exist"})
        adduser(data)
        return json.demps({"code":0,"result":"add user success"})
    else:
        return render_template("add.html",info=session)

@app.route("/userinfo")
@login_required
def userinfo():
    where ={}
    where['id'] = request.args.get('data-id',None)
    data=Getone(where['id'])
    print data
    return render_template('userlist.html',user = data)

@app.route("/delete")
@login_required
def del_user():
    uid = request.args.get("id")
    delete(uid)
    return json.dumps({"code":0,"result":"delete user success"})

