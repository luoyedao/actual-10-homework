#!/usr/bin/env python
#coding=utf-8

from flask import Flask,request,render_template,redirect
import MySQLdb as mysql
import time
import traceback
import json

conn=mysql.connect(host='localhost',user='root',passwd='123',db='reboot10',unix_socket='/app/mysql/data/mysql.sock',charset='utf8')
cur=conn.cursor()
app=Flask(__name__)

def usernames():
  cur.execute('select name from users')
  users=cur.fetchall()
  uinfo=[]
  for i in users:
    uinfo.append(i[0])
  return uinfo 

@app.route('/')
def usermgr():
  return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
  if request.method == 'POST':
    user=request.form.get('user')
    passwd=request.form.get('pass')
    if not user:
      errmsg = 'please input username..'
      return render_template('login.html',result=errmsg)
    if user in usernames():
      sql='select password from users where name="%s"'%(user)
      cur.execute(sql)
      passre=cur.fetchone()
      if passwd in passre:
        return redirect('/userinfo?name=%s' %(user))
      else:
        errmsg = 'password not true...'
        return render_template('login.html',result=errmsg)
    else: 
      errmsg = '%s not exist..please create it' %(user)
      return render_template('login.html',result=errmsg)
  else:
    return render_template('login.html')

@app.route('/userinfo')
def userinfo():
  uid = {}
  uid['id'] = request.args.get('id',None)
  uid['name'] = request.args.get('name',None)
  if not uid['id'] and not uid['name']:
    return redirect('/login')
  if uid['id'] and not uid['name']:
    condition = 'id="%(id)s"' % uid
  if uid['name'] and not uid['id']:
    condition = 'name="%(name)s"' % uid
  if uid['name'] == 'Admin':
    return redirect('/userlist?name=Admin')
  fields=['id','name','name_cn','email','mobile','role','status']
  print condition
  sql='select %s from users where %s' %(','.join(fields),condition)
  print sql
  cur.execute(sql)
  result=cur.fetchone()
  uinfo={}
  for i,k in enumerate(fields):
    uinfo[k]=result[i]
  print uinfo
  return render_template('userinfo.html',user=uinfo)

@app.route('/oneuser')
def oneuser():
  name=request.args.get('user')
  field="name,name_cn,password,email,mobile,role,status"
  if not name:
    return redirect('/userlist') 
  sql='select %s from users where name="%s"' %(field,name)
  cur.execute(sql)
  result=cur.fetchall()
  return render_template('userlist.html',users=result)

@app.route('/userlist')
def userlist():
  fields=['id','name','name_cn','email','mobile','role','status']
  sql='select %s from users' %(','.join(fields))
  print sql
  cur.execute(sql)
  result=cur.fetchall()
  return render_template('userlist.html',users=result)

@app.route('/register',methods=['GET','POST'])
def register():
  if request.method == 'POST':
    reginfo={}
    reginfo["name"]=request.form.get('name',None)
    reginfo["name_cn"]=request.form.get('name_cn',None)
    reginfo["password"]=request.form.get('passwd',None)
    reginfo["passre"]=request.form.get('passre',None)
    reginfo["email"]=request.form.get('email',None)
    reginfo["mobile"]=request.form.get('mobile',None)
    reginfo["role"]=request.form.get('role',None)
    reginfo["status"]=request.form.get('status',None)
    reginfo["create_time"]=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print reginfo
    fields=['name','name_cn','password','email','mobile','role','status','create_time']
    if not reginfo["name"] or not reginfo["password"] or not reginfo["email"]:
      errmsg = 'please input username,password,email at least!'
      return render_template("register.html",result=errmsg)     
    if reginfo["password"] != reginfo["passre"]:
      errmsg = 'password not match,please retry input'
      return render_template("register.html",result=errmsg)     
    try:
      sql='insert into users(%s) values (%s)' %(','.join(fields),','.join(['"%s"' % reginfo[x] for x in fields]))
      cur.execute(sql)
      conn.commit()
      info = '%s register seccess,now you can return login!!!'% reginfo["name"]
      return render_template("register.html",result=info)
    except:
      errmsg = 'register failed'
      print traceback.print_exc()
      return render_template("register.html",result=errmsg)     
  else:
    return render_template('register.html')

@app.route('/update',methods=['GET','POST'])
def update():
  userid=request.args.get('id')
  if request.method == 'POST':
    userdata=dict(request.form)
    userdata.pop('update')
    condition=[ '%s="%s"' %(k,v[0]) for k,v in userdata.items() ]
    uid=userdata["id"][0]
    sql='update users set %s where id=%s'%(','.join(condition),uid)
    print sql
    cur.execute(sql)
    conn.commit()
    return redirect('/userinfo?id=%s'%(uid))
  else:
    fields=['id','name','name_cn','email','mobile','role','status']
    sql='select %s from users where id=%s' %(','.join(fields),userid)
    cur.execute(sql)
    user=cur.fetchone()
    uinfo={}
    for i,k in enumerate(fields):
      uinfo[k]=user[i]
    return render_template('update.html',user=uinfo)

@app.route('/deluser')
def deluser():
  uid=request.args.get('id')
  sql='delete from users where id="%s"' %(uid)
  cur.execute(sql)
  conn.commit()
  return redirect('/userlist')

if __name__ == '__main__':
  app.run(host='0.0.0.0',port=1000,debug=True)

