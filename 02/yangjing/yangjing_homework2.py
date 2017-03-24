# SelectionStore

arr = [13,15,37,89,60,39,12,109,56,72]
n = 0
j = 0
for i in range(arr_length):
	print '++++Compare round %s ++++' %(i+1)

	for j in range(i+1, arr_length):
		print 'compare number is %s' %arr[i]
		print 'neighbor is %s' %arr[j]
		print 'compare scope: %s' % arr[j:arr_length]
		print 'compare %s with %s' % (arr[i], arr[j])
		if arr[i] < arr[j]:
			print 'no swap'
			print 'no swap arr is : %s' % arr
		else:
			print 'swap %s  with %s' % (arr[i], arr[j])
			arr[i], arr[j] = arr[j], arr[i]
			print 'new arr is %s' %arr
			print 'new arr min number is %s' % arr[i]
		n += 1
		print '-----------------------------'
		print 'Total min number is %s' % arr[0]
		print '-----------------------------'

	n += 1

print arr
print n


#Insert sort 

arr = [13,15,37,89,60,39,12,109,56,72]
arr_length = len(arr)
n =0

print 'original arr is %s' % arr
for i in range(arr_length):
	print 'start compare %s' %arr[i]
	for j in range(i+1, arr_length):
		temp = arr[j]
		print 'remainder arr:%s' % arr[j:arr_length]
		print 'temp value is %s' % arr[j]

		if temp < arr[i]:
			# print 'original arr :%s' % arr
			print 'compare value %s is smaller than %s' % (arr[j], arr[i])
			print 'swap temp %s with %s' % (arr[j], arr[i])
			arr[j], arr[i] = arr[i], arr[j]

			print 'new arr :%s' % arr
		else:
			# print 'remained arr:%s' % arr[j:arr_length]
			print 'temp %s is bigger or equal %s,now swap' %(temp, arr[i])
			print 'compared arr :%s' % arr[j:arr_length]
			print 'nex reminder compare arr: %s' % arr[j+1:arr_length]
		n +=1
		print '------------------%s---------------------------' % j
	print '------- Compare round %s finished--------' %i
	print arr
	print '------- Compare round %s finished--------\n' %i
	n += 1

print '----------------compare result ----------------------'
print  arr
print n

