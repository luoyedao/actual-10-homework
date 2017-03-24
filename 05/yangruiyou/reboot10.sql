create database reboot10 default charset=utf8;
use reboot10;
drop table users;

create table users(
	id int AUTO_INCREMENT primary key comment '用户id'
	,name varchar(20) not null comment '用户名'
	,name_cn varchar(50) not null comment '中文名'
	,password varchar(50) not null comment '用户密码'
	,email varchar(50) comment '电子邮件'
	,mobile varchar(11) not null comment '手机号码'
	,role varchar(10) not null comment '1:sa;2:php;3:ios;4:test'
	,status tinyint
	,create_time datetime comment '创建时间'
	,last_time datetime comment '最后登录时间'
	,unique key uni_username (name) ) engine=innodb default charset=utf8 comment '用户表';

#查询表创建
show create  table users\G;

import MySQL as mysql

























