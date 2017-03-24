#encoding: utf-8
from flask import Flask
import loganalysis

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello, reboot'

@app.route('/logs/')
def logs():
    logfile = '/root/share/03/zuoye/access.log'
    return loganalysis.loganalysis(logfile=logfile)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999, debug=True)
