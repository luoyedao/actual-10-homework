#!/usr/bin/env python
#coding=utf8

dict={}
def writefile(username,userpassword):
    with open('user.txt','a') as f:
        f.write("%s:%s\n"%(username,userpassword))
  
def readfile():
    with open('user.txt','r') as f:
        content=f.readlines()
    for user in content:
        tmp = user.rstrip("\n").split(':')
        name,dict[name]=tmp[0],tmp[1]
    return dict
    
def checkuser(username,userpassword):
    userdict=readfile()
    if username not in userdict:
        return 'nouser'
    elif userpassword == userdict[username]:
        return 'yes'
    elif not userpassword == userdict[username]:
        return 'passwordworng'
    else:
        return 'error warning'

def checkegister(username,userpassword):
    while True:
        if checkuser(username,userpassword) == 'nouser':
            replyuser=raw_input('注册用户：%s,密码为：%s \n是否确认(Y/N)？'%(username,userpassword)).strip()
            if replyuser == 'Y' or replyuser == 'y':
                writefile(username,userpassword)
                if checkuser(username,userpassword) == 'yes':
                    print '用户：%s注册成功，请牢记密码！'%(username)
                    break
                else:
                    print '用户注册失败，请重试' 
            else:
                break
        else:
            print '注册失败，用户已存在！！！\n请勿重复注册!!1'
            break

def inputuserpass(tmpselect):
    username=raw_input( "请输入用户名: ").strip()
    while not username:
         print '当前select:%s,username为:%s'%(tmpselect,username) 
         username=raw_input( "\n用户名不能为空\n请重新输入用户名: ").strip()
         continue
    print '当前select:%s,username为:%s'%(tmpselect,username)
    userpassword=raw_input('请输入密码:').strip()
    if tmpselect == '1':
        while not userpassword:
            userpassword=raw_input('\n密码不能为空！\n请输入密码:').strip()
            continue
    elif tmpselect == '2':
        reuserpassword=raw_input('请再次输入密码:').strip()
        while not reuserpassword == userpassword or not userpassword or not reuserpassword:
            print '\n两次密码不一致或为空,请重新输入!'
            userpassword=raw_input('请输入密码:').strip()
            reuserpassword=raw_input('请再次输入密码:').strip()
            continue
    d=[username,userpassword]
    return d

def printcheckuser(username,userpassword):
    if checkuser(username,userpassword) == 'nouser':
        print "\n用户名不存在"
    elif checkuser(username,userpassword) == 'yes':
        print '\n登陆成功！\n欢迎%s用户！！'%(username)
    elif checkuser(username,userpassword) == 'passwordworng': 
        print '\n登陆失败，密码错误！请重试!!'
    else:
        print '\n输入异常错误！！'    
        exit(1)

def useruse(select):
    if select == '1' or select == '2':
        tmp1dict=inputuserpass(select)
        username,userpassword=tmp1dict[0],tmp1dict[1]
       
    if select == '1':
        printcheckuser(username,userpassword)

    elif select == '2':
        checkegister(username,userpassword)
        
    elif select == '3':
        print 'See you!'
        exit(0)

    else:
        print '无效'

printwelcome=(lambda x:x)("\n欢迎使用!\n请选择功能：\n登陆请输入1,  注册请输入2,   退出请输入3")

while True:
    print printwelcome
    select=raw_input("请选择: ").strip()
    useruse(select)

