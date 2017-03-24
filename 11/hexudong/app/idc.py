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

@app.route('/idc')
@login_required
def idc():
    fields = ["id","name","name_cn","address","adminer","phone","number"]
    data = Userlist_idc(fields)
    #print data
    #me_role = getone({'role':session['role']})
    role = session['role']
    print role
    return render_template("idc.html",users = data,me_role=role,info=session)
