#!/usr/bin/env python
# coding=utf-8
ips = []
dict_ip = {}
dict_ips = {}
num = 0
f = open('access.log')
nginx_files = open('nginx_file', 'a+')
nginx_lines = f.readlines()
for nginx_line in nginx_lines:
    ips.append(nginx_line.split()[0])

for ip in ips:
    if ip in dict_ip:
        dict_ip[ip] += 1
    else:
        dict_ip[ip] = 1

f.close()
for k, v in dict_ip.iteritems():
    dict_ips.setdefault(v, []).append(k)

keys = dict_ips.keys()
keys.sort()
keys.reverse()
for i in keys:
    num += 1
    if num == 1:
        if len(dict_ips[i]) == 1:
            nginx_files.write('''<!DOCTYPE html>
<head>
<meta charset="utf-8">
</head>
<html>
<body>
<table border='1'>
     <tr>
         <th>访问量</th>
         <th>IP</th>
     </tr>
     <tr>
         <td>%d</td>
         <td>%s</td>
     </tr>''' % (i, dict_ips[i][0])
                              )
            continue
        elif len(dict_ips[i]) > 1:
            nginx_files.write('''<!DOCTYPE html>
<head>
<meta charset="utf-8">
</head>
<html>
<body>
<table border='1'>
    <tr>
         <th>访问量</th>
         <th>IP</th>
    </tr> '''
                              )
            for t in dict_ips[i]:
                nginx_files.write('''
     <tr>
         <td>%d</td>
         <td>%s</td>
     </tr>''' % (i, t)
                                  )
    for t in dict_ips[i]:
                nginx_files.write('''
     <tr>
         <td>%d</td>
         <td>%s</td>
     </tr>''' % (i, t)
                                  )

    if num == 10:
        nginx_files.write('''</table>
 </body>
 </html>''')
        break
nginx_files.close()
