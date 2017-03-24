#!/usr/bin/env python
# Program:
#	This program is the database operation
# Author:   Tantianran    15915822634@139.com
# last modification time:  /2016/08/26  
# Version:  v1.1

# Import time module
import time
date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

# Import the mysql module
import MySQLdb as mysql

# Connect to the database and the establishment of a cursor object
conn = mysql.connect(host='127.0.0.1', port=3306, user='root', passwd='1qaz#EDC', db='reboot10')
cur = conn.cursor(cursorclass=mysql.cursors.DictCursor)


# All the user information retrieved from the database
def get_user_all():
    sql = "select * from users"
    cur.execute(sql)
    res = cur.fetchall()
    return res

# By the name the where condition, for specified user information
def get_user_name(username):
    sql = "select * from users where name = '%s'" % (username)
    cur.execute(sql)
    users = cur.fetchall()
    for user in users:
	return user

# To check if the login user name exists in the database
def check_login_name(username):
    for temp in get_user_all():
        if temp['name'] == username:
	    return True

# this is delete users
def del_by_id(userid):
    sql = "delete users from users where id = '%s'" % (userid)
    cur.execute(sql)
    conn.commit()

# Update the user information
def update_user_data(sql,userid):
    sql_updatename = "update users set %s where id='%s'" % (sql,userid)
    cur.execute(sql_updatename)
    conn.commit()

# The data via the ID from the database
def get_by_id(userid):
    sql = "select * from users where id = '%s'" % (userid)
    cur.execute(sql)
    users = cur.fetchall()
    for user in users:
	return user

# Add user
def add_set_user(user):
    fields = ['status','role','name','mobile','password','name_cn','email']
    sql = "insert into users (%s,create_time,last_time) values (%s,'%s','%s')" % (','.join(fields), user, date,date)
    cur.execute(sql)
    conn.commit()

# Write the last login time
def update_user_lasttime(times,username):
    sql_updatename = "update users set last_time='%s' where name='%s'" % (times,username)
    cur.execute(sql_updatename)
    conn.commit()
