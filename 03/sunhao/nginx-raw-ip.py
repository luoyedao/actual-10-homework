#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
f = open('log1.log')
res = {}
for line in f.readlines():
    tmp = line.split(" ")
    ip = tmp[0]
    if ip in res:
        res[ip] += 1
    else:
        res[ip] = 1
f.close()

for r in res.items():
    res_list = res.items()
    for j in range(10):
        for i in range(len(res_list)-1):
            if res_list[i][1] > res_list[i+1][1]:
                res_list[i],res_list[i+1]=res_list[i+1],res_list[i]

    i = 0
    html_str = '<table border="1px"><tr><td>no</td> <td>ip</td><td>count</td>'
    for r in res_list[:-11:-1]:
        i = i+1
        html_str += '<tr><td>no%s</td> <td>%s</td><td>%s</td>'%(i,r[0],r[1])
    html_str+='</table>'

    html_f = open('res.html','w')
    html_f.write(html_str)
    html_f.close()
