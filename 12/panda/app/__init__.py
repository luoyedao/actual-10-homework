#coding:utf-8
from flask import Flask


app = Flask(__name__)

app.secret_key = "UIsadl;oi3&*(&9023sd"

import login
import demo
import idc
import cabinet
import server
import mem
import log
