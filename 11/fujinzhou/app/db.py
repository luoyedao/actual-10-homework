#!/usr/bin/env python
#coding:utf-8
import MySQLdb as mysql
conn=mysql.connect(user='root',passwd='www.123',db='reboot10',charset='utf8')
curs=conn.cursor()

#获取用户列表

def get_userlist(userlist):
        sql="select %s from users" %','.join(userlist)
        users=[]
        curs.execute(sql)
        result=curs.fetchall()
	users=[dict((k,row[i]) for i, k in enumerate(userlist)) for row in result]
        return users

#获取单个用户

def getuser(uid):
        userlist=["name","name_cn","email","mobile","role","status"]
        sql="select %s from users where id=%s" %(",".join(userlist),uid)
        curs.execute(sql)
        result=curs.fetchone()
        conn.commit()
        userinfo={}
        for i,k in enumerate(userlist):
                userinfo[k]=result[i]
        return userinfo


def getone(name):
	userlist=["id","name","name_cn","email","mobile","role","status"]
	sql="select %s from users where name='%s'" %(",".join(userlist),name)
        curs.execute(sql)
        result=curs.fetchone()
        conn.commit()
        userinfo={}
        for i,k in enumerate(userlist):
                userinfo[k]=result[i]
        return userinfo



#添加用户

def add_user(userlist):
	sql="insert into users(%s)values('%s')"%(",".join(userlist.keys()),"','".join(userlist.values()))
        curs.execute(sql)
        conn.commit()

#删除用户

def del_user(uid):
        sql="delete from users where id=%s"%uid
        curs.execute(sql)
        conn.commit()

#更新用户

def update_user(userdict):
        sql="update users set email='%(email)s',mobile='%(mobile)s',role='%(role)s',status='%(status)s' where name='%(name)s'"%(userdict)
        curs.execute(sql)
        conn.commit()
#检查用户
def checkuser(name):
    sql = "select password from users where name='%s'"%name
    curs.execute(sql)
    passwd = curs.fetchone()
    return passwd[0]

#修改密码
def modpasswd(password,uid):
    sql = "update users set password='%s' where id='%s'"%(password,uid)
    curs.execute(sql)
    conn.commit()

#获取idc列表

def get_idclist(idclist):
        sql="select %s from idclist" %','.join(idclist)
        idcs=[]
        curs.execute(sql)
        result=curs.fetchall()
        idcs=[dict((k,row[i]) for i, k in enumerate(idclist)) for row in result]
        return idcs

#添加idc

def add_idc(idclist):
        sql="insert into idclist(%s)values('%s')"%(",".join(idclist.keys()),"','".join(idclist.values()))
        curs.execute(sql)
        conn.commit()

#删除idc

def del_idc(uid):
        sql="delete from idclist where id=%s"%uid
        curs.execute(sql)
        conn.commit()


#更新IDC

def update_idc(idcdict):
        sql="update idclist set cabinets='%(cabinets)s',hosts='%(hosts)s',contacts='%(contacts)s',telephone='%(telephone)s',remarks='%(remarks)s'  where name='%(name)s'"%(idcdict)
        curs.execute(sql)
        conn.commit()

#获取单个IDC

def getidc(uid):
        idclist=["name","cabinets","hosts","contacts","telephone","remarks"]
        sql="select %s from idclist where id=%s" %(",".join(idclist),uid)
        curs.execute(sql)
        result=curs.fetchone()
        conn.commit()
        idcinfo={}
        for i,k in enumerate(idclist):
                idcinfo[k]=result[i]
        return idcinfo
