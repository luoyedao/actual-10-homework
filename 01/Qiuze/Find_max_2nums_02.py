#!/usr/bin/env python
# coding=utf-8

arr=[1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45,5000]

# 定义B为最大值
b=0
# 定义C为第二大值
c=0

for num in arr:
    # 当每一个num值都比b大的时候，将b的值赋予给c，num的值赋给b；循环到最后，则b的值为最大值，c的值为第二大值
    if num > b:
        c=b
        b=num

    # 当每一个num值都比b小的时候，即b的值就是最大值
    elif num < b:

        # 已经知道b是最大值，接下来获取第二大值，获取第二大值的有两条件：1.比list里的值都大 2.不能等于b
        if num > c and num != b:
            c=num

print "The max number is %s" % (b)
print "The second max number is %s" %(c)
