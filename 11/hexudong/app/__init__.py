#coding:utf-8
from flask import Flask


app = Flask(__name__)

app.secret_key = "UIsadl;oi3&*(&9023sd"

import demo,login,idc,server,cabinet
