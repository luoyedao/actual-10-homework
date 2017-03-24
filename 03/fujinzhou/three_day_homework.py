#!/usr/bin/env python
#coding:utf-8

#将ip从文件中读取并输出到一个字典中
f=open('access.log','r')
ip_list={}

for i in f:
    ip=i.split()[0]
    if ip in ip_list:
        ip_list[ip]+=1
    else:
        ip_list[ip]=1
f.close()
#print ip_list

#将ip反转统计
statistics={}
for k,v in ip_list.items():
    statistics.setdefault(v,[])
    statistics[v].append(k)
#print statistics

count=0
f = open('staistics.html','a+')
f.write("<html><table style='border:solid 1px'>")
f.write("<th style='border:solid 1px'>Access NUmber</th><th style='border:solid 1px'>IP Address</th>")

while count < 10:
    key = max(statistics.keys())
    max_ip=statistics[key]
#    print max_ip
    if len(max_ip) >1:
        ips=",".join(max_ip)
    else:
        ips=max_ip[0]
    f.write('<tr><td style="border:solid 1px">%s</td><td style="border:solid 1px">%s</td></tr>' % (key,ips))
    statistics.pop(key)
    count = count +1
f.write("</table></html>")
f.close()