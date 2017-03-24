#!/usr/bin/env python
#@The author: toby (15915822634@139.com)
#@Date: 2016-08-09
import MySQLdb
conn= MySQLdb.connect(host='localhost', port = 3306, user='root', passwd='1qaz#EDC', db ='reboot10',)
cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)

class Updateuser:
    def __init__(self):
	pass
    def setuserinfo(self,username,username_cn,passwords,emails,mobiles,roles,userid):
	if userid:
            sql_updatename = "update users set name='%s',name_cn='%s',password='%s',email='%s',mobile='%s',role='%s' where id='%s'" % (username,username_cn,passwords,emails,mobiles,roles,userid)
            cur.execute(sql_updatename)
            conn.commit()
	    return True
	else:
	    return False
    def chagepasswd(self,username,passwd):
	sql_chagepasswd = "update users set password='%s' where name='%s'" % (passwd,username)
	cur.execute(sql_chagepasswd)
        conn.commit()

def adduser(name,name_cn,password,email,mobile,role):
    cur.execute("insert into users (name,name_cn,password,email,mobile,role,status,create_time,last_time) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)", (name,name_cn,password,email,mobile,role,"1",20160812,"20160812"))
    conn.commit()

def getuser():
    cur.execute("select * from users")
    userinfo = cur.fetchall()
    return userinfo

def check_loginname(loginname):
    for user in getuser():
	username = user['name']
	if loginname == username:
	    return True

def queryuser(username):
    sql = "select * from users where name = '%s'" % (username)
    cur.execute(sql)
    usersinfo = cur.fetchall()
    for userdict in usersinfo:
	return userdict

def deluser(username):
    sql = "delete users from users where name = '%s'" % (username)
    cur.execute(sql)
    conn.commit()

def queryuserid(userid):
    sql = "select * from users where id = '%s'" % (userid)
    cur.execute(sql)
    userid_info = cur.fetchall()
    for userinfo in userid_info:
	return userinfo

