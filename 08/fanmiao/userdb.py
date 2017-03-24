#coding=utf-8

import MySQLdb as mysql
import time
import traceback

conn=mysql.connect(user='root',host='127.0.0.1',passwd='yy7943RMB',db='reboot10',charset='utf8')
conn.autocommit(True)
cur = conn.cursor()


fields= ['id', 'name', 'name_cn','password', 'email', 'mobile','role']

def validate_user(data):
	if not data["name"] or not data["password"] or not data["role"]:
		errmsg = 'name or password or role not null'
		return True,errmsg
	if data["password"] != data["repwd"]:
		errmsg = 'The two passwords you typed do not match'
		return True,errmsg
	else:
		errmsg="ok"
		return False,errmsg

def create_user(data):
	fields = ['name','name_cn','mobile','email','role','status','password','create_time']
	try:
		sql = 'INSERT INTO users (%s) VALUES (%s)' % (','.join(fields),','.join(['"%s"' % data[x] for x in fields]))
		cur.execute(sql)
		return True
	except:
		return Flase

def user_listone(condition):
	try:
		sql = "select %s from users where %s" %(','.join(fields),condition)
		cur.execute(sql)
		res = cur.fetchone()
		user=dict((k,res[i]) for i,k in enumerate(fields))
		return True,user
	except:
		errmsg = "get one failed"
		print traceback.print_exc()
		return False,errmsg

def user_list():
	users=[]
	try:
		sql = "select %s from users" % ','.join(fields)
		cur.execute(sql)
		result=cur.fetchall()
		users=[dict((k,row[i]) for i,k in enumerate(fields)) for row in result]
		return True,users
	except:
		errmsg = "select userlist failed"
		print traceback.print_exc()
		return False,errmsg

def update_user(data):
	conditions = ["%s='%s'" % (k,v[0]) for k,v in data.items()]
	sql = "update users set %s where id = %s" % (','.join(conditions),data['id'][0])
	cur.execute(sql)


def del_user(id):
	sql = "delete from users where id = %s" % id
	cur.execute(sql)



