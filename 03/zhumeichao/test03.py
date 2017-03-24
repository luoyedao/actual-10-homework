#!/usr/bin/env python
#coding=utf-8

#找出access.log中所有IP导入到列表
arr=[]
f=open("access.log")
while True:
  text=f.readline()
  if not text:
    break
  arr.append(text.split(" ")[0])
#print arr
#统计IP次数 导入 字典
ip={}
for i in arr:
  if i not in ip:
    ip[i]=1
  else:
    ip[i]+=1
#print ip
#反转统计IP次数 导入 字典列表
tp={}
for k,v in ip.items():
  tp.setdefault(v,[])
  tp[v].append(k)
#print tp
#将字典列表导入html文件中(统计前10)
f = open('tongji2.html','w+')
f.write("<html><table style='border:solid 1px'>")
f.write("<th style='border:solid 2px' width=80px>访问次数</th><th style='border:solid 2px'>访问IP</th>")
count=0
#while count < len(tp.keys()):
while count < 10:
  k=max(tp.keys())
  for v in tp[k]:
    f.write('<tr><td style="border:solid 1px">%s</td><td style="border:solid 1px">%s</td></tr>' % (k,v))
    count+=1
  tp.pop(k)
'''
arr=tp.items()[::-1]
for t in arr:
  f.write('<tr><td style="border:solid 1px">%s</td><td style="border:solid 1px">%s</td></tr>' % (t[0],t[1]))
'''
f.write("</table></html>")
f.close()

