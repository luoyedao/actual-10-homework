#!/usr/bin/env python
import os
filenames=[]
for i in os.listdir('/data/python/actual-10-homework/03/fujinzhou'):
	if i.endswith(".py"):
		file=i.rstrip(".py")
		filenames.append(file)
print filenames
