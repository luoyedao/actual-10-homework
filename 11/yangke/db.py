#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-08-13 18:59:48
# @Author  : yang ke (jack_keyang@163.com)

import MySQLdb as mysql

conn = mysql.connect(host="localhost",user="root",passwd="123456",db="reboot10",charset="utf8")
conn.autocommit(True)
curs = conn.cursor()

#获取用户信息列表
def userlist(fields):
    sql = "select %s from users"%",".join(fields)
    curs.execute(sql)
    result = curs.fetchall()
    u_list = [dict((k,row[i]) for i, k in enumerate(fields)) for row in result]
    return u_list

'''
    获取单个用户信息，可通过id或用户名查询该用户信息
    getone({"id":1})
    getone({"name":"admin"})

'''
def getone(dic):
    fields = ["id","name","name_cn","password","mobile","email","role","status"]
    sql = "select %s from users where %s='%s'"%(",".join(fields),dic.keys()[0],dic.values()[0])
    print sql
    curs.execute(sql)
    result = curs.fetchone()
    if result:
        u_dict = dict((k, result[i])for i, k in enumerate(fields))
        return u_dict
    else:
        return False

#修改用户信息
def modfiy(fields):
    print fields
    data = ",".join(["%s='%s'"%(k,v) for k,v in fields.items()])
    print data
    sql = "update users set %s where id='%s'"%(data,fields["id"])
    print sql
    curs.execute(sql)
    conn.commit()

#添加用户
def adduser(fields):
    sql = "insert into users(%s)values('%s')"%(",".join(fields.keys()),"','".join(fields.values()))
    curs.execute(sql)
    conn.commit()

#删除用户
def delete(uid):
    sql = "delete from users where id=%s"%uid
    curs.execute(sql)
    conn.commit()

def modpasswd(dict):
    sql = "update users set password='%(password)s' where id=%(id)s"%dict
    curs.execute(sql)
    conn.commit()

def idclist():
    fields = ["id","name","name_cn","address","adminer","phone","num"]
    sql = "select %s from idc"%",".join(fields)
    curs.execute(sql)
    result = curs.fetchall()
    result = [dict( (v,row[k]) for k,v in enumerate(fields)) for row in result]
    return result

def idc_getone(dicts):
    fields = ["id", "name", "name_cn", "address", "adminer", "phone", "num"]
    sql = "select %s from idc where %s=%s"%(",".join(fields),dicts.keys()[0],dicts.values()[0])
    curs.execute(sql)
    result = curs.fetchone()
    result = dict((v,result[k]) for k,v in enumerate(fields))
    if result:
        return result
    else:
        return False

def idc_update(dicts):
    data = ",".join(["%s='%s'"%(k,v) for k,v in dicts.items()])
    sql = "update idc set %s where id=%s"%(data,dicts["id"])
    curs.execute(sql)
    conn.commit()

#检测idc是否存在，存在返回false
def idc_check(idcname):
    sql = "select count(id) from idc where name='%s'"%idcname
    curs.execute(sql)
    result = curs.fetchone()[0]
    if result == 1:
        return False
    else:
        return True

def idc_add(dic):
     sql = "insert into idc(%s)values('%s')"%(",".join(dic.keys()),"','".join(map(str,dic.values())))
     curs.execute(sql)
     conn.commit()

def idc_del(id):
    sql = "delete from idc where id=%s"%id
    curs.execute(sql)
    conn.commit()

def idc_name():
    fields = ["id","name_cn"]
    sql = "select %s from idc"%",".join(fields)
    curs.execute(sql)
    result = curs.fetchall()
    return dict(result)

def cab_list():
    fields = ["a.id","a.name","b.name_cn","a.u_num"]
    sql = "select %s from cabinet as a,idc as b where %s=%s"%(",".join(fields),"a.idc_id","b.id")
    curs.execute(sql)
    result = [dict((v,row[k]) for k,v in enumerate(fields)) for row in curs.fetchall()]
    return result

def cab_getone(id):
    fields = ["id","name","u_num"]
    sql = "select %s from cabinet where id=%s" % (",".join(fields),id)
    curs.execute(sql)
    result = curs.fetchone()
    result = dict((v,result[k]) for k,v in enumerate(fields))
    return result

def cab_update(dic):
    data = ",".join(["%s='%s'"%(k,v) for k,v in dic.items()])
    sql = "update cabinet set %s where id=%s"%(data,dic["id"])
    curs.execute(sql)
    conn.commit()

def cab_del(id):
    sql = "delete from cabinet where id=%s"%id
    curs.execute(sql)
    conn.commit()

def cab_add(fields):
    sql = "insert into cabinet(%s)values('%s')"%(",".join(fields.keys()),"','".join(fields.values()))
    curs.execute(sql)
    conn.commit()

def cab_name():
    fields = ["id","name"]
    sql = "select %s from cabinet"%",".join(fields)
    curs.execute(sql)
    result = curs.fetchall()
    return dict(result)

def server_list():
    fields = ["a.id","a.hostname","a.lan_ip","a.wan_ip","b.name","a.op","a.phone"]
    sql = "select %s from server as a,cabinet as b where %s=%s"%(",".join(fields),"a.cabinet_id","b.id")
    curs.execute(sql)
    result = [dict((v, row[k]) for k, v in enumerate(fields)) for row in curs.fetchall()]
    return result

def server_check(dic):
    data = "%s='%s'"%(dic.keys()[0],dic.values()[0])
    sql = "select count(id) from server where %s"%data
    curs.execute(sql)
    result = curs.fetchone()
    return result[0]

def server_add(dic):
    sql = "insert into server(%s)values('%s')"%(",".join(dic.keys()),"','".join(dic.values()))
    curs.execute(sql)
    conn.commit()

def server_getone(id):
    fields = ["id","hostname","lan_ip","wan_ip","cabinet_id","op","phone"]
    sql = "select %s from server where id=%s"%(",".join(fields),id)
    curs.execute(sql)
    result = curs.fetchone()
    return dict((v,result[k]) for k,v in enumerate(fields))

def server_up(dic):
    data = ",".join(["%s='%s'"%(k,v) for k,v in dic.items()])
    sql = "update server set %s where id=%s"%(data,dic["id"])
    curs.execute(sql)
    conn.commit()

def server_del(id):
    sql = "delete from server where id=%s"%id
    curs.execute(sql)
    conn.commit()

if __name__ == "__main__":
#    field = ["role"]
    #fields = ["id","name","name_cn","mobile","email","role","status"]
    print cab_name()
