#coding: utf-8

l1 = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45,5000]

a = 0
b = 0
for i in l1:
    if i > a:
        a = i
l2 = l1
l2.remove(a)
for j in l2:
    if j > b:
        b = j
print 'The first max num is %s and the second max num is %s' % (a,b)
