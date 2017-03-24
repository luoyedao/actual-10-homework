#!/usr/bin/env python
#coding=utf8
arr=[1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45,5000]
tianshi=arr[0]

for i in arr:
    if i > tianshi:
        tianshi=i
print '最大的数:'+str(tianshi)

tmp=0

for x in arr:
    if x != tianshi:
        if x > tmp:
             tmp=x
print '第二大的数：'+str(tmp)
