#!/usr/bin/env python
#coding:utf-8
import pickle
#增加
def create(username,password):
#	users={'fujinzhou':'123456','pc':'123','wd':'111'}
	users={username:password}
	f=open('userlist.txt','wb')	#pickle模块是以二进制形式存储在文件中，所以必须用二进制方式打开
	pickle.dump(users,f)		#将字典写入文件
	f.close()
#删除
def delete():
	content={}
	f=open('userlist.txt')		#导入字典的时候不能用wb模式
	content=pickle.load(f)		#将文件导入字典中
	f.close
	content.pop('wd')
	f=open('userlist.txt','wb')	#修改后的字典再次写入文件
	pickle.dump(content,f)
	f.close()

#改
def modify(username,password):
	name=username
	password=password
	content={}
	f=open('userlist.txt')
	content=pickle.load(f)
	f.close
	content[name]=password
	f=open('userlist.txt','wb')
	pickle.dump(content,f)
	f.close()


#查所有
def select():
	content={}
	f=open('userlist.txt')
	content=pickle.load(f)
	f.close()
	print content
	for k,v in content.items():
		print '用户信息:%s-->%s'%(k,v)


#查一条
def selectone(username):
	name=username
	content={}
	userinfo={}
        f=open('userlist.txt')
        content=pickle.load(f)
        f.close()
	userinfo[name]=content[name]
	print userinfo
	return userinfo


#create('panda',"123456")
#delete()
modify('panda','654321')
select()
#selectone('pc')
