#!/usr/bin/env python
#coding:utf-8

from flask import Flask

app = Flask(__name__)
app.secret_key='!s\xa3-\xafle6\xe2=\xfa3'

import users,idc,cabinet,server
