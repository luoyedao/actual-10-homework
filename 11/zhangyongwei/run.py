from app import app
import sys


reload(sys)
sys.setdefaultencoding('utf8')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9898, debug=True)