#!/bin/env python
# encoding:utf-8

from flask import Flask,render_template,request,redirect
import sys,pickle
import MySQLdb as mysql
import traceback
import time

app=Flask(__name__)

conn=mysql.connect(host='192.168.16.237',user='root',passwd='zdsoft',db='reboot10',charset='utf8')
cur=conn.cursor()
conn.autocommit(True)


@app.route('/')
def index():
        return render_template('index.html')

@app.route('/userinfo')
def userinfo():
        where={}
        where['id']=request.args.get('id',None)
        where['name']=request.args.get('name',None)
        if not where['id'] and not where['name']:
                errmsg='must have a where'
                return render_template('info.html',result=errmsg)
        if where['id'] and not where['name']:
                condition='id = "%(id)s"'%where
        if where['name'] and not where['id']:
                condition='name = "%(name)s"'%where
        fileds=['id','name','name_cn','email','mobile']
        try:
                sql='select %s from users where %s'%(','.join(fileds),condition)
                cur.execute(sql)
                res=cur.fetchone()
                user=dict((k,res[i]) for i,k in enumerate(fileds))
                return render_template('info.html',user=user)
        except:
                errmsg='get one failed'
                print traceback.print_exc()
                return render_template('info.html',result=errmsg)

@app.route('/login',methods=['GET','POST'])
def login():
        if request.method=='POST':
                name=request.form.get('name')
                pwd=request.form.get('pwd')
                fileds=['name','name_cn','password','email','role','status','mobile']
                sql='select %s from users'%','.join(fileds)
                cur.execute(sql)
                res=cur.fetchall()
                li=[dict((k,row[i]) for i,k in enumerate(fileds)) for row in res]
                for line in li:
                        if name==line['name'] and pwd==line['password']:
                                return redirect('/userinfo?name=%s'%name)
                return redirect('/login')
        else:
                return render_template('login.html')

@app.route('/register',methods=['GET','POST'])
def reg():
        if request.method=='POST':
                data=dict(request.form)
                data['create_time']=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
                fileds=['name','name_cn','mobile','email','role','status','password','create_time']
                if not data['name'] or not data['password'] or not data['role']:
                        errmsg='name or password or role not null'
                        return render_template('register.html',result=errmsg)
                if data['password']!=data['repwd']:
                        errmsg='The two password do not match'
                        return render_template('register.html',result=errmsg)
                try:
                        sql='insert into users(%s) values(%s)'%(','.join(fileds),','.join(['"%s"'%data[x][0] for x in fileds]))
                        cur.execute(sql)
                        return redirect('/userinfo?name=%s'%data['name'][0])
                except:
                        errmsg='inser failed'
                        print traceback.print_exc()
                        return render_template('register.html',result=errmsg)
        else:
                return render_template('register.html')

@app.route('/userlist')
def userlist():
        fileds=['id','name','name_cn','email','mobile']
        sql='select %s from users'%','.join(fileds)
        cur.execute(sql)
        res=cur.fetchall()
        users=[dict((k,row[i]) for i,k in enumerate(fileds)) for row in res]
        return render_template('userlist.html',users=users)

@app.route('/update',methods=['GET','POST'])
def update():
        if request.method=='POST':
                data=dict(request.form)
                conditions=["%s='%s'"%(k,v[0]) for k,v in data.items()]
                sql='update users set %s where id=%s'%(','.join(conditions),data['id'][0])
                cur.execute(sql)
                return redirect('/userlist')
        else:
                id=request.args.get('id',None)
                if not id:
                        errmsg='must have id'
                        return render_template('update.html',result=errmsg)
                fileds=['id','name','name_cn','email','mobile']
                try:
                        sql='select %s from users where id=%s'%(','.join(fileds),id)
                        cur.execute(sql)
                        res=cur.fetchone()
                        user=dict((k,res[i]) for i,k in enumerate(fileds))
                        return render_template('update.html',user=user)
                except:
                        errmsg='get one failed'
                        print traceback.print_exc()
                        return render_template('update.html',result=errmsg)

@app.route('/delete',methods=['GET','POST'])
def delete():
        id=request.args.get('id',None)
        if not id:
                errmsg='must have id'
                return render_template('update.html',result=errmsg)
        sql='delete from users where id=%s'%id
        cur.execute(sql)
        return redirect('/userlist')




if __name__=='__main__':
        app.run(host='192.168.16.237',port=9898 ,debug='Treu')
