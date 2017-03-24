#!/usr/bin/env python

list = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45,5000]

max01 = 0
max02 = 0

for value in list:
    if value > max01:
	max02 = max01
        max01 = value
    elif value != max01:
	if value > max02:
	    max02 = value
print(max01,max02) 
