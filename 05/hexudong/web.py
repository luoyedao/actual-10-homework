from flask import Flask,request,render_template,redirect
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("test.html")
@app.route('/check')
def check():
    username = request.args.get('name')
    password = request.args.get('password')
    res_dict = {}
    with open('user.txt') as f:
     for i in f:
        user = i.rstrip("\n").split(":")[0]
        res_dict[user] = i.rstrip("\n").split(":")[1]
    if username in res_dict and password ==res_dict[username]:
        return render_template("table.html")
    else:
        return render_template("null.html")
@app.route('/adduser')
def adduser():
    name = request.args.get('name')
    pwd = request.args.get('password')
    if name and pwd:
        with open('user.txt','a+') as f:
            f.write('%s:%s\n' %(name,pwd))
        return redirect('/reboot')
    else:
        return 'need name and password'
@app.route('/null')
def null():
    return render_template("null.html")    
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404
@app.route('/deluser')
def deluser():
    name = request.args.get('name')
    tmp = []
    with open('user.txt') as f :
        for user in f:
            tmp.append(user)
    #print user
    tmp1 = []
    for item in tmp:
        if item.split(':')[0] !=str(name):
            tmp1.append(item)
#print tmp1
    with open('user.txt','w') as f:
        for i in tmp1:
            f.writelines(i)
    return redirect('/reboot')
@app.route('/reboot')
def reboot():
    word = request.args.get('word','reboot')
    #return 'seach word is %s' %(word)

    #return render_template('index.html')

    #return render_template('test.html',word=word,age=12)    
    
    #names = [{'name':'xiFFFg','age':16},{'name':'xiaoming','age':22},{'name':'dong','age':33}]
    f = open('user.txt')
    names = [line.split(':') for line in f.read().split('\n')]

    return render_template('table.html',names=names)
    f.close()
#True
'''
    f = open('templates/index.html')
    return f.read()
    f.closed()
'''
if __name__=='__main__':
    app.run(host='0.0.0.0',port=9000,debug=True)
