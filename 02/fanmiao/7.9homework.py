#coding=UTF-8
#插入排序

arr=[3,6,2,5,1,32,4,7,33,99]
print arr
for i in range(1,len(arr)):
        j=i
        print "这是第%s次大循环" % i
        while arr[j] < arr[j-1] and j>=1:
                        arr[j],arr[j-1]=arr[j-1],arr[j]
                        j -=1
                        print "这时候的'i'=%s,'j'=%s。序列为%s" %(i,j,arr)

print arr
