#!/usr/bin/env python
# -*- coding:utf-8 -*-
#__author__ = 'Madon'
from flask import Flask

app=Flask(__name__)

app.secret_key="sdfsajfkjslf"

from demo import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9292,debug=True)
