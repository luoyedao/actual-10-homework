#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
def open_file(file_name):
    res = {}
    with open(file_name) as f:
        for line in f:
            ip = line.split(" ")[0]
            res[ip] = res.get((ip),0)+1
#            if ip in res:
#                res[ip] += 1
#            else:
#                res[ip] = 1
    return sorted(res.items(),key=lambda x:x[1],reverse=True)
#def bubble_sort(arr,times):
#    for j in range(times):
#        for i in range(len(arr)-1):
#                if arr[i][1] > arr[i+1][1]:
#                    arr[i],arr[i+1]=arr[i+1],arr[i]
#    return arr

def write_html(arr,file_html):
    i = 0
    html_str = '<table border="1px"><tr><td>no</td> <td>ip</td><td>count</td>'
    for r in arr[:10]:
        i = i+1
        html_str += '<tr><td>no%s</td> <td>%s</td><td>%s</td>'%(i,r[0],r[1])
    html_str+='</table>'

    html_f = open(file_html,'w')
    html_f.write(html_str)
    html_f.close()

def start_operate():
    res_list = open_file('log1.log')
    write_html(res_list,'sunhao.html')
start_operate()
