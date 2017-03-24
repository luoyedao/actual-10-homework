#!/usr/bin/env python
# coding:utf-8
# @Date     : 2016-09-07 21:53
# @Author   : William/linqz


from flask import Flask

app = Flask(__name__)

app.secret_key = '$#!@fsa432fd'

from view import *

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True)