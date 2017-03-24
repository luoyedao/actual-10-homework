#coding:utf-8

from flask import Flask,request,render_template,redirect
import MySQLdb as mysql
import json 
import time
import traceback

conn=mysql.connect(user='root',host='127.0.0.1',db='reboot10',charset='utf8')
#conn=mysql.connect(host='192.168.9.10',port=3306,user='admin',passwd='123.com',db='backstage',charset='utf8')
conn.autocommit(True) 
cur = conn.cursor()
app = Flask(__name__)

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method =='POST':
        '''
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
        print data
        '''
        print request.form
        data = dict(request.form)
        print data
        #fields = ['name','name_cn','mobile','email','role','status','password','create_time']
        conditions = ["%s='%s'" %(k,v[0]) for k,v in data.items()]
        print conditions
        #sql = 'INSERT INTO login (%s) VALUES (%s)' %(','.join(fields),','.join(['"%s"' %data[x] for x in fields]))
        sql = 'insert into login set %s'%','.join(conditions)
        print sql
        cur.execute(sql)
        return redirect('/userinfo?name=%s' %request.form.get('name'))
    else:
        return render_template("register.html")
@app.route('/userlist')
def userlist():
    users =[]
    fields = ['id', 'name', 'name_cn', 'email', 'mobile']
    try:
        sql="select %s from login" %','.join(fields)
        cur.execute(sql)
        result = cur.fetchall()
        for row in result:
            #user ={}
            #for i,k in enumerate(fields):
                #print i;
            #    user[k] = row[i]
            #print user  
            #users.append(user)
            users=[dict((k,row[i]) for i,k in enumerate(fields)) for row in result]
        return render_template('userlist.html',users=users)
    except:
        errmsg = "select userlist failed"
        print traceback.print_exc()
        return render_template("userlist.html",result=errmsg)

@app.route('/userinfo')
def userinfo():
    where ={}
    where['name']=request.args.get('name',None)
    if not where ['name']:
        errmsg = "nust hava a where"
        return render_template('index.html',result = errmsg)
    if where['name']:
        condition = "name ='%(name)s'" % where
    fields = ['id', 'name', 'name_cn', 'email', 'mobile']
    try:
        sql = "select %s from login where %s" %(','.join(fields),condition)
        print sql
        cur.execute(sql)
        res = cur.fetchone()
        user = {}
        for i,k in enumerate(fields):
            user[k]=res[i]
        #user=[dict((k,row[i]) for i,k in enumerate(fields)) for row in result]
        return render_template('index.html',user = user)
    except:
        errmsg = "get one failed"
        print traceback.print_exc()
        return render_template("index.html",result=errmsg)
@app.route('/update',methods=['GET','POST'])
def update():
    if request.method =="POST":
        print request.form
        data = dict(request.form)
        print data
        conditions = ["%s='%s'" %(k,v[0]) for k,v in data.items()]
        print conditions
        sql ="update login set %s where id =%s" %(','.join(conditions),data['id'][0])
        print sql
        cur.execute(sql)
        return redirect('/userlist')
    else:
        id = request.args.get('id',None)
        if not id:
            errmsg = "must hava id"
            return render_template("update.html",result=errmsg)
        fields = ['id', 'name', 'name_cn', 'email', 'mobile']
        try:
            sql = "select %s from login where id = %s" % (','.join(fields),id)
            cur.execute(sql)
            res = cur.fetchone()
            user = {}
            for i,k in enumerate(fields):
                user[k]=res[i]
            return render_template('update.html',user=user)
        except:
            errmsg = "get one failed"
            print traceback.print_exc()
            return render_template("update.html",result=errmsg)
@app.route('/update_password',methods=['GET','POST'])
def update_password():
    if request.method =='POST':
        userdict=dict(request.form)
        if userdict['password'][0] ==userdict['password_rep'][0]:
            print userdict['password'][0];print userdict['password_rep'][0];
            password=["%s='%s'" %(k,v[0]) for k,v in userdict.items()][2]
            print password
            try:
                sql ="update login set %s where id=%s" %(password,userdict['id'][0])
                print sql
                cur.execute(sql)
                return redirect('/userlist')
            except:
                errmsg = "error password"
                print traceback.print_exc()
                return render_template("userlist.html",result=errmsg)
    else:
        id = request.args.get('id',None)
        if not id:
            errmsg ='must have id'
            return render_template("update_password.html",result=errmsg)
        fields = ['id','name']
        try:
            sql = "select %s from login where id = %s" % (','.join(fields),id)
            cur.execute(sql)
            res = cur.fetchone()
            user = {}
            for i,k in enumerate(fields):
                user[k]=res[i]
            return render_template('update_password.html',user=user)
        except:
            errmsg = "get one failed"
            print traceback.print_exc()
            return render_template("update_password.html",result=errmsg)
@app.route('/delete',methods=['GET'])
def delete():
    id = request.args.get('id',None)
    if not id:
        errmsg = "must hava id"
        return render_templeate("userlist.html",result=errmsg)
    try:
        sql = "delete from login where id= %s" %id
        cur.execute(sql)
        return redirect('/userlist')
    except:
        errmsg="delete failde"
        return render_template("userlist.html",result=errmsg)




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9292,debug=True)
