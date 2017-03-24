import MySQLdb as mysql

conn = mysql.connect(user='root',host='127.0.0.1',passwd='123456',db='reboot10',charset='utf8')
conn.autocommit(True)
cur = conn.cursor()

def insert(fields,data,table):
    sql = 'INSERT INTO %s (%s) VALUES (%s)' % (table, ','.join(fields), ','.join([ '"%s"' % data[x] for x in fields ]))
    cur.execute(sql)

def selectOne(fields,condition):
    sql = "SELECT %s FROM users WHERE %s" % (','.join(fields), condition)
    cur.execute(sql)
    res = cur.fetchone()
    return res

def selectAll(fields,table):
    sql = "SELECT %s FROM %s" % (','.join(fields),table)
    cur.execute(sql)
    res = cur.fetchall()
    return res

def update(condition,id,table):
    sql = "UPDATE %s SET %s WHERE id = %s" % (table, ','.join(condition), id)
    cur.execute(sql)

def selectId(fields,id,table):
    sql = "SELECT %s FROM %s WHERE id = %s" % (','.join(fields), table, id)
    cur.execute(sql)
    res = cur.fetchone()
    return res

def delete(id,table):
    sql = "DELETE FROM %s WHERE id = %s" % (table,id)
    cur.execute(sql)

def updatepwd(passwd,id):
    sql = "UPDATE users SET password='%s' WHERE id = %s" % (passwd, id)
    cur.execute(sql)
