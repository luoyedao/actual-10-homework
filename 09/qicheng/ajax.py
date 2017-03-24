#coding:utf-8

from flask import Flask,request,render_template
import json
app = Flask(__name__)



# 获取单个用户信息，注册成功传name作为where条件,查询这条数据渲染主页
@app.route('/')
@app.route('/index')
def index():
    return render_template('ajax.html')
@app.route('/list')
def list():
    user = {'id':1,'name':'wd','age':18}
    return json.dumps({'code':0,'result':user})


@app.route('/add',methods=['GET','POST'])
def add():
        data = dict((k,v[0]) for k,v in dict(request.form).items())
        # print data
        return json.dumps({'code':0,'result':data})
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9092,debug=True)
