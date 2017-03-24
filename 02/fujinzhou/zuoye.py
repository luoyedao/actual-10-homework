#coding=UTF-8
#插入排序
array = [3,1,4,2,5,7,6]
length = len(array)
for i in range(length-1):
   for j in range(i+1,length):
	if array[i]>array[j]:
		array[i],array[j]=array[j],array[i]
print array
