#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import session,redirect,render_template
from functools import wraps

def login_required(func):
    @wraps(func)
    def deco(*args,**kwargs):
        if not session.get('username'):
            return redirect("/login")
        else:
            return func(*args,**kwargs)
    return deco

def my_render(*args,**kwargs):
    return render_template(info=session,*args,**kwargs)