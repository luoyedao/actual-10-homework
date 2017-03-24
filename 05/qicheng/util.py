#!/bin/env python
#encoding:utf-8

file_data = {}


def update_data():
	with open('user.txt') as f:
		for line in f:
			if not line:
				continue
			tmp=line.split(':')
			file_data[tmp[0]] = tmp[1].replace('\n','')
def update_file():
	user_list = []
	for user,pwd in file_data.items():
		user_list.append('%s:%s'%(user,pwd))
	print user_list
	with open('user.txt','w') as f:
		f.write('\n'.join(user_list))