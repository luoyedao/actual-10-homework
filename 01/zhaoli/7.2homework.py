list = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45,5000]
max1=0
max2=0

for num in list:
    if num > max1:
        max1=num
for num in list:
    if num==max1:
        continue
    if num > max2:
        max2=num
print "The first num is %s"%(max1)
print "The second num is %s"%(max2)
