def user_list():
    d = {}
    with open('userpasswd.txt') as f:
        for line in f:
            temp = line.strip().split(":")
            d.setdefault(temp[0],temp[1])
   # print d
    return d


def write(name,passwd):
    with open('userpasswd.txt','a') as f:
        f.write('%s:%s\n'%(name,passwd))

def register():
#    fo = open('userpasswd.txt','a+')

    while True:
        name = raw_input('please input your name: ').strip()
        if not name:
            print 'the name can not be null'
            continue
        elif name in user_list():
            print 'User already exists'
        else:
            passwd  = raw_input('please input your passwd: ').strip()
            repasswd = raw_input('please input your passwd again: ').strip()
            if not passwd or passwd != repasswd:
                print 'wrong passwd'
                continue
            else:
                write(name,passwd)
                print 'register successfully'
                break

def login():
    name = raw_input('please input your name: ').strip()
    passwd = raw_input('please input your passwd: ').strip()
    d = user_list()
    if not name in d:
        print 'user is not exist!please input: '
    elif d[name] != passwd:
        print 'name or passwd is wrong!pleas input: '
    else:
        print 'login successfully!'

def start():
    i = raw_input('please choose login or register: ')
    if i != 'login' and i != 'register':
        print 'please choose one'
    elif i == 'login':
        login()
    else:
        register()

start()