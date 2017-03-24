#!/usr/bin/env python
#encoding=utf-8

#插入排序
#从空列表开始一直插入

arr=[]
head = 0
end = 0

while True:
  print arr
  newnum=int(raw_input('请输入一个非零整数：'))
  while True:
    mid = (head+end)/2
    end = len(arr)-1
    if len(arr) == 0:
      arr.append(newnum)
      break
    elif len(arr) == 1 and newnum < arr[0]:
      arr.insert(0,newnum)
      break
    elif newnum < arr[head]:
      arr.insert(0,newnum)
      break
    elif newnum > arr[end]:
      arr.append(newnum)
      break
    elif newnum >= arr[mid] and newnum <= arr[mid+1]:
      arr.insert(mid+1,newnum)
      break
    elif newnum > arr[mid+1]:
      head = mid
    elif newnum < arr[mid]:
      end = mid
