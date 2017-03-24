a = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45,5000]
max = 0 
max2 =0

for i in a:
    if i > max:
	max = i
for j in a:
    if j == max:
        continue
    if j > max2:
	max2=j
print 'The max number is %s' %(max)
print 'The second max number is %s' %(max2)
