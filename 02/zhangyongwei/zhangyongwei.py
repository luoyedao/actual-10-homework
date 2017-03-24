#coding: utf-8
#selection sort
arr = [3,8,1,12,20,2,9,7,6]

for i in range(len(arr)-1):
    min = arr[i]
    for j in range(i+1,len(arr)):
        if min > arr[j]:
            min, arr[j] = arr[j], min
    arr[i] = min
print arr
