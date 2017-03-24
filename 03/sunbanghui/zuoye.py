#!coding=utf-8
# 还存在一个问题，输出的结果只按照IP的次数来计算，实际上会显示出12个IP，需要继续修改才行

file = open('access.log')
ip_dict = {}
for line in file.readlines():
	ip = line.split(' ')[0]
	if ip not in ip_dict:
		ip_dict[ip] = 1
	elif ip in ip_dict:
		ip_dict[ip] +=1
# print ip_dict
ip_dict2 = {}
for key,value in ip_dict.items():
	ip_dict2.setdefault(value,[])
	ip_dict2[value].append(key)
# print ip_dict2
file.close()

count = 0
result = open('access_count.html','a+')
result.write("<html><table style='border:solid 1px'>")
result.write("<th style='border:solid 1px'>count</th><th style='border:solid 1px'>IP</th>")
while count < 10:
    key = max(ip_dict2.keys())
    # print 'IP: {1}, count: {0}' .format(key,ip_dict2[key])
    for value in ip_dict2[key]:
        result.write('<tr><td style="border:solid 1px">%s</td><td style="border:solid 1px">%s</td></tr>' % (key,value))
    ip_dict2.pop(key)
    count = count +1
result.write("</table></html>")
result.close()
