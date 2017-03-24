from flask import Flask, redirect, render_template
import MySQLdb as mysql

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/userlist/')
def userlist():
    sql = "select name,name_cn,email,mobile from users"
    cur.execute(sql)
    result = cur.fetchall()
    return render_template('userlist.html', users=result)


if __name__ == '__main__':
    app.run(debug=True)
