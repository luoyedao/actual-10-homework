#!/usr/bin/python
#coding:utf-8
'''
write by liwei.fu
date:2016-07-17
'''
import os,sys
os.system('clear')
before_dict = {}
log_f = open("access.log",'r')
lines = log_f.readlines()
#print lines
for line in lines:
	line = line.strip()
#	print line
	ip = line.split(' ')[0]
	if ip not in before_dict :
		before_dict[ip] = 1
	else :
		before_dict[ip] += 1
log_f.close()
print before_dict

'''
倒置字典,以出现次数为key,ip为value存放在after_dict字典中
'''
after_dict = {}
for k,v in before_dict.items():
#有优化空间,装逼的代码
	after_dict.setdefault(v,[])
	after_dict[v].append(k)
'''
*********劣质代码*************
	if v not in after_dict :
		after_dict[v] = [k]
	else :
		after_dict[v].append(k)

'''
#调试打印倒转后的字典
#print after_dict 
'''
最后一部分实现写入到网页文件中去
'''
count = 0 
result_f = open("version2_Nginx_log_ip.html",'a+')
result_f.write("<html><table style='border:solid 1px'>\n")#打印表格1px,数字1  px.
result_f.write("<th style='border:solid 1px'>排名</th><th style='border:solid 1px'>次数</th><th style='border:solid 1px'>ip地址</th>\n")
while count < 10 :
	key = max(after_dict.keys())
	print key
	for i in after_dict[key]:
		result_f.write("<tr><td style='border:solid 1px'>%d</td><td style='border:solid 1px'>%s</td><td style='border:solid 1px'>%s</td></tr>\n"  %((count + 1),key,i))
	after_dict.pop(key)
	count += 1
result_f.write("</table></html>")
result_f.close()

