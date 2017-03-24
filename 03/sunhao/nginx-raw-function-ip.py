#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
def open_file(file_name):
    res = {}
    with open(file_name) as f:
        for line in f:
            tmp = line.split(" ")
            ip = tmp[0]
            if ip in res:
                res[ip] += 1
            else:
                res[ip] = 1
    return res.items()

def bubble_sort(arr,times):
    for j in range(times):
        for i in range(len(arr)-1):
                if arr[i][1] > arr[i+1][1]:
                    arr[i],arr[i+1]=arr[i+1],arr[i]
    return arr

def write_html(arr):
    i = 0
    html_str = '<table border="1px"><tr><td>no</td> <td>ip</td><td>count</td>'
    arr.reverse()
    for r in arr[:-10]:
        i = i+1
        html_str += '<tr><td>no%s</td> <td>%s</td><td>%s</td>'%(i,r[0],r[1])
    html_str+='</table>'

    html_f = open('111.html','w')
    html_f.write(html_str)
    html_f.close()

def start_operate():
    res_list = open_file('log1.log')
    arr = bubble_sort(res_list,10)
    write_html(arr)
start_operate()
