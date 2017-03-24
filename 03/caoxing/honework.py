#!/usr/bin/env python
#coding=utf8

fil=open('access.log','r')

ip_dict={}
for i in fil:
     ip=i.split()[0]
     if ip in ip_dict:
          ip_dict[ip] += 1
     else:
          ip_dict[ip]=1
fil.close

dict_ip={}
for ip,count in ip_dict.items():
    dict_ip.setdefault(count,[])
    dict_ip[count].append(ip)

count=0
fil=open('tianshi.html','a+')
fil.write("<html><table style='border:solid 1px'>")
fil.write("<th style='border:solid 1px'>count</th><th style='border:solid 1px'>IP</th>")
xxxx=0
while True:
    if dict_ip:
        key = max(dict_ip.keys())
        for max_ip in dict_ip[key]:
            fil.write('<tr><td style="border:solid 1px">%s</td><td style="border:solid 1px">%s</td></tr>' % (key,max_ip))
        dict_ip.pop(key)
        count += 1
    if count > 9:
        break
    xxxx +=1
#    print dict_ip
fil.write("</table></html>")
fil.close()
