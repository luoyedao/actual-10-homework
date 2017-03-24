#!/usr/bin/env python
#coding=utf-8

arr1=[34,5,89,35,74,2,20,15]
arr2=[('aa',34),('bb',5),('cc',89),('dd',35),('ee',74),('ff',2),('gg',20),('hh',15)]

print sorted(arr1,reverse=True)
print sorted(arr2,key=lambda x:x[1],reverse=True)

def my_sort(arr,key=lambda x:x,reverse=False):
  for i in range(len(arr)-1):
    for j in range(len(arr)-1-i):
       if key(arr[j]) > key(arr[j+1]):
         arr[j],arr[j+1] = arr[j+1],arr[j]
  if reverse == True:
    return arr[::-1]
  return arr

def sort_f1(x,n=1):
  return x[n]

print my_sort(arr1)
print my_sort(arr1,reverse=True)
print my_sort(arr2,reverse=True)
print my_sort(arr2,key=sort_f1,reverse=True)
