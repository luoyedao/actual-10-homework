#coding:utf-8

from flask import Flask,request,render_template,redirect
import MySQLdb as mysql
import json 
import time
import traceback

conn=mysql.connect(user='root',host='127.0.0.1',passwd='123456',db='reboot10',charset='utf8')
conn.autocommit(True) 
cur = conn.cursor()


app = Flask(__name__)

# 注册，即添加用户,第一次请求获取注册页面，用GET请求，点击表单按钮提交用post方式，执行sql插入数据，注册成功
# 则跳转到个人信息页面，失败则在注册页面打印错误信息
@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        data =  {} 
        data["name"] = request.form.get('name',None)
        data["name_cn"] = request.form.get('name_cn',None)
        data["mobile"] = request.form.get('mobile',None)
        data["email"] = request.form.get('email',None)
        data["role"] = request.form.get('role',None)
        data["status"] = request.form.get('status',None)
        data["password"] = request.form.get('password',None)
        data["repwd"] = request.form.get('repwd',None)
        data["create_time"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        # data = request.form
        # data = request.get_json()
        print data
        fields = ['name','name_cn','mobile','email','role','status','password','create_time']
        if not data["name"] or not data["password"] or not data["role"]:
            errmsg = 'name or password or role not null'
            return render_template("register.html",result=errmsg)
            
        if data["password"] != data["repwd"]:
            # return  json.dumps('code':1,'errmsg':'The two passwords you typed do not match.'
            errmsg = 'The two passwords you typed do not match'
            return render_template("register.html",result=errmsg)
        try:
            sql = 'INSERT INTO users (%s) VALUES (%s)' % (','.join(fields), ','.join(['"%s"' % data[x] for x in fields]))
            cur.execute(sql)
            return redirect('/userinfo?name=%s' % data['name'])
        except:
            errmsg = "insert failed" 
            print traceback.print_exc()
            return render_template("register.html",result=errmsg)
    else:
        return render_template("register.html")

# 获取单个用户信息，注册成功传name作为where条件，查询这条数据，更新操作需要传id来获取数据，
@app.route('/userinfo')
def userinfo():
    where = {}
    where['id'] = request.args.get('id',None)
    where['name'] = request.args.get('name',None)
    if not where['id']  and not where['name']:
        errmsg  = "must hava a where"
        return render_template('index.html', result = errmsg )
    if where['id'] and not where['name']:
       condition = 'id = "%(id)s"' % where
    if where['name'] and not where['id']:
       condition = 'name = "%(name)s"' % where
    fields = ['id', 'name', 'name_cn', 'email', 'mobile'] 
    try:
        sql = "select %s from users where %s" % (','.join(fields),condition)
        cur.execute(sql)
        res = cur.fetchone()
        # user = {}
        # for i,k in enumerate(fields):    
        #    user[k]=res[i]   
        user = dict((k, res[i]) for i,k in enumerate(fields))  
        return  render_template('index.html', user = user)
    except:
        errmsg  = "get one failed"
        print traceback.print_exc()
        return  render_template("index.html",result=errmsg)
              
# 用户列表，生产环境中只有管理员才有这个权限，暂时不设置权限
@app.route('/userlist')
def userlist():
    users = []
    fields = ['id', 'name', 'name_cn', 'email', 'mobile'] 
    try:
        sql = "select %s from users" % ','.join(fields) 
        cur.execute(sql)
        result = cur.fetchall()
        # for row in result:
        #    user = {}
        #    for i, k in enumerate(fields):
        #        user[k] = row[i]
        #    users.append(user)    
        users = [dict((k, row[i]) for i,k in enumerate(fields)) for row in result]
        return  render_template('userlist.html', users = users)
    except:
        errmsg = "select userlist failed" 
        print traceback.print_exc()
        return  render_template("userlist.html",result=errmsg)
if __name__ ==   '__main__':
    app.run(host='0.0.0.0', port=9090,debug=True)
