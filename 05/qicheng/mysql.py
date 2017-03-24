Centos7数据库mysql安装
yum install wget –y && wget http://repo.mysql.com/mysql-community-release-el7-5.noarch.rpm
rpm -ivh mysql-community-release-el7-5.noarch.rpm
yum install mysql-server –y
service mysqld start



# 进入数据库
mysql

# 创建数据库
mysql> create database aatest;


# 进入数据库
mysql> use aatest


#建表语句
mysql> create table aatest(
	name varchar(200),
	age int
);

# 完整建表语句
create table user(
	id int primary key auto_increment,
	username varchar(25),
	password varchar(32),
	age int
	)engine=innodb default charset=utf8;

# 查询表结构
mysql> desc aatest;


# 在表中插入数据
mysql> insert into aatest values ('wd',18);


# 查询数据（格式）
mysql> select 列名  from 表名;
# 如下
mysql> select name from aatest;


# 查询所有字段（可用*代替）
mysql> select name,age from aatest;

# 再次尝试多插入几个数据
mysql> insert into aatest values ('pc',12);
mysql> insert into aatest values ('ada',10);
mysql> insert into aatest values ('woniu',30);

查询数据（所有字段）
mysql> select * from aatest;   #生产环境慎用
+-------+------+
| name  | age  |
+-------+------+
| wd    |   18 |
| pc    |   12 |
| ada   |   10 |
| woniu |   30 |
+-------+------+


修改数据
mysql> update aatest set age=100 where name='wd';

mysql> select name,age from aatest;
+-------+------+
| name  | age  |
+-------+------+
| wd    |  100 |
| pc    |   12 |
| ada   |   10 |
| woniu |   30 |
+-------+------+

mysql> update aatest set age=1;  #update修改数据如果不加where语句，后果很严重
mysql> select name,age from aatest;
+-------+------+
| name  | age  |
+-------+------+
| wd    |    1 |
| pc    |    1 |
| ada   |    1 |
| woniu |    1 |
+-------+------+


mysql> delete from aatest where name='wd';   #删除数据，也必须加where条件，否则所有数据全删除
+-------+------+
| name  | age  |
+-------+------+
| pc    |    1 |
| ada   |    1 |
| woniu |    1 |


# 继续插入数据
insert into aatest values ('xiaoming',12);
insert into aatest values ('xiaohua',100);
insert into aatest values ('reboot',30);

mysql> select name,age from aatest;
+----------+------+
| name     | age  |
+----------+------+
| pc       |    1 |
| ada      |    1 |
| woniu    |    1 |
| xiaoming |   12 |
| xiaohua  |  100 |
| reboot   |   30 |
+----------+------+

# 条件查询1
mysql> select * from aatest where name='reboot';
+--------+------+
| name   | age  |
+--------+------+
| reboot |   30 |
+--------+------+
1 row in set (0.00 sec)

# 条件查询2
mysql> select * from aatest where age>10;
+----------+------+
| name     | age  |
+----------+------+
| xiaoming |   12 |
| xiaohua  |  100 |
| reboot   |   30 |
+----------+------+


#条件查询3(多条件查询and)
mysql> select * from aatest where age>10 and age<40;
+----------+------+
| name     | age  |
+----------+------+
| xiaoming |   12 |
| reboot   |   30 |


#条件查询4(多条件查询or)
mysql> select * from aatest where name='woniu' or name='pc';
+-------+------+
| name  | age  |
+-------+------+
| pc    |    1 |
| woniu |    1 |



# Python读取数据库数据需要装插件
yum install gcc gcc-devel python-devel -y
yum install MySQL-python -y


# 给新用户user授权某个库kk2所有权限
CREATE USER 'reboot'@'localhost' IDENTIFIED BY '123456';
grant all on kk2.* to 'reboot'@'localhost' identified by '123456';
flush privileges;

#python操作数据库
linux命令航中输入python
import MySQLdb   #引入mysql
conn = MySQLdb.connect(host='localhost', port=3306, user='reboot', passwd='123456', db='kk2', charset='utf8')
conn             #创建连接
cur = conn.cursor()   #获取游标才能操作数据库
cur.execute('insert into user(username, password, age) values("kk", md5("123456"), 29)')   #插入一条数据
conn.commit()                   #数据应用到数据库，否则不生效
mysql> select * from  kk2.user;       #查询语句
+----+----------+----------------------------------+------+
| id | username | password                         | age  |
+----+----------+----------------------------------+------+
|  1 | kk       | e10adc3949ba59abbe56e057f20f883e |   29 |
+----+----------+----------------------------------+------+

conn.autocommit(True)     #也可以设置自动提交，插入数据立即生效
cur.execute('select * from user;')    #查询表中共有多少行数据
cur.fetchone()          	#按一行行的去查询数据
cur.execute('select * from user;')    #重新查询表中共有多少行数据
cur.fetchall()				#一次读完所有数据
cur.close()                #关闭cur
conn.close()               #关闭conn连接


# 代码写到python脚本中
import MySQLdb as mysql
db = mysql.connect(user="root", passwd="", \
	db="aatest", charset="utf8")
db.autocommit(True)
cur = db.cursor()
cur.execute('select * from aatest')

for c in cur.fetchall():
	print 'name is %s and age is %d' % c


# 执行结果
[root@centos7.2:/root/python/06]# python mysql1.py 
name is pc and age is 1
name is ada and age is 1
name is woniu and age is 1
name is xiaoming and age is 12
name is xiaohua and age is 100
name is reboot and age is 30




<style type="text/css">

#test{
	width:200px;
	height:200px;
	background: red;
}
</style>
<div id='test'></div>