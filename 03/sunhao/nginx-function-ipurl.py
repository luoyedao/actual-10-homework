#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
def open_file(file_name):
    res = {}
    with open(file_name) as f:
        for line in f:
            ip = line.split(" ")[0]
            url = line.split(" ")[6]
            res[(ip,url)] = res.get((ip,url),0)+1
    
    return sorted(res.items(),key=lambda x:x[1],reverse=True)
def write_html(arr,file_html):
    i = 0
    html_str = '<table border="1px"><tr><td>no</td> <td>ip</td><td>url</td><td>count</td>'
    for r in arr[:10]:
        i = i+1
        html_str += '<tr><td>no%s</td> <td>%s</td><td>%s</td><td>%s</td>'%(i,r[0][0],r[0][1],r[1])
    html_str+='</table>'

    html_f = open(file_html,'w')
    html_f.write(html_str)
    html_f.close()

def start_operate():
    res_list = open_file('log1.log')
    write_html(res_list,'sunhao.html')
start_operate()
