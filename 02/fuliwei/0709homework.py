#!/usr/bin/python
#coding:utf-8
#filename : 0709homework.py

#discriptions:用插入排序的方法对列表进行排序.
test_list = [69, 471, 106, 66, 149, 983, 160, 57, 792, 489, 764, 589, 909, 535, 972, 188, 866, 56, 243, 619] 
test_len = len(test_list)
 
for out_loop in range(1,test_len) :
#    print 'x' * 30
    tmp_value = test_list[out_loop]
    in_loop = out_loop
#    print  tmp_value ,test_list[out_loop] ,in_loop ,out_loop
    while ( in_loop > 0 ) and ( test_list[in_loop-1] > tmp_value ) :
        test_list[in_loop] , test_list[in_loop-1] =test_list[in_loop-1] , test_list[in_loop]
        in_loop = in_loop - 1
print  test_list
