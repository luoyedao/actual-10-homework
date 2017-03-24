#!/usr/bin/env python
#coding=utf-8

#字符串、列表、字典之间的转换

text="who have touched their lives Love begins with a smile grows with a kiss and ends with a tear The brightest future will always be based on a forgotten past you can’t go on well in lifeuntil you let go of your past failures and heartaches"

#字符串切割 --》列表
word=text.split(" ")
print word
#统计字符串出现次数 --》字典
d={}
for i in word:
  if i not in d:
    d[i]=1
  else:
    d[i]+=1
print d
#反转统计次数对应字符串 --》字典嵌套列表
dr={}
'''方法一：
for k,v in d.items():
  if v not in dr:
    dr[v]=[k]
  else:
    dr[v].append(k)
'''
#方法二：
for k,v in d.items():
  dr.setdefault(v,[])
  dr[v].append(k)
print dr
#对字典中key次数进行排序 --》列表
print dr.items()[::-1]

#显示在html文件中
f = open('tongji.html','w+')
f.write("<html><table style='border:solid 1px'>")
f.write("<th style='border:solid 2px' width=80px>出现次数</th><th style='border:solid 2px'>单词汇总</th>")
#列表取值
arr=dr.items()[::-1]
for t in arr:
  f.write('<tr><td style="border:solid 1px">%s</td><td style="border:solid 1px">%s</td></tr>' % (t[0],t[1]))

'''
#字典取值
count = 0
while count < 4:
    key = max(dr.keys())
    print "出现了%s次的单词：%s" % (key,dr[key])
    for word in dr[key]:
        f.write('<tr><td style="border:solid 1px">%s</td><td style="border:solid 1px">%s</td></tr>' % (key,word))
    dr.pop(key)
    count = count +1
'''
f.write("</table></html>")
f.close()
