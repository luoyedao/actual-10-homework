#!/usr/bin/env python
#coding:utf-8

a = [1,2,3,4,5,565,334,7677,8,33,667]
b = 0
c = 0
for i in a:
    if i > b:
        b = i 
print "The largest number is %d" %b
a.remove(b)
for i in a:
    if i > c:
        c = i 
print "The second largest number is %d" %c

