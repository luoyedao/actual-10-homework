#!/usr/bin/env python
from flask import Flask,render_template,request,redirect
import db
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == "POST":
	name = request.form.get('name')
	password = request.form.get('password')
	if db.check_login_name(name) == True:
	    if db.get_by_name(name)['password'] == password:
		return render_template('login.html', info='login ok !!!')
	    else:
		return render_template('login.html', info='password error')
	else:
            return render_template('login.html', info='user not fond')
    else:
	return render_template('login.html')

@app.route('/admin/', methods=['GET','POST'])
def userlist():
    if request.method == "POST":
        queryuser = db.get_by_name(request.form.get('name'))
	return render_template('admin.html',users=db.get_by_all(),queryinfo=queryuser)
    else:
	queryuser = db.get_by_name(request.form.get('name'))
        return render_template('admin.html',users=db.get_by_all(),queryinfo=queryuser)

@app.route('/admin/adduser/', methods=['GET','POST'])
def adduser():
    if request.method == "POST":
	userdict = dict(request.form)
	print userdict
	db.add_set_user(','.join(['"%s"' % (v[0]) for k,v in userdict.items()]))
        return render_template('adduser.html', info='Users to add to complete')
    else:
	return render_template('adduser.html')

@app.route('/admin/delete/')
def delete():
    db.del_by_id(request.args.get('id'))
    return redirect('/admin')

@app.route('/update', methods=['GET','POST'])
def update():
    if request.method == "POST":
	userdict = dict(request.form)
	userlist = ["%s='%s'" % (k,v[0]) for k,v in userdict.items()]
	db.update_user_data(','.join(userlist),userdict['id'][0])
        return redirect('/admin')
    else:
	return render_template('update.html',user=db.get_by_id(request.args.get('id')))

@app.route('/update/chagepasswd/', methods=['GET','POST'])
def chagepasswd():
    if request.method == "POST":
	userdict = dict(request.form)
	if userdict['def_passwd'][0] == db.get_by_id(request.form.get('id'))['password']:
            if userdict['rep_passwd'][0] == userdict['password'][0]:
		new_password = ["%s='%s'" % (k,v[0]) for k,v in userdict.items()][1]
		db.update_user_data(new_password,userdict['id'][0])
	    else:
                return render_template('chage_passwd.html',user=db.get_by_id(request.form.get('id')),info='Two different Password')
	else:
	    return render_template('chage_passwd.html',user=db.get_by_id(request.form.get('id')),info='error password!')
        return render_template('chage_passwd.html',user=db.get_by_id(request.form.get('id')),info='chage complete!!!')
    else:
	return render_template('chage_passwd.html',user=db.get_by_id(request.args.get('id')))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)
