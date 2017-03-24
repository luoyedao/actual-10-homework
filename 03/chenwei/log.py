#!/usr/bin/env python
#coding=utf8


def oper_file(file_name):
	res = {}
	with open(file_name) as f:
		for line in f:
			tmp = line.split(' ')
			ip,url=tmp[0],tmp[6]
			res[(ip,url)] = res.get((ip,url),0)+1
	return sorted(res.items(),key=lambda x:x[1],reverse=True)

def write_html(arr):
	r = 0
	html_str = '<table border="1px">'
	arr.reverse()
	for i in arr[:10]:
		r+=1
		html_str += '<tr><td>NO%s</td> <td>%s</td><td>%s</td><td>%s</td></tr>'%(r,i[0][0],i[0][1],i[1])
	html_str+='</table>'

	html_f = open('res1.html','w')
	html_f.write(html_str)
	html_f.close()

res_list = oper_file('log1.log')
write_html(res_list)


