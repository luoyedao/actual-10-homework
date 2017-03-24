#!/usr/bin/env pyton
#Create by miaojun

l=[1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45,5000]
def maopao_sort(l):
    for i in range(len(l),0,-1):
        for j in range(len(l)-1):
            if l[j] > l[j+1]:
                tmp = l[j]
                l[j] = l[j+1]
                l[j+1] = tmp

    print("result: " + str(l))

maopao_sort(l)
print("the number in l top 2 is : %d,%d" %(l[-1],l[-2]))
