def insertion_sort(seq):
    if len(seq) > 1:
        for i in range(1,len(seq)):
            while i > 0 and seq[i] < seq[i-1]:
                t = seq[i]
                seq[i] = seq[i-1]
                seq[i-1] = t
                i = i -1

a = [45,67,23,78,34,975,223]

insertion_sort(a)

print a
