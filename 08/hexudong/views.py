#!/usr/bin/env python
# -*- coding:utf-8 -*-
#__author__ = 'Madon'
from run import app
from flask import render_template,request,redirect,session
from db import *
from functools import wraps
import traceback

def login_required(func):
    @wraps(func)
    def deco(*args,**kwargs):
        if not session.get("username"):
            return redirect("/login")
        else:
            return func(*args,**kwargs)
    return deco

@app.route('/')
def index():
    return render_template("/login")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.route('/userlist')
@login_required
def userlist():
    data=Userlist()
    return render_template("userlist.html",users=data)

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "POST":
        login_info =dict((k,v[0]) for k,v in dict(request.form).items())
        if login_info["password"] == Checkuser(login_info["name"]):
            session["username"]=login_info["name"]
            return redirect("/userlist")
        else:
            errmsg = "wrong user or password"
            return render_template("login.html",result=errmsg)
    else:
        return render_template("login.html")

@app.route("/register",methods=["GET","POST"])
def register():
    if request.method =="POST":
        data=dict(request.form)
        conditions=["%s='%s'" %(k,v[0]) for k,v in data.items()]
        try:
            Request(conditions)
            #errmsg="Successed"  #add Wrong
            return redirect("/userinfo?name=%s" %request.form.get('name'))
        except:
            errmsg="Wrong"   #add Wrong
            print traceback.print_exc()
            return render_template("userlist.html",result=errmsg)
    else:
        return render_template("register.html")

@app.route("/userinfo")
@login_required
def userinfo():
    where ={}
    where['name'] = request.args.get('name',None)
    data=Getone(where['name'])
    return render_template('index.html',user = data)

@app.route("/update",methods=['GET','POST'])
@login_required
def update():
    if request.method=="POST":
        data=dict(request.form)
        conditions = ["%s='%s'" %(k,v[0]) for k,v in data.items()]
        id =data['id'][0]
        try:
            Monfiy(conditions,id)
            return redirect("/userlist")
        except:
            errmsg="Wrong"   #add Wrong
            print traceback.print_exc()
            return render_template("userlist.html",result=errmsg)
    else:
        id =request.args.get('id',None)
        if not id:
            errmsg="must have id"
            return render_template("update.html",result=errmsg)
        try:
            data=Getid(id)
            return render_template("update.html",user=data)
        except:
            errmsg="Wrong"
            return render_template("update.html",result=errmsg)

@app.route("/update_password",methods=['GET','POST'])
def update_password():
    if request.method=='POST':
        userdict=dict(request.form)
        new_password = ['%s="%s"' %(k, v[0]) for k, v in userdict.iteritems() if k == 'password']
        if userdict["password_old"][0] != Checkpassword(request.form.get('id')):
            errmsg="password Wrong"
            return render_template("update_password.html",result=errmsg)
        elif userdict["password"][0] != userdict["password_rep"][0]:
            errmsg="NEW password Wrong"
            return render_template("update_password.html",result=errmsg)
        else:
            Monfiy(new_password,userdict['id'][0])
            return redirect("/userlist")
    else:
        id = request.args.get('id',None)
        if not id:
            errmsg ='must have id'
            return render_template("update_password.html",result=errmsg)
        data = SelectPassword(id)
        return render_template("update_password.html",user=data)

@app.route('/delete',methods=['GET'])
@login_required
def delete():
    id=request.args.get('id',None)
    if not id:
        errmsg="much hava id"
        return render_template("userlist.html",result=errmsg)
    Delete(id)
    return redirect('/userlist')

@app.route("/logout")
@login_required
def logout():
    session.pop('username', None)
    return redirect("/login")
