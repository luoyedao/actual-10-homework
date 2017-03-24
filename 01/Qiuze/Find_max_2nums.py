#!/usr/bin/env python
# coding=utf-8

arr=[1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45,5000]
b=0
c=0

# 获取序列里最大的值
for num in arr:
    if num > b:
        b=num

# 获取序列里第二大的值
for num in arr:
    # 第二大的值必须满足：1.比list里所有值都大 2.不等于最大值
    if num > c and num != b:
        c=num

print "The max number is %s" % (b)
print "The second max number is %s" %(c)
