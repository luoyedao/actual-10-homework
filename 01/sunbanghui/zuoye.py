#!/usr/bin/python

list = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45,5000]
m = list[0]
for x in list:
	if x > m:
		n = m
		m = x
	elif x < m and x > n:  
		n = x

print 'the first max number is %s,the second max number is %s' %(m,n)
