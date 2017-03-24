#!/usr/bin/python
#coding:utf-8

import  MySQLdb as mysql

conn = mysql.connect(user='root',passwd='123456',host='localhost',db='reboot10')
cur = conn.cursor()

def idclist(id=None):
    idcs = []
    fields = ['id','city','name','idc_supplier','idc_address','business_contacts','operation']
    if not id:
        sql = "select %s from idc"%','.join(fields)
        cur.execute(sql)
        result = cur.fetchall()
        for row in result:
            idc = {}
            for i,k in enumerate(fields):
                idc[k] = row[i]
            idcs.append(idc)
        return idcs
    else:
        sql2 = "select %s from idc where id='%s'"%(','.join(fields),id)
        cur.execute(sql2)
        result = cur.fetchone()
        idc = {}
        for i,k in enumerate(fields):
            idc[k] = result[i]
        return idc

def update_list(id):
    fields = ['id','city','name','idc_supplier','idc_address','business_contacts','operation']
    sql = "select %s from idc where id='%s'"%(','.join(fields),id)
    cur.execute(sql)
    result = cur.fetchone()
    idc = {}
    for i,k in enumerate(fields):
        idc[k] = result[i]
    return idc

def idcadd(args):
    sql = 'insert into idc set %s'%','.join(args)
    cur.execute(sql)
    conn.commit()
    
def delidc(id):
    sql = "delete from idc where id='%s'"%(id)
    cur.execute(sql)
    conn.commit()

def update(args,id):
    sql = "update idc set %s where id=%s"%(','.join(args),id)
    cur.execute(sql)
    conn.commit()
