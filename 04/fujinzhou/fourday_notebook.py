#!/usr/bin/env python
#coding:utf-8
#函数的概念： 函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段

#定义函数的规则：函数代码块以def 关键字开头，后面接函数标识符名称和圆括号（）
#任何传入参数和自变量 必须放在圆括号中间，圆括号中间可以用于定义参数
#函数的内容以冒号起始，并且缩进。
#return（表达式）结束函数，选择性的返回一个值给调用方。

#小栗子
def hello(name):
    print "hello %s" %(name)
hello(name="fujinzhou")
hello(name="reboot")

#不定长参数
#惨了星号的变量名会存放所有未命名的变量参数
def prininfo(arg1,*vartuple):
    print "输出 ："
    print arg1
    print vartuple
    return
prininfo(10,20,30,40)

#匿名函数lambda 是一个表达式
#lambda [arg1 [,arg2,.....argn]]:语句

#函数说明
sum1=lambda arg1,arg2:arg1*arg2
#调用sum1函数
print "相乘后的值为:",sum1(10,29)

#return 语句
#return语句[表达式]退出函数，选择性地向调用方返回一个表达式。不带参数值的return语句返回None。

#函数说明
def count(arg1,arg2):
    total=arg1+arg2
    print "函数内：",total
    return total
#调用count函数
total=count(10,20)
print "函数外:",total

#变量作用域 一个程序的所有变量并不是在哪个位置都可以访问的。访问权限取决于这个变量在哪里赋值

#全局变量和局部变量
#定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域
#局部变量只能在被声明的函数内部访问，全局变量在整个程序都可以访问

#这是一个全局变量
total=0
def sum(arg1,arg2):
    total=arg1+arg2
    print "函数内部是局部变量：",total
    return total

sum(10,20)
print "函数外部是全局变量:",total


#函数的参数就是个变量
#定义函数的时候，使用关键字参数，可以指定默认值
def hello(name='reboot',age=1):
    return 'hello %s,your age is %s' %(name,age)
print hello('reboot',3)
print hello(3,'reboot')
#print hello(age=3,name='reboot')
print hello('reboot')
def f(n):
    count=1
    for i in range(1,n+1):
        count=i*count
    return count
print f(5)

# *号开头的参数，收集所有的剩余参数（位置参数）,组装成元组
# **开头的参数，收集所有剩下参数（关键字参数），组装成字典
def sum(name,*num):
    print num
    return sum
sum(111,2222,333)

#练习、函数add_all，把传入的所有参数求和并打印

def count(*add_all):
    count=0
    for i in add_all:
        count+=i
    return count
print count(1,2,3,4,5)

def name(**dict):
    print dict
name(name='reboot',teach='pc',age=30)

#排序
def my_sort(arr,sort_fn):
    for j in range(11):
        for i in range(len(arr)-1):
            if sort_fn(arr[i])>sort_fn(arr[i+1]):
                arr[i],arr[i+1]=arr[i+1],arr[i]
    return arr

arr=[1,22,3,55,99,0,4,7]
def sort_fn1(data):
    return data
print my_sort(arr,sort_fn1)

arr2=[('xiaoming',29),('xiaohua',44),('xiaohong',99)]
def sort_fn2(data):
    return data[1]
print my_sort(arr2,sort_fn2)

arr3=[{'name':'xiaohong','age':22},{'name':'pc','age':18},{'name':'xiaohua','age':99}]
def sort_fn3(data):
    return data['age']
print my_sort(arr3,sort_fn3)
print sorted(arr3,key=sort_fn3)  #sorted（待排序的list，決定根据元素的那個排序）

#lambda 没有名字的函数,特别简单的函数，只有return语句的函数
#语法 lambda 返回值
def hello(x):
    return x[1]
print hello([1,2])

hello=lambda  x:x[1]
hello1=lambda  x:x[0]+x[1]
hello2=lambda x,y:x*y
print hello([1,2])
print hello1([3,4])
print hello2(2,3)

#遍历list的方法
arr=['hello','world','111']
for index,value in enumerate(arr):
    print index,value

for i in range(len(arr)):
    print i,arr[i]
#遍历字典
#for in 遍历key 然后通过key查找value
arr1={'name':'reboot','age':12,'job':'devops'}
for key in arr1:
    print key,arr1[key]
##for in 遍历key，value
for key,value in arr1.items():
    print key,value
