numlist=[1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
max1=0
max2=0
for i in numlist:
	if max1<i:
		max1=i
for i in numlist:
	if max1==i:
		continue
	if max2<i:
		max2=i
print max1,max2
