#/usr/bin/python3
#encoding=utf-8

lt=[1,2,3,2,12,3,1,3,21,2,2,3,4111,22,444,111,3333,4,5,777,65535,45,33,45,5000]

m=n=0
for i in lt:
  if i>m:
    n=m
    m=i
  elif i>n:
    n=i
print m,n
