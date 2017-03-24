#encoding: utf-8
import json

def login_required(username, password):
    with open('db.txt') as f:
        for user in f:
            if user.split(':')[1].split(',')[0] == username and user.split(':')[2].strip('}\n') == password:
                return '登录成功'
        return '登录失败，用户或密码错误'

def add_user(username, password):
    if check_user(username):
        return "用户名已存在"
    elif username == '' or password == '':
        return '用户名和密码不能为空'
    else:
        with open('db.txt', 'a') as f:
            f.write("{'name':%s,'password':%s}\n" %(username, password))
        return '用户添加成功'

def check_user(username):
    with open('db.txt') as f:
        for user in f:
            if user.split(':')[1].split(',')[0] == username:
                return True
            else:
                return False

def uesrs():
    users = []
    with open('db.txt') as f:
        for user in f:
            username = user.split(':')[1].split(',')[0]
            password = user.split(':')[2].strip('}\n')
            users.append({'username':username, 'password':password})
    return users

def delete_users(username):
    tmp = []
    with open('db.txt') as f:
        for user in f:
            tmp.append(user)
        tmp1 = []
        for item in tmp:
            if item.split(':')[1].split(',')[0] != str(username):
                tmp1.append(item)

    with open('db.txt', 'w') as f:
        for i in tmp1:
            f.writelines(i)