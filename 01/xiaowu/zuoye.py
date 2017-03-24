li=[1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45,5000]
max=0
max2=0

for num in li:
        if num>max:
                max=num
for num2 in li:
        if num2==max:
                continue
        elif num2>max2:
                max2=num2

print 'max : %d , second : %d'%(max,max2) 
