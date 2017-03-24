#coding:utf-8

from flask import Flask,request,render_template,redirect,session
import MySQLdb as mysql
import json 
import time
import traceback
import sys

conn=mysql.connect(user='root',host='127.0.0.1',passwd='123456',db='reboot10',charset='utf8')
conn.autocommit(True) 
cur = conn.cursor()


app = Flask(__name__)
app.secret_key="dsadfasdfasdf"

# 注册，即添加用户,第一次请求获取注册页面，用GET请求，点击表单按钮提交用post方式，执行sql插入数据，注册成功
# 则跳转到个人信息页面，失败则在注册页面打印错误信息
@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        data = request.form
        data = dict(request.form)
        data = dict((k,v[0]) for k,v in data.items())
        data["create_time"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        fields = ['name','name_cn','mobile','email','role','status','password','create_time']
        if not data["name"] or not data["password"] or not data["role"]:
            errmsg = 'name or password or role not null'
            return render_template("register.html",result=errmsg)
            
        if data["password"] != data["repwd"]:
            errmsg = 'The two passwords you typed do not match'
            return render_template("register.html",result=errmsg)
        try:
            sql = 'INSERT INTO users (%s) VALUES (%s)' % (','.join(fields), ','.join(['"%s"' % data[x] for x in fields]))
            cur.execute(sql)
            return redirect('/userlist')
        except:
            errmsg = "insert failed" 
            print traceback.print_exc()
            return render_template("register.html",result=errmsg)
    else:
        return render_template("register.html")

# 用户列表，生产环境中只有管理员才有这个权限，暂时不设置权限
@app.route('/userlist')
def userlist():
    if not session.get('name',None):
        return redirect('/login') 
    users = []
    fields = ["id","name","name_cn","email","mobile","role","status"]
    # print users.status
    # print users
    try:
        sql = "select %s from users" % ','.join(fields) 
        cur.execute(sql)
        result = cur.fetchall()
        users = [dict((k, row[i]) for i,k in enumerate(fields)) for row in result]
        print users
        return  render_template('userlist.html', users = users)
    except:
        errmsg = "select userlist failed" 
        print traceback.print_exc()
        return  render_template("userlist.html",result=errmsg)

# 获取单个用户信息，注册成功传name作为where条件,查询这条数据渲染主页
@app.route('/')
@app.route('/index')
def index():
    if not session.get('name',None):
        return redirect('/login') 
    # name = request.args.get('name',None)
    name = session['name']
    fields = ['id', 'name', 'name_cn', 'email', 'mobile'] 
    try:
        sql  = 'select %s from users where name="%s"' % (','.join(fields),name)
        cur.execute(sql)
        res = cur.fetchone()
        user = {}
        user = dict((k, res[i]) for i,k in enumerate(fields))  
        return  render_template('index.html', user = user)
    except:
        errmsg  = "get  one failed"
        print traceback.print_exc()
        return render_template("index.html",result=errmsg)

@app.route('/getbyid')
def getbyid():
    if not session.get('name',None):
        return redirect('/login') 
    id = request.args.get('id') 
    if not id:
         return json.dumps({"code":1,'errmsg':"must hava a condition"}) 
    condition = 'id="%s"' % id 
    fields = ['id', 'name', 'name_cn', 'email', 'mobile','role','status'] 
    try: 
        sql  = "select %s from users where %s" % (','.join(fields),condition)
        cur.execute(sql)
        res = cur.fetchone()
        user = {}
        user = dict((k, res[i]) for i,k in enumerate(fields))  
        return json.dumps({"code":0,'result':user}) 
    except:
        print traceback.print_exc()
        return json.dumps({"code":1,'errmsg':"select userinfo failed"}) 

# 更新操作，两步 1：get请求显示更新页面并获取要更新数据的信息，2：点击按钮POST请求，执行sql完成更新，成功
# 跳转userlist页面，否则在更新页面输出错误信息。生产环境分两个场景，个人修改自己的信息， 管理员可以更新所
# 有人，暂且不分
@app.route('/update',methods=['GET','POST'])
def update():
     if not session.get('name',None):
        return redirect('/login') 
     if request.method == 'POST':
        data = dict(request.form)
        data = dict((k,v[0]) for k,v in data.items())
        print data                  
        conditions = ["%s='%s'" %  (k,v) for k,v in data.items()]
        try:
            sql = "update users set %s where id = %s" % (','.join(conditions),data['id'])
            cur.execute(sql)
            return json.dumps({"code":0,'result':"update success"})
        except:
            print traceback.print_exc()
            return json.dumps({"code":1 ,'result':"update failed"}) 
     else:
         uid = request.args.get('id')
         return render_template('update.html',uid=uid)

# 删除，只有传入一个id作为where条件即可，删除成功挑战userlist，生产环境中管理员才有权限，本课暂不区分
@app.route('/delete',methods=['GET'])
def delete():
    if not session.get('name',None):
        return redirect('/login') 
    id = request.args.get('id',None)
    if not id:
          errmsg = "must hava id" 
          return render_template("userlist.html",result=errmsg)
    try: 
        sql = "delete from users where id = %s" % id
        cur.execute(sql)
        return redirect('/userlist')
    except:
        errmsg = "delete failed" 
        return render_template("userlist.html",result=errmsg)


# 登录页面，太简单，不写了
@app.route('/login',methods=['GET','POST'])
def login():
     if request.method == "POST":
        data = dict((k,v[0]) for k,v in dict(request.form).items())
        if not  data.get('name',None) or  not data.get('password',None):
            errmsg="name or password not null"
            # return render_template('login.html',result=errmsg)
            return json.dumps({'code':'1','errmsg':errmsg})

        fields=['name','password','role']                
        sql = 'select %s from users where name = "%s"' % (','.join(fields),data['name'])
        cur.execute(sql)
        res = cur.fetchone()  
        if not res:   # 如果这个用户在数据中不存在，返回的结果就是res = (())
            errmsg="%s is not exist" % data['name']
            #return render_template('login.html',result=errmsg)
            return json.dumps({'code':'1','errmsg':errmsg})
        user = {}
        user = dict((k, res[i]) for i,k in enumerate(fields)) #{'name':'wd','password':'sdsds'}
        if user['password'] != data['password']:  
            errmsg="password is wrong"
            #return render_template('login.html',result=errmsg)
            return json.dumps({'code':'1','errmsg':errmsg})
    
        session['name'] = user['name']
        session['role'] = user['role']
        return redirect('/userlist')
        return json.dumps({'code':'0','result':"login sucess"})
            
     else:
        return render_template('login.html')

# @app.route('/users',methods=['GET','POST'])
# def users():
#     return render_template("moban.html",result=errmsg)


@app.route('/loginout')
def loginout():
    session.pop('name')
    session.pop('role')
    return redirect('/login')

    

        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9092,debug=True)
