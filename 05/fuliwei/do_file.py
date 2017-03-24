#!/usr/bin/python
#coding:utf-8

def get_Users(filename,mode="r"):
	users_dict = {}
	with open(filename,mode) as do_f:
		for line in do_f:
			k ,v = line.strip("\n").split(":")
			users_dict[k] = v 
	return users_dict
#print get_Users()

def add_user(filename,username,password ):
	tmp_dict = get_Users(filename)
	tmp_dict[username] = password
	with open(filename,"a+") as tmp_f:
		tmp_f.write("{}:{}\n".format(username,password)) 
	return tmp_dict


def del_Users(filename,tmp_dict):
	with open(filename,"w+") as write_f:
		for i in tmp_dict.keys():
			write_f.write("%s:%s\n" %(i,tmp_dict[i]))
	return "Done"
if __name__ == "__main__" :
	tmp_dict = get_Users()
	del tmp_dict["mmm"]

	print del_Users("tmp_user.txt",tmp_dict)
	
