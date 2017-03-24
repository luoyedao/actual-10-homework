from flask import render_template
from . import app

@app.route('/idc/')
def idc():
    return render_template('idc.html')


@app.route('/idcadd/')
def idcadd():
    return render_template('idcadd.html')


@app.route('/cabinet/')
def cabinet():
    return render_template('cabinet.html')


@app.route('/server/')
def server():
    return render_template('server.html')


