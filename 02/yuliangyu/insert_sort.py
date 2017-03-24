def insert_sort(list):
    if len(list) > 1:
        for i in range(1,len(list)):
            while i > 0 and list[i] < list[i-1]:
                list[i], list[i-1] = list[i-1], list[i]
                i = i -1

l = [45,67,23,726,10,7,4,975,223]
insert_sort(l)
print l