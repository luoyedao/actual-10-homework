#coding=UTF-8

dict_old={}
ips=[]

#读取文件，导入字典
f=open('/Users/mario/Desktop/fanmiao/day_3/access.log')
content = f.readlines()

for line in content:
	ip = line.strip("\n").split()[0]
 	if ip not in dict_old:
		dict_old[ip] = 1
	else:
		dict_old[ip] += 1

#key 和value 互换位置
dict_new={}
for k,v in dict_old.items():
	dict_new.setdefault(v,[])
	dict_new[v].append(k)

f.close

#打印成页面显示
count = 0
fo = open('/Users/mario/Desktop/fanmiao/day_3/tongji.html','a+')
fo.write("<html><table style='border:solid 1px'>")
fo.write("<th style='border:solid 1px'>number</th><th style='border:solid 1px'>IP</th>")
while count < 10:
    key = max(dict_new.keys())
    print "出现了%s次的单词：%s" % (key,dict_new[key])
    for word in dict_new[key]:
        fo.write('<tr><td style="border:solid 1px">%s</td><td style="border:solid 1px">%s</td></tr>' % (key,word))
    dict_new.pop(key)
    count = count +1
fo.write("</table></html>")
fo.close()

f.close()

