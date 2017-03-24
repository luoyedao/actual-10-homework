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
    return res.items()
#print res



def bubble_sort(arr,time):
#print res_list
#冒泡排序,统计前十
    for j in range(time):
        for i in range(len(arr)-1):
            if arr[i][1]>arr[i+1][1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
    return arr


def write_html(arr):
#拼接字符串
    count=0
    html_str='<table border="1px">'
    arr.reverse()
#(('218.200.66.204', '/data/uploads/2014/0707/12/small_53ba21ee5cbde.jpg'), 1)
    for i in arr[:10]:
        count=count+1
        html_str+='<tr><td>Num%s</td> <td>%s</td> <td>%s</td> <td>%s</td>' %(count,i[0][0],i[0][1],i[1])
#print html_str
    html_str+='</table>'
    html_f=open('res2.html','w')
    html_f.write(html_str)
    html_f.close()

def start_operate():

    res_list=open_file('log1.log')
    sort_list=bubble_sort(res_list,11)
    write_html(sort_list)
start_operate()