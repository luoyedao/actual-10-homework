# #!/usr/bin/env python
# #coding:utf-8

f = open('access.log','r')

ip_dict = {}
for i in f:
    ip = i.split()[0]
    if ip in ip_dict:
        ip_dict[ip] += 1
    else:
        ip_dict[ip] = 1
f.close()

dict_ip = {}
for ip,count in ip_dict.items():
    dict_ip.setdefault(count,[])
    dict_ip[count].append(ip)


count = 0
f = open('tongji.html','a+')
f.write("<html><table style='border:solid 1px'>")
f.write("<th style='border:solid 1px'>count</th><th style='border:solid 1px'>IP</th>")
while count < 10:
    key = max(dict_ip.keys())
    for max_ip in dict_ip[key]:
        f.write('<tr><td style="border:solid 1px">%s</td><td style="border:solid 1px">%s</td></tr>' % (key,max_ip))
    dict_ip.pop(key)
    count = count + 1
    print dict_ip
f.write("</table></html>")
f.close()

