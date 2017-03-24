#!/usr/bin/env python

arr = [45,7,2]
for i in range(len(arr)-1):
    index = i
    for j in range(i+1,len(arr)):
	if arr[index] > arr[j]:
	    index = j
        tmp = arr[i]
        arr[i] = arr[index]
	arr[index] = tmp
print arr 
