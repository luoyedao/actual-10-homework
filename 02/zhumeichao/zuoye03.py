#!/usr/bin/env python
#encoding=utf-8

#冒泡排序

arr=[3,1,45,17,133,299,48,100,4]
print "初始序列："
print arr
for j in range(len(arr)-1):
  print "第 %s 次循环：" % (j+1)
  for i in range(len(arr)-1-j):
    print "第 %s 次冒泡：" % (i+1)
    if arr[i] > arr[i+1]:
      arr[i],arr[i+1] = arr[i+1],arr[i]
    print arr

#print arr
