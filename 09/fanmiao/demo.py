#coding:utf-8

from flask import Flask,request,render_template,redirect,session
import json 
import time
import traceback
from userdb import validate_user,create_user,user_listone,user_list,update_user,del_user,change_passwd

app = Flask(__name__)
app.secret_key="sdasdasdasd"
@app.route('/register',methods=['GET','POST'])

def register():
#	if not session.get('name',None):
#		return redirect('/login')
	if request.method == 'POST':
		res =dict(request.form)
		data=dict([i,k[0]] for i,k in res.items())
		data["create_time"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) 
		#判断账号密码是否为空
		validate_result,errmsg=validate_user(data)
		if validate_result:	
			return render_template("register.html",result=errmsg)
		
		if create_user(data):
			return redirect('/userinfo?name=%s' % data['name'])
		else:
			errmsg = "insert failed"
			print traceback.print_exc()
			return render_template("register.html",result=errmsg)
	else:
		return render_template("register.html")

@app.route('/userinfo')
def userinfo():
	if not session.get('name',None):
		return redirect('/login')
	where = {}
	where['id'] = request.args.get('id',None)
	where['name'] = request.args.get('name',None)
	if not where['id'] and not where ['name']:
		errmsg = "must have a where"
		return render_template('userlistone.html',result = errmsg)
	if where['id'] and not where['name']:
		condition = 'where id = "%(id)s"' % where
	if where['name'] and not where['id']:
		condition = 'name = "%(name)s"' % where
	#数据库查询数据
	userlist_result,userlist_data=user_listone(condition)
	print userlist_result
	if userlist_result:
		return render_template('userlistone.html',user=userlist_data)
	#else:
	#	return render_template('index.html',result=userlist_data)


@app.route('/userlist')
def userlist():
	if not session.get('name',None):
		return redirect('/login')
	userlist_result,users=user_list()
	if userlist_result:
		return  render_template('userlist.html', users = users)
	else:
		errmsg = "select userlist failed"
                print traceback.print_exc()
                return  render_template("userlist.html",result=errmsg)

@app.route('/update',methods=['GET','POST'])
def update():
	if not session.get('name',None):
		return redirect('/login')
	if request.method=="POST":
		data=dict(request.form)
		update_user(data)
		return redirect('/userlist')
	else:
		id = request.args.get('id',None)
		if not id:
			errmsg = "must hava id"
			return render_template("update.html",result=errmsg)
		condition = 'id = "%s"' % id
		userlist_result,user=user_listone(condition)
		if userlist_result:
			return render_template('update.html',user=user)


@app.route('/delete',methods=['GET'])
def delete():
	if not session.get('name',None):
                return redirect('/login')
	id = request.args.get('id',None)
        if not id:
                errmsg="must have id"
                return render_template("userlist.html",result=errmsg)
        try:
		del_user(id)        
		return redirect('/userlist')
        except:
                errmsg="delete failed"
                return render_template("userlist.html",result=errmsg)

@app.route('/login',methods=['GET','POST'])
def login():
        if request.method=='POST':
                data = dict((k,v[0]) for k,v in dict(request.form).items())
                if not data.get('name',None) or not data.get('password',None):
                        errmsg="name or password not null"
                
		condition = 'name = "%(name)s"' % data
		userlist_result,user=user_listone(condition)
		#print userlist_result,user
		if not userlist_result:
                        errmsg="%s is not exist" % data['name']
                        return json.dumps({'code':'1','errmsg':errmsg})
                if user['password'] != data['password']:
                        errmsg="name or password is wrong"
                        return json.dumps({'code':'1','errmsg':errmsg})
                else:
                        session['name'] = data['name']
			role=user['role']
			username=user['name']
                        return json.dumps({'code':'0','result':"login sucess",'role':role,'name':username})
                        #return json.dumps({'code':'0','result':"login sucess"})

        else:
                return render_template('login.html')

@app.route('/change-password',methods=['POST'])
def change_password():
	uid = request.form.get('userid')
	user_password = request.form.get('user-password')
	change_passwd(uid,user_password)
	return json.dumps({'status':'ok'})


@app.route('/loginout')
def loginout():
	session.pop('name')
	return redirect('/login')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9001,debug=True)  

