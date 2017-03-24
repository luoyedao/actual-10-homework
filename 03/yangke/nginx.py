#home work
log_file = "access.log"
html_file = "top_ten.html"
#read log
dic = {}
with open(log_file) as f:
	for line in f:
		ip = line.strip().split()[0]
		if ip not in dic:
			dic[ip] = 1
		else:
			dic[ip] += 1
#k:v => v:k 
new_dic = {}
for k,v in dic.items():
	new_dic.setdefault(v,[])
	new_dic[v].append(k)

#top ten
with open(html_file,'a') as f:
	f.write("<html><table style='border:solid 1px'>")
	f.write("<th style='border:solid 1px'>Num</th><th style='border:solid 1px'>IP</th>")
	count = 0
	while count < 10:
		num = max(new_dic)
		max_ip = new_dic[num]
		if len(max_ip) > 1:
			ip = ",".join(max_ip)
		else:
			ip = max_ip[0]
		f.write("<tr><td style='border:solid 1px'>{0}</td><td style='border:solid 1px'>{1}</td></tr>".format(num,ip))
		new_dic.pop(num)
		count += 1
