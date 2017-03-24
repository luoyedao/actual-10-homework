#!/usr/bin/env python
#@The author: toby (15915822634@139.com)
#@Date: 2016-08-08 

from flask import Flask
app = Flask('__name__')

from route import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)
