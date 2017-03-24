#!/usr/bin/python
#-*- coding: UTF-8 -*-
arr = [4,2,11,7,6,33,1]
for i in range(len(arr)-1):
    print ('i = %s,------------------')%(i)
    for j in range(i+1,len(arr)):
        if arr[i] > arr[j]:
            print arr
            print 'j = %s,arr[%s]>arr[%s]'%(j,i,j)
            arr[i], arr[j] = arr[j], arr[i]
            print arr
        else:
            print 'j = %s,arr[%s]<=arr[%s]no change'%(j,i,j)
            print arr
