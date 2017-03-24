#!/usb/bin/env python
#coding:utf8
import pickle

def Create(username,password):
#    users = {'pc':'123456','wd':'123','kk':'234'}
    users = {username:password}
    fo = open('users.txt','wb')
    pickle.dump(users,fo)
    fo.close()

def Delete():
    content = {}
    f = open('user.txt')
    content = pickle.load(f)
    f.close
    content.pop('kk')
    f = open('users.txt','wb')
    pickle.dump(content,f)
    f.close()

def Modify(username,password):
    name = username
    password = password
    content = {}
    f = open('users.txt')
    content = pickle.load(f)
    f.close
    content[name] = password
    f = open('users.txt', 'wb')
    pickle.dump(content,f)
    f.close()

def Select():
    content = {}
    f = open('users.txt')
    content = pickle.load(f)
    f.close
    print content
    for k,v in content.items():
        print "用户信息: %s-->%s" % (k,v)

def SelectOne(username):
    name = username
    content = {}
    userinfo = {}
    f = open('users.txt')
    content = pickle.load(f)
    f.close()
    userinfo[name] = content[name]
    print userinfo
    return userinfo

#SelectOne('pc')
Create("panda","123456")

#Create()
#Delete()
Modify("panda",'654321')
Select()
