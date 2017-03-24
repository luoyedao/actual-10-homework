#coding:utf-8
from flask import Flask

app = Flask(__name__)

app.secret_key = "jisldjlew"

import user,login,idc,cabinet,server
