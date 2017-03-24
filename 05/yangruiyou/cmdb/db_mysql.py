import MySQLdb as mysql
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('config.ini')


def execute_sql(sql):
    res_list = []
    conn = mysql.connect(host=config.get('mysql', 'host'), port=config.getint('mysql', 'port'),
                         user=config.get('mysql', 'username'), passwd=config.get('mysql', 'password'),
                         db=config.get('mysql', 'dbname'), charset=config.get('mysql', 'charset'))
    cur = conn.cursor()
    res = cur.execute(sql)

    res_list = cur.fetchall()
    conn.commit()
    #print res_list
    cur.close()
    #print res_list
    conn.close()
    return res_list


if __name__ == "__main__":
    sql = "insert into users(name,name_cn,password,mobile,role,status,create_time) values('long1','long1','123456','12345678901',1,0,now())"
    execute_sql(sql)
