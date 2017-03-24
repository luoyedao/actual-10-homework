#!/usr/bin/env python

import MySQLdb,time
date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
conn = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='1qaz#EDC', db='reboot10')
cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)

def add_set_user(user):
    fields = ['status','role','name','mobile','password','name_cn','email']
    sql = "insert into users (%s,create_time,last_time) values (%s,'%s','%s')" % (','.join(fields), user, date,date)
    cur.execute(sql)
    conn.commit()


def get_by_all():
    cur.execute("select * from users")
    user = cur.fetchall()
    return user

def get_by_id(userid):
    sql = "select * from users where id = '%s'" % (userid)
    cur.execute(sql)
    users = cur.fetchall()
    for user in users:
	return user

def get_by_name(username):
    sql = "select * from users where name = '%s'" % (username)
    cur.execute(sql)
    users = cur.fetchall()
    for user in users:
	return user

def del_by_id(userid):
    sql = "delete users from users where id = '%s'" % (userid)
    cur.execute(sql)
    conn.commit()

def update_user_data(sql,userid):
    sql_updatename = "update users set %s where id='%s'" % (sql,userid)
    cur.execute(sql_updatename)
    conn.commit()

def check_login_name(username):
    for i in get_by_all():
        if i['name'] == username:
	    return True




