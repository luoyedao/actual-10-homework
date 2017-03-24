def dictionary(filename):
	d = {}
	with open(filename) as f:
		content = f.readlines()
		for user in content:
			name = user.rstrip("\n").split(":")[0]
			d[name] = user.rstrip("\n").split(":")[1]
		return d

def register(filename):
	res_dict = dictionary(filename)
	while True:
		name = raw_input("input your name:").rstrip(" ")
		password = raw_input("input your password:").rstrip(" ")
		repass = raw_input("input the password again:").rstrip(" ")
		if len(name) == 0:
			print "username can not be empty"
			continue
		elif name in res_dict:
			print "already has the name, register error"
			continue
		elif len(password) == 0 or password != repass:
			print "password error"
			continue
		else:
			print "register success"
			break
	with open(filename, "a+") as f:
		f.write("%s:%s\n" %(name,password))
	
def login(filename):
	res_dict = dictionary(filename)
	count = 0
	while True:
		count += 1
		if count > 3:
			print "wrong for 3 times"
			break
		name = raw_input("input your name:").rstrip(" ")
		password = raw_input("input your password:").rstrip(" ")
		if name not in res_dict:
			print "wrong name"
			continue
		elif password != res_dict[name]:
			print "wrong password"
			continue
		else:
			print "login success"
			break

def user(filename):
	choice = raw_input("input your choice: login or register:").rstrip(" ")
	if choice == "login":
		login(filename)
	elif choice == "register":
		register(filename)
	else:
		print "wrong choice"
		
user("user.txt")