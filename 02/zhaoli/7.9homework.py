arr = [4,2,11,7,6,33,1]
length = len(arr)
print length

for i in range(length-1):
    for j in range(i+1,length):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
print arr