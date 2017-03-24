#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)
app.secret_key = "dfahiu2jf"
salt = "jack"

import login,admin,server,idc,cabinet

