#!/usr/bin/python
#_*_ coding:utf-8 _*_
#version2 : 利用if选择分支来减少遍历列表的次数,用list.index(j) == 0 来将列表中的第一个数赋值给dict[0]当作最大数存放
list = [1,2,3,20000,12,433,1,3,21,2,2,3,111,22,3333,444,111,4,5,777,65555,45,33,45,5000000]
max1 = int(0)
dict = {0: 0 ,1 : 0}
for j in list :
	if int(j) > dict[1] :## 大于第二大的数,进入循环
		if int(j) > dict[0] and list.index(j) == 0:##将列表的的第一个数字赋值给dict[0],dict[0]用来保存最大数
			dict[0] = int(j)
		elif int(j) > dict[0] : ##若列表中的数大于dict[0]，则将这两个数都保存下来
			dict[1] = dict[0]
                        dict[0] = int(j)
		else :
			continue
print "The two max number is %d %d" %(dict[0],dict[1])
