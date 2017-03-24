#!/usr/bin/env python
#coding=utf-8

#函数封装日志统计及排序

#提取日志某列，并统计次数及排序
def OpenLog(name,y=0,z=0):
  d={}
  with open(name) as f:
    for line in f:
      part=line.strip("\n").split(' ')
      k=part[0]
      if y>0 and z>0:
        k=part[0],part[y],part[z]
      d[k]=d.setdefault(k,0)+1
  return sorted(d.items(),key=lambda x:x[1],reverse=True)

def AddHtml(arr):
  seg='<table border="1px">'
  if len(arr[0][0]) != 3:
    for j in arr:
      seg+='<tr><td>%s</td> <td>%s</td></tr>' % (j[0],j[1])
  else:
    for j in arr:
      seg+='<tr><td>%s</td> <td>%s</td> <td>%s</td> <td>%s</td></tr>' % (j[0][0],j[0][1],j[0][2],j[1])
  seg+='</table>'
  with open("/web/site/pytest/index.html",'w+') as w:
    w.write(seg)

#默认IP第一列IP统计，若需要IP加其他元素合并统计，则制定列号 y=  
tongji=OpenLog(name='access.log',y=6,z=8)
AddHtml(tongji)

