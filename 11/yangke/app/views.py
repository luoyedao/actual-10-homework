#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template
from . import app

@app.route("/views")
def views():
    return "hello views"