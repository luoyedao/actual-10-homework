# coding=utf-8
# !/usr/bin/env python
d = {}


def get_file():
    with open('test.txt') as f:
        f1 = f.readlines()
        try:
            for i in f1:
                username = i.split(':')[0].strip()
                password = i.split(':')[1].strip()
                d[username] = password
        except IndexError, E:
            return E
        finally:
            return d


def write_file(username, password):
    with open('test.txt', 'a+') as f:
        f.write('%s:%s\n' % (username, password))
        return 0


def del_file(username):
    file_dict = get_file()
    if username in file_dict.keys():
        del file_dict[username]
        with open('test.txt', 'w+') as f:
            for keys, values in file_dict.iteritems():
                f.write('%s:%s\n' % (keys, values))
            return 0
    else:
        return 1

