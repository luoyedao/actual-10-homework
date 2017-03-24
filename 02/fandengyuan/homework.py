arr = [3,1,5,9,2,11,7]
arr0 = []

for i in range(len(arr)):
        arr0.append(int(arr[i]))
        m = len(arr0)-1

        while m >= 1 and arr0[m] < arr0[m-1]:
                arr0[m],arr0[m-1] = arr0[m-1],arr0[m]
                m = m - 1

print arr0
