arr = [6,5,3,1,8,7,7,2,4]
for i in range(len(arr)):
	for j in range(i):
		if arr[j] > arr[i]:
			arr[j],arr[i]=arr[i],arr[j]
print arr
