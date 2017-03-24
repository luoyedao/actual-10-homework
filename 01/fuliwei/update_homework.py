#/usr/bin/python
#coding:utf-8
#discription:第一节课讲解作业后代码优化.

list = [1,2,5000000,3,20000,12,433,1,3,21,2,2,3,111,22,3333,444,111,4,5,777,65555,45,33,45,5000000]
d = {'max_1': 0 ,'max_2' :0}
#print d['max_1'] ,d['max_2'] 

for i in list :
	if i >  d['max_1'] :
		d['max_2'] = d['max_1'] 
		d['max_1'] = i
		#最大值换成i,并把上一个最大值赋值给第二大的值
	elif i > d['max_2'] : # 完整条件是 d['max_2']  < i <  d['max_1'],但是可以省略i<d['max_1']
		d['max_2'] = i
		#直接将i赋值给d['max_2'] 
	'''
	else :    #不做任何操作
	#可以省略
	'''

print d['max_1'] ,d['max_2']
