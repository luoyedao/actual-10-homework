#!/usr/bin/python

'''
Seek the maximum two values in the list

'''
#方法一：

_list=[1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
max_1=0
max_2=0

print "list: %s" % _list
print "Seek the maximum two values in the list"
print "-" * 50

for i in _list:
    for j in _list:
    	if max_1 < j:
            max_1 = j
    	if max_1 != i and i > max_2: 
            max_2 = i

print "1,The two maximum values in the list are: %s and %s" % (max_1,max_2) 

#----------------------------------------------------------------------------------------
#方法二：

for i in _list:
    if i > max_1:
        max_2 = max_1
        max_1 = i

print "Method 2"
print "2,The two maximum values in the list are: %s and %s" % (max_1,max_2)

#----------------------------------------------------------------------------------------

