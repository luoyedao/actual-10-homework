def oper_file(filename):
	with open(filename) as f:
		for line in f:
			print line
		# print f.readlines()

oper_file('log.log')

