#!/usr/bin/env python
#encoding=utf-8

#插入排序
#在一个有序列表中插入
#使用交叉替换，代替insert函数

arr=[1,5,13,45,77,103,200,443]
print arr
newnum=int(raw_input('请输入一个非负整数：'))
head = 0
end = len(arr)-1

while True:
  mid = (head+end)/2
  if newnum >= arr[mid] and newnum <= arr[mid+1]:
    f=arr[mid+1]
    arr[mid+1]=newnum
    arr.append(arr[end])
    for i in range(len(arr)-1-mid-1):
      arr[mid+1+i+1],f=f,arr[mid+1+i+1]
    break
  elif newnum >= arr[end]:
    arr.append(newnum)
    break
  elif newnum <= arr[head]:
    f=arr[0]
    arr[0]=newnum
    arr.append(arr[end])
    for i in range(len(arr)-1):
      arr[i+1],f=f,arr[i+1]
    break
  elif newnum > arr[mid+1]:
    head = mid
  else:
    end = mid

print arr

