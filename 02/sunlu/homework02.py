# coding=utf-8
#!/usr/bin/env python


a = [1,4,2,7,9,14,11,20,18,37,3,6]

for i in range(len(a)):
	min_num = i    ###设定最小的值
	for j in range(i+1,len(a)):
		if a[min_num] > a[j]:
			min_num = j
		else:
			print "no jiaohuan"
	
	l = a[i]
	a[i] = a[min_num]
	print a[min_num]
	print a[i]
	a[min_num] = l
	print a

