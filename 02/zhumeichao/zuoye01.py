#!/usr/bin/env python
#encoding=utf-8

#插入排序
#在一个有序列表中插入

arr=[1,5,13,45,77,103,200,443]
print arr
newnum=int(raw_input('请输入一个非负整数：'))
head = 0
end = len(arr)-1

while True:
  mid = (head+end)/2
  if newnum >= arr[mid] and newnum <= arr[mid+1]:
    arr.insert(mid+1,newnum)
    break
  elif newnum >= arr[end]:
    arr.append(newnum)
    break
  elif newnum <= arr[head]:
    arr.insert(0,newnum)
    break
  elif newnum > arr[mid+1]:
    head = mid
  else:
    end = mid

print arr

