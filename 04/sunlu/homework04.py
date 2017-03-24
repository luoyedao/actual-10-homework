# coding=utf-8
#!/usr/bin/env python


def get_file():
    dict_up = {}
    with open('test') as f:
        lines = f.readlines()
        try:
            for line in lines:
                dict_up[line.split(':')[0]] = line.split(':')[1].strip()
        except IndexError, error:
            pass
    return dict_up


def write_file(username, password):
    with open('test', 'a+') as f:
        f.write('%s:%s\n' %(username, password))
        return 0


def regsiters():
    while True:
        username = raw_input('plases input username: ').strip()
        if username in get_file().keys():
            print '用户名已存在'
            continue
        password = raw_input('plases input password: ').strip()
        re_password = raw_input('plases input re password: ').strip()
        if password == re_password:
            write_file(username, password)
            return '注册成功'

        else:
            print '两次密码不相同'


def signed():
    c = 0
    print get_file()
    while True:
        c += 1
        username = raw_input('please input username: ').strip()
        if username in get_file().keys():
            password = raw_input('please input password: ').rstrip('\n\r')
            if password == get_file().get(username):
                return '登陆成功'
            else:
                if c == 3:
                    return '账号或密码错误超过三次'
                print '密码错误'
        else:
            print '用户名不存在'

if __name__ == '__main__':
    print '注册'
    print regsiters()
    print '登陆'
    print signed()
