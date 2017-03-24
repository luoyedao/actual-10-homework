#coding:utf-8
#呵呵
#print 'hello world'
#x='hello world'
#print x
#x=raw_input('hello world')
#print x
#int
#print 2+3
#print 1+2*3
#print 8/3
#print 8/3.0
#print 8%3
#str  单双引号无却别
print 'hello world'
print "hello world"
print "I'am pythoner"
print 'I\'am pythoner'
#三个单引号 起声明作用
print '''
this 

is 
a
 test
'''
#字符串拼接
print 'hello '+'reboot'
print 'hello '*2

#字符串格式化
#数字(0, 1, ...)即代表format()里面的元素, 所以可以使用"."调用元素的方法;
x='fujinzhou'
y=22
h='good'
print 'Hi %s I am %d years old ,You are very %s'%(x,y,h)
print 'Hi '+ x +',You are very '+ h +'' 
print ('Hi {0} I am {1} years old,You are very {2}!'.format(x,y,h))
#布尔值 True False  与或非 
#and
#两边都是真，才是真
#print True and True
#print 2>3 and 3>2
#or 或 ,两种情况只要有一种情况
#print True or False
#not 非
#print not False
#print not True

#流程控制
#if True or False:
#    是True 就执行这段代码

if 2<3 or 5<4:
	print 'condition is True'
else:
	print 'condition is False'

name='reboot'
age=20
if name=='reboot':
	if age>10:
		print 'you are %s years old'%(age)
	print 'condition is reboot'
else:
	print 'condition is False'

#while 循环
#while 情况1：
#	里面的代码会一直执行，直到情况1是false
#i=0
#while i<20:
#	print i
#	i+=1
#print 'while is end'
#用户一直输入数字，当输入0时。终止并输出数字之和
count=0
while True:
        i=int(raw_input('please inut your number:'))
        count +=i
        if i==0:
          print count
          break;
count=0
y=raw_input('please input a number')
while int(y)!=0:
  count =count+int(y)
  y=raw_input('please input a number')
print 'the total is %d'%(count)

#用户一直输入数字，当输入为空时。终止并输出平均值
count=0
total=0
y=raw_input('please input a number')
while y:
  count =count+int(y)
  y=raw_input('please input a numbers:')
  total+=1
print 'the total is %s'%(count/total)

#for 循环 专门针对list dict等结构
#arr=['1','2','three']
#for i in arr:
#  print i
#找出列表中js出现的次数
#num=0
#list1=['c','python','js','node','java','js','ruby']
#for i in list1:
#	if i =='js':
#            num+=1
#print num
#numlist=[1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
#max1=0
#max2=0
#for i in numlist:
#	if max1<i:
#		max1=i
#for i in numlist:
#	if max1==i:
#		continue
#	if max2<i:
#		max2=i
#print max1,max2

#i=0
#while True:
#	if i >10:
#		break
#	print i
#	i+=1
#arr=['c','python','js','node']
#for i in arr:
#	if i=='js':
#		continue
#	print i

#d ={'name':'reboot','age':50}
#print d['name'] #根据key 获取 value
#d['age']=50  #修改值
#print d
#d['newkey']='key1' #增加新值
#print d
#total=0
b={}
a=['C','js','python','js','css','js','html','node','js','python','js','css','js','html','node','js','python','js','css','js']
for i in a:
	if i in b:
		b[i]+=b[i]+1
	else:
		b[i]=1
print b
