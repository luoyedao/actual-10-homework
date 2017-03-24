#!/usr/bin/env python
#coding:utf-8

f=open("access.log")
result = { }
for lines in f.readlines():
    line=lines.split()
    iplist=line[0]
#    print line[0]
    if iplist in result:
        result[iplist] +=1
    else:
        result[iplist] = 1
#print result
res = { }
for k,v in result.items():
    res.setdefault(v,[])
    res[v].append(k)
#print res
f.close()
count = 0
f = open('tongji.html','a+')
f.write("<html><table style='border:solid 1px'>")
f.write("<th style='border:solid 1px'>访问排名</th><th style='border:solid 1px'>IP</th>")
while count < 10:
    key = max(res.keys())
    for word in res[key]:
        f.write('<tr><td style="border:solid 1px">%s</td><td style="border:solid 1px">%s</td></tr>' % (key,word))
    res.pop(key)
    count = count +1
f.write("</table></html>")
f.close()
