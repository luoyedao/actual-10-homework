#!/usr/bin/env python
# coding=utf-8

max1 = 0

max2 = 0

list_num = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45,5000]

for num in list_num:
	if num > max1:
		max1 = num

for num in list_num:
	if num == max1:
		continue
	if num > max2:
		max2 = num	

print "this list first max: %s" % max1
print "this list second max: %s" % max2

