#!/usr/bin/python
#-coding:utf-8-

fo = open('access.log')
content = fo.readlines()
fo.close()

#从字符串转化为列表
l = []
d = {}
d2 = {}
for msg in content:
    ipaddr = msg.split(' ')[0]
    l.append(ipaddr)
#print l

#从列表转化为字典
for ipaddr in l:
    if ipaddr in d:
        d[ipaddr] += 1
    else:
	d[ipaddr] = 1
#print d
for k,v in d.items():
    d2.setdefault(v,[])
    d2[v].append(k)
#print d2


#找出访问频率最高的前十个ip地址，保存为html格式
count = 0
f = open('access.html','a+')
f.write("<html><table style='border:solid 1px'>")
f.write("<th style='border:solid 1px'>访问次数</th><th style='border:solid 1px'>ip地址</th>")
while count < 10:
    key = max(d2.keys())
    for index in range(len(d2[key])):
            f.write('<tr><td style="border:solid 1px">%s</td><td style="border:solid 1px">%s</td></tr>' % (key,d2[key][index]))
    num = len(d2[key])
    d2.pop(key)
    count = count + num
f.write("</table></html>")
f.close()
