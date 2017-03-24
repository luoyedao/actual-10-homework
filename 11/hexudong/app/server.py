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

@app.route('/server')
@login_required
def server():
    return render_template("server.html",info=session)
