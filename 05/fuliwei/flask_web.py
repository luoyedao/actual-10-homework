#!/usr/bin/python 
#coding:utf-8

from flask import Flask ,request ,url_for ,render_template
from do_file import get_Users,add_user,del_Users
app = Flask(__name__) 

#获取网页参数中的用户名和密码
def getMes():
	username = request.args.get("username","None")
	password = request.args.get("password","None")
	return {username:password}

@app.route("/zhuce")
def zhuce():
	word = request.args
	print word ," ***" ,type(word)
	print "-"*40
	len_word = len(request.args)
	if len_word == 2 :
		username = request.args.get("username","None")
		password = request.args.get("password","None")
		print username ,password
		print "-"*40
		all_user = get_Users("users.txt")
		print all_user
		print "-"*40
		if username in all_user.keys():
			return render_template("zhuce.html",messege="exist",p_dict=all_user)
		else:
			mes = add_user("users.txt",username,password)
			return render_template("zhuce.html",messege="{} zhuce  success".format(username),p_dict=mes)                                                     
	else :
		return render_template("zhuce.html",messege="Unknown Options" ,p_dict = {})

@app.route("/login")
def loginIn():
	x = getMes()
	print x 
	all_user = get_Users("users.txt") 
	lock_user = get_Users("lock.txt")
	for k ,v in x.items():
		if k in lock_user.keys():
			return render_template("lock.html",messege="{} is locked  ".format(k),p_dict=lock_user) 
		if k in all_user.keys():
			if  all_user[k] == v:
				return render_template("login.html",messege="{} is login in Successed ".format(k),p_dict=all_user)   
			else :
				return render_template("login.html",messege="Password  is wrong ",p_dict=all_user)
		else :
			return render_template("login.html",messege="{} is not exist".format(k),p_dict=all_user)

@app.route("/del")
def userDel():
#	del_user = getMes()
	k = request.args.get("username","None")
	all_user = get_Users("users.txt")
#	for k,v in del_user.items():
#		print k ,v 
	if k in all_user.keys():
		del all_user[k]
		del_Users("users.txt",all_user)
		return render_template("delUser.html",p_dict=all_user,messege=" {} has been deleted ".format(k))	
	else:
		return render_template("delUser.html",p_dict=all_user,messege="{} is not exist ".format(k))



@app.route("/newpassword") # 更新密码
def ChangePassword():
	username = request.args.get("username","None")
	password = request.args.get("password","None")
	firstnew = request.args.get("firstnew","None")
	secondnew = request.args.get("secondnew","None")
#	print username ,"***111***" ,password ,"**222***" ,firstnew ,"***333***" ,secondnew 
	all_user = get_Users("users.txt")
	lock_user = get_Users("lock.txt")
	if username in lock_user.keys():
		return render_template("lock.html",messege="{} is locked  ".format(username),p_dict=lock_user) 
	if username in all_user.keys():
		if password == all_user[username] and firstnew == secondnew :
			all_user[username] = firstnew
			del_Users("users.txt",all_user)
			return render_template("newpassword.html",messege="Changed Success",p_dict = all_user)
		elif password == all_user[username] and firstnew != secondnew :
			return render_template("newpassword.html",messege="Passwords are not consistent",p_dict = all_user)
		else :
			return render_template("newpassword.html",messege="Wrong password",p_dict = all_user)
	else :
		return render_template("newpassword.html",messege="The username is not exist",p_dict = all_user)
if __name__ == "__main__":
	app.run(host="0.0.0.0",port=1000,debug=True)
