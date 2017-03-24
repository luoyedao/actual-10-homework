#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-08-06 18:40:26
# @Author  : yang ke (jack_keyang@163.com)

from flask import Flask

app = Flask(__name__)

from views import *

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000,debug=True)