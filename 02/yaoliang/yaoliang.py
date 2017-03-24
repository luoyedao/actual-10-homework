array = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45,5000]
for i in range(1,len(array)):
    j = i
    while j>0 and array[j-1]>array[j]:
        array[j],array[j-1] = array[j-1],array[j]
        j -= 1
print array
