
def get_user():
    with open('user.txt') as f:
        user_dict = {}
        for line in f.readlines():
            user=line.split(":")[0]
            user_dict[user]=line.split(":")[1].strip("\n")
    return user_dict

def check_user(name,pwd):
    user_dict = get_user()
    if user_dict.has_key(name) and pwd == user_dict[name]:
        return 0
    else:
        return 1

def add_user(name,pwd):
    with open('user.txt','a+') as f:
        f.write('%s:%s\n' % (name,pwd))
    return

