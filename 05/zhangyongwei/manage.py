#coding: utf-8
from flask import Flask, request, render_template, redirect
import db

app = Flask(__name__)


@app.route('/')
def index():
    return redirect('/login/')

@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/login_required/', methods=['GET'])
def login_required():
    username = request.args.get('username')
    password = request.args.get('password')
    return db.login_required(username, password)

@app.route('/regedit/')
def regedit():
    return render_template('add_user.html')

@app.route('/add_user/', methods=['GET'])
def add_user():
    username = request.args.get('username')
    password = request.args.get('password')
    return db.add_user(username, password)

@app.route('/users/')
def users():
    users = db.uesrs()
    return render_template('users.html', users=users)

@app.route('/delete_user/')
def delete_users():
    username = request.args.get('username')
    db.delete_users(username)
    return redirect('/users/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)