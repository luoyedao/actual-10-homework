#!/usr/bin/env python
f = open('userpassword.txt')
passwd = {}
for i in f.readlines():
    tmp = i.split(':')
    passwd[tmp[0]] = tmp[1]

while True:
    print 'register: 1'
    print 'Login: 2'
    menu = raw_input('Please enter:')
    if menu == str(1):
	print 'You have been to the registration system!'
	username = raw_input('Registered user name:')
	if passwd.has_key(username) == True:
	    print 'The user name is registered, please try again'
	    continue
	password = raw_input('Set the password:')
	passw = raw_input('Again to confirm password:')
	if passw != password:
	    print 'sorry! Password error, please try again'
	    continue
	else:
	    print 'Registration completed!'
	    f = open('userpassword.txt','a+')
	    f.write('%s:%s\n' % (username,password))
	    break
    elif menu == str(2):
	print 'You have entered a log entry!'
	username = raw_input('user:')
	password = raw_input('password:')
	if passwd.has_key(username) == True:
	    paw = passwd[username]
	    if password in paw:
	        print 'Oh my god!Login to complete'
		break
	    else:
		print 'Sorry, authentication failed'
		continue
	else:
	    print 'User name does not exist, please return to register, thank you!'
	    continue
    else:
	print 'Input is wrong, please input again.'
	continue
