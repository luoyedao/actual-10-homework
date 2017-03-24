#!/usr/bin/env python
f = open('/home/toby/reboot_homework/access.log')

dict = {}
for i in f.readlines():
    ip = i.split(' - - ')[0]
    if ip in dict:
	dict[ip] += 1
    else:
	dict[ip] = 1

ip_dict = {}
for k,v in dict.items():
    ip_dict.setdefault(v,[])
    ip_dict[v].append(k)

f = open('/home/toby/reboot_homework/access.html','a+')
f.write("<html><table style='border:solid 1px'>")
f.write("<th style='border:solid 1px'>Access NUmber</th><th style='border:solid 1px'>IP Address</th>")
cont = 0
while cont < 10:
    key = max(ip_dict.keys())
    for val in ip_dict[key]:
	f.write('<tr><td style="border:solid 1px">%s</td><td style="border:solid 1px">%s</td></tr>' % (key,val))
    ip_dict.pop(key)
    cont += 1
f.write("</table></html>")    
f.close()


