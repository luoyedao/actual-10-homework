#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
max_1 = 0
max_2 = 0

list = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,5000,65555,45,33,45]
for i in list:
    if i > max_1:
        max_1 = i
    elif i != max_1 and i > max_2:
        max_2 = i
print ('max_1 is %s , max_2 is %s') % (max_1,max_2)
