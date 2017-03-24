a=[1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,4444,111,4,5,777,65555,45,33,45,5000]
b=0
c=0
for i in a:
    if b<i:
        b=i
for x in a:        
    if  x==b:
        continue
    if  x>c:
        c=x
print  'The max number is ' + str(b)
print  'The second max number is ' + str(c)
