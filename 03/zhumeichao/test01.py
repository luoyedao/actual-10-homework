#!/usr/bin/env python
#coding=utf8

#找出目录下面以py结尾的文件的文件名，并导入列表

import os
filelist=[]
for filename in os.listdir('/RebootPY/class01/'):
  if filename.endswith(".py"):
     filelist.append(filename.rstrip('.py'))

print filelist
