#!/usr/bin/env python
#coding:utf-8
from flask import Flask,request,render_template,redirect
#request 里面包含一次网络请求所有的内容，所有url参数(get的参数)，都在request.args里，args是一个类似字典的数据
#render_template 渲染前端html文件，默认渲染/templates下面的文件,有模板功能
#jinjia2模板语言{{}}包裹的是变量 循环语法{% for x in arr %} {%endfor%}
#新建app
app=Flask(__name__)

#监听路由。就是url  在域名和端口后面
#当域名和端口后面只有一个/的时候，这个路由触发
@app.route('/')

def index():
	name=request.args.get('name')
	pwd=request.args.get('password')
	if name =='admin' and pwd=='admin123':
		return redirect('/reboot')	
	else:
		return 'please login'
#        return "hello world"

@app.route('/adduser')
def adduser():
	name=request.args.get('name')
	pwd=request.args.get('password')
	with open('user.txt','a+') as f:
		f.write('%s:%s\n'%(name,pwd))
	return redirect('/reboot')


@app.route('/reboot')

def reboot():
	word=request.args.get('word','reboot')
#	names=[{'name':'xiaoming','age':12},{'name':'wd','age':10}]
#	return "search word is %s"%(word)
	f=open('user.txt')
	names=[line.split(':') for line in f.read().split('\n')]
	return render_template('test.html',word=word,age=12,names=names)
#	f=open('templates/test.html')
#	content= f.read()
#	f.close()
#	return content



#启动app
if __name__ =='__main__':
	app.run(host='0.0.0.0',port=8888,debug=True)

