#!/usr/bin/env python
# coding=utf-8
# coding=utf-8
def zdpx(filename):
    ips = []
    dict_ip = {}
    dict_ips = {}
    with open(filename) as f:
        nginx_lines = f.readlines()
        for nginx_line in nginx_lines:
            ips.append(nginx_line.split()[0])
        for ip in ips:
            dict_ip[ip] = dict_ip.get(ip, 0) + 1
        for k, v in dict_ip.iteritems():
            dict_ips.setdefault(v, []).append(k)
        return dict_ips

def px():
    keys = zdpx('access.log').keys()
    keys.sort()
    keys.reverse()
    return keys

def w_file(filename):
    num = 0
    with open(filename, 'a+') as nginx_files:

        for i in px():
            num += 1
            if num == 1:
                if len(zdpx('access.log')[i]) == 1:
                    nginx_files.write('''<!DOCTYPE html>
        <head>
        <meta charset="utf-8">
        </head>
        <html>
        <body>
        <table border='1'>
             <tr>
                 <th>访问量</th>
                 <th>IP</th>
             </tr>
             <tr>
                 <td>%d</td>
                 <td>%s</td>
             </tr>''' % (i, zdpx('access.log')[i][0])
                                      )
                    continue
                elif len(zdpx('access.log')[i]) > 1:
                    nginx_files.write('''<!DOCTYPE html>
        <head>
        <meta charset="utf-8">
        </head>
        <html>
        <body>
        <table border='1'>
            <tr>
                 <th>访问量</th>
                 <th>IP</th>
            </tr> '''
                                      )
                    for t in zdpx('access.log')[i]:
                        nginx_files.write('''
             <tr>
                 <td>%d</td>
                 <td>%s</td>
             </tr>''' % (i, t)
                                          )
            for t in zdpx('access.log')[i]:
                nginx_files.write('''
             <tr>
                 <td>%d</td>
                 <td>%s</td>
             </tr>''' % (i, t)
                                  )

            if num == 10:
                nginx_files.write('''</table>
         </body>
         </html>''')
                break
    return 'good'

print w_file('nginx_file')

