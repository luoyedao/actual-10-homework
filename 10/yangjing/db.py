#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-08-13 18:59:48
# @Author  : yang ke (jack_keyang@163.com)

import MySQLdb as mysql

conn = mysql.connect(host="localhost", user="root", passwd="1q2w3e4r", db="reboot10", charset="utf8")
conn.autocommit(True)
curs = conn.cursor()


def userlist(fields):
	sql = "select %s from users" % ",".join(fields)
	curs.execute(sql)
	result = curs.fetchall()
	u_list = [dict((k, row[i]) for i, k in enumerate(fields)) for row in result]
	return u_list


def getone(uid):
	fields = ["id", "name", "name_cn", "mobile", "email", "role"]
	sql = "select %s from users where id=%s" % (",".join(fields), uid)
	curs.execute(sql)
	result = curs.fetchone()
	u_dict = dict((k, result[i]) for i, k in enumerate(fields))
	return u_dict


def modfiy(fields):
	data = ",".join(["%s='%s'" % (k, v) for k, v in fields.items()])
	sql = "update users set %s where id='%s'" % (data, fields["id"])
	print sql
	curs.execute(sql)
	conn.commit()


def adduser(fields):
	sql = "insert into users(%s)values('%s')" % (",".join(fields.keys()), "','".join(fields.values()))
	curs.execute(sql)
	conn.commit()


def delete(uid):
	sql = "delete from users where id=%s" % uid
	curs.execute(sql)
	conn.commit()


def checkuser(dict, field='password'):
	sql = "select %s from users where %s='%s'" % (field, dict.keys()[0], dict.values()[0])
	curs.execute(sql)
	result = curs.fetchall()
	if len(result):
		result = [v[0] for v in result]
	else:
		result = []
	return result


def modpasswd(dict):
	sql = "update users set password='%(password)s' where id=%(id)s" % dict
	curs.execute(sql)
	conn.commit()
