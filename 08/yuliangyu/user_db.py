import MySQLdb as mysql

conn = mysql.connect(user='root',host='127.0.0.1',passwd='123456',db='reboot10',charset='utf8')
conn.autocommit(True)
cur = conn.cursor()

def insert(fields,data):
    sql = 'INSERT INTO users (%s) VALUES (%s)' % (','.join(fields), ','.join([ '"%s"' % data[x] for x in fields ]))
    cur.execute(sql)
    
def selectOne(fields,condition):
    sql = "SELECT %s FROM users WHERE %s" % (','.join(fields), condition)
    cur.execute(sql)
    res = cur.fetchone()
    return res

def selectAll(fields):
    sql = "SELECT %s FROM users" % ','.join(fields)
    cur.execute(sql)
    res = cur.fetchall()
    return res

def update(condition,id):
    sql = "UPDATE users SET %s WHERE id = %s" % (','.join(condition), id)
    cur.execute(sql)

def selectId(fields,id):
    sql = "SELECT %s FROM users WHERE id = %s" % (','.join(fields), id)
    cur.execute(sql)
    res = cur.fetchone()
    return res

def delete(id):
    sql = "DELETE FROM users WHERE id = %s" % (id)
    cur.execute(sql)
