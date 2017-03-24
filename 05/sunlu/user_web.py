# coding=utf-8
# !/usr/bin/env python
from flask import Flask, request, render_template, redirect
import files

app = Flask(__name__)


@app.route('/add')
def test():
    username = request.args.get('username')
    password = request.args.get('password')
    if username in files.get_file().keys():
        return redirect('/')
    else:
        files.write_file(username, password)
        return redirect('/')


@app.route('/')
def index():
    d = files.get_file()
    return render_template('index.html', d=d)


@app.route('/adduser')
def adduser():
    username = request.args.get('username')
    password = request.args.get('password')
    if username in files.get_file().keys():
        return redirect('/')
    else:
        files.write_file(username, password)
        return redirect('/')


@app.route('/deluser')
def deluser():
    username = request.args.get('username')
    if username in files.get_file().keys():
        files.del_file(username)
        return redirect('/')
    else:
        return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)

