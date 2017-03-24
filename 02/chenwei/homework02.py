# coding=utf-8
#!/usr/bin/env python


num_list = [1,4,2,7,9,14,11,20,18,37,3,6]

for i in range(len(num_list)):
	min_num = i    ###设定最小的值
	for j in range(i+1,len(num_list)):
		if num_list[min_num] > num_list[j]:
			min_num = j
	
	l = num_list[i]
	num_list[i] = num_list[min_num]
	num_list[min_num] = l
print num_list

