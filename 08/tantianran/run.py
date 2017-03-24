#!/usr/bin/env python
# Program:
#	This program is the run the program
# Author:   Tantianran    15915822634@139.com
# last modification time:  /2016/08/25    
# Version:  v0.1

from flask import Flask
app = Flask('__name__')

from view import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)

