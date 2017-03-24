#!/usr/bin/python
#_*_ coding:utf-8 _*_
#version1 : 利用两次遍历,第一次遍历找到最大值，第二次找到除了最大值以外的第二个值即为第二大的数
list = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45,5000]
max1 = int(0)
for i in list :
#	print i
	if int(i) > max1 :
		max1 = int(i) 

max2 = int(0)
for j in list :
	if int(j) > max2 and int(j) < max1:
		max2 = int(j)

print 'The two max numbers are  %d %d ' %(max1,max2)
