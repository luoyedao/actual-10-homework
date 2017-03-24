#!/user/bin/env python
#coding=utf-8

from flask import Flask

app=Flask(__name__)
app.secret_key='!s\xa3-\xafle6\xe2=\xfa3'

from usermgr import *

if __name__ == '__main__':
  app.run(host='0.0.0.0',port=2000,debug=True)
