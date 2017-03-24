#!/usr/bin/env python
#coding:utf-8

f = open('access.log')

d1 = {}
# 将字典拼接为ip:num的格式
for i in f.readlines():
    ip = i.split(" ")[0]
    if ip not in d1:
        d1[ip] = 1
    else:
        d1[ip] += 1
f.close()

# 将字典翻转成为num:word的格式
d2 ={}
for k,v in d1.items():
    d2.setdefault(v,[])
    d2[v].append(k)

# 统计nginx前十日志
'''count = 0
while count < 10 :
    max1 = max(d2.keys())
    str_d2 = ".".join(d2[max1])
    d2.pop(max1)
    count += 1
    print max1,str_d2'''


# 统计nginx前十ip
count = 0
f = open('analyza_nginx_log.html','a+')
    # 设置utf8编码
f.write('<head>')
f.write('<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />')
f.write('</head>')

f.write("<html><table style='border:solid 1px'>")
f.write("<th style='border:solid 1px'>次数</th><th style='border:solid 1px'>IP地址</th>")

while count < 10:
    max_key = max(d2.keys())
    for i in d2[max_key]:
        f.write('<tr><td style="border:solid 1px">%s</td><td style="border:solid 1px">%s</td></tr>' % (max_key,i))
    d2.pop(max_key)
    count += 1

f.write("</table></html>")
f.close()

