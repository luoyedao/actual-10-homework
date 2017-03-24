#!/usr/bin/python
#coding:utf-8

from flask import Flask,render_template,request
import file

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='GET':
        return render_template('login.html')
    else:
 	name = request.form.get('name')
 	password = request.form.get('password')

	d = {}
        for i in file.userlist():
	    d[i['name']] = i['password']
	if name=='admin' and d[name]==password:
	    return render_template('userlist.html',users = file.userlist())
	elif name in d and d[name]==password:
	    return render_template('userone.html',user = file.userlist(name))
	else:
	    return render_template('error.html')

@app.route('/listone',methods=['POST'])
def listone():
    name = request.form.get('name')
    return render_template('listone.html',user = file.userlist(name))

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='GET':
	return render_template('register.html')
    else:
        name = request.form.get('name')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        name_cn = request.form.get('name_cn')
        email = request.form.get('email')
        mobile = request.form.get('mobile')
        role = request.form.get('role')
        status = request.form.get('status')

        for i in file.userlist():
	    if name!=i['name'] and password==repassword:
		fields = [name,name_cn,password,email,mobile,role,status]
		file.register(*fields)
		return render_template('register_ok.html')
	    else:
		return render_template('error.html')

@app.route('/delete')
def delete():
    id = request.args.get('userid')
    file.deluser(id)
    return render_template('userlist.html',users = file.userlist())


@app.route('/updateone',methods=['GET','POST'])
def updateone():
    if request.method=='GET':
        id = request.args.get('userid')
	return render_template('updateone.html',user = file.update_list(id))
    else:
        id = request.form.get('userid')
	
        name = request.form.get('name')
        name_cn = request.form.get('name_cn')
        password = request.form.get('password')
        email = request.form.get('email')
        mobile = request.form.get('mobile')
        role = request.form.get('role')
        status = request.form.get('status')

        fields = [name_cn,password,email,mobile,role,status,id]
        file.update(*fields)
	return render_template('userone.html',user = file.update_list(id))

@app.route('/update',methods=['GET','POST'])
def update():
    if request.method=='GET':
        id = request.args.get('userid')
	return render_template('update.html',user = file.update_list(id))
    else:
        id = request.form.get('userid')
	
        name = request.form.get('name')
        name_cn = request.form.get('name_cn')
        password = request.form.get('password')
        email = request.form.get('email')
        mobile = request.form.get('mobile')
        role = request.form.get('role')
        status = request.form.get('status')
	
        fields = [name_cn,password,email,mobile,role,status,id]
        file.update(*fields)
        return render_template('userlist.html',users = file.userlist())

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8888,debug=True)
    
