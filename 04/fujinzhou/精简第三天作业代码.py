#!/usr/bin/env python
#coding:utf-8

def open_file(file_name):
    res={}
    with open(file_name) as f:
        for line in f:
            tmp=line.split(' ')
#           print tmp
            ip,url=tmp[0],tmp[6]
#       print ip,url 以元组的形式存到列表中
            res[(ip,url)]=res.get((ip,url),0)+1
    return sorted(res.items(),key=lambda  x:x[1],reverse=True)
#print open_file('log1.log')


def get_htmlstr(arr):
#拼接字符串
    tmp1='<tr><td>Num%s</td> <td>%s</td> <td>%s</td> <td>%s</td></tr>'
    html_str='<table border="1px">'+tmp1%('名次','IP','URL','COUNT')
    for index,value in  enumerate(arr[:10]):
        html_str+='<tr><td>Num%s</td> <td>%s</td> <td>%s</td> <td>%s</td></tr>' %(index,value[0][0],value[0][1],value[1])
    html_str+='</table>'
    return html_str
def write_html(file_name):
    res=open_file(file_name)
    with open('res2.html','w') as f:
        f.write(get_htmlstr(res))
write_html('log1.log')
