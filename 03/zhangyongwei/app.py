# coding: utf-8

logfile = open('access.log', 'r')

result = {}
for i in logfile:
    ip = i.split()[0]
    if ip in result:
        result[ip] += 1
    else:
        result[ip] = 1
logfile.close()

res = {}
for k,v in result.items():
    res.setdefault(v, [])
    res[v].append(k)

html = open('statistic.html', 'a+')
html.write("<html><table style='border:solid 1px'>")
html.write("<th style='border:solid 1px'>访问IP</th><th style='border:solid 1px'>访问次数</th>")
count = 0
loop = len(res.keys())
while count < 10:
    key = max(res.keys())
    for word in res[key]:
        html.write("<tr><td style='border:solid 1px'>%s</td><td style='border:solid 1px'>%s</td>" % (word, key))
        count += 1
    res.pop(key)

html.write("</table></html>")
html.close()
