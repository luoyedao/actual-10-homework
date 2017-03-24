#!/usr/bin/env python

first = 0
second = 0
list = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45,5000]

for y in list:
    if y > first:
        first = y

for y in list:
    if y == first:
        continue
    if y > second:
        second = y
		
print "this first max: %s" %first
print "this second max: %s" %second
