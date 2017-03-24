#!/usr/bin/env python
#coding:utf-8
def userinfo():
    res={}
    with open('user.txt') as f:
        for line in f:
            tmp=line.strip().split(":")
            res[tmp[0]]=tmp[1]
    return res
#print userinfo()

def adduser(user,password):
	with open('user.txt','a+') as f:
		f.write("%s:%s\n"%(user,password))

def checkinfo (user,password):
	if len(user) !=0  and len(password)!=0:
		return True

def deluser(user):
	dic=userinfo()
	del dic[user]
	userstr="\n".join(map(lambda x: ":".join(x),dic.items()))
	with open('user.txt','w+') as f:
		f.writelines("%s\n"%userstr)
'''
dic={'123123123': '123123123123', 'fujinzhou': '123', 'reboot': '123', 'fyhubzgiy': '123123', 'junkai': '123'}
userstr="\n".join(map(lambda x: ":".join(x),dic.items()))
user1=map(lambda x: ":".join(x),dic.items())
user2=(lambda x: ":".join(x),dic.items())

print user2
[('123123123', '123123123123'), ('junkai', '123'), ('fujinzhou', '123'), ('fyhubzgiy', '123123'), ('reboot', '123')])

print user1
['123123123:123123123123', 'junkai:123', 'fujinzhou:123', 'fyhubzgiy:123123', 'reboot:123']

"\n".join(user2)
'123123123:123123123123\njunkai:123\nfujinzhou:123\nfyhubzgiy:123123\nreboot:123'

print userstr
123123123:123123123123
junkai:123
fujinzhou:123
fyhubzgiy:123123
reboot:123
'''
