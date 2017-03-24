x = 0
arr = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45,5000]
for i in  arr:
    if x < i:
        x = i
print '1st number is %s' %x
location = list.index(arr,x)
#arr.pop(location)
arr.remove(x)

x = 0
for i in  arr:
    if x < i:
        x = i
print '2st number is %s' %x
