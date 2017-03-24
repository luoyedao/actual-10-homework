#coding:utf-8
from flask import request,render_template, redirect,session
from app import app
import json

@app.route('/log')
def log():
   if not session.get('username',None):
        return redirect("/login")
   return  render_template('log.html',info=session)

@app.route('/map')
def map():
   if not session.get('username',None):
        return redirect("/login")
   # 地图数据暂时没搞，课上实现，有兴趣的可以玩玩
   return  render_template('map.html',info=session)

@app.route('/status')
def status():
   if not session.get('username',None):
        return redirect("/login")

   # 模拟的假数据，真实数据拼接成这个格式即可
   result = {
       'legend':['200','404','502'],
       'data':[{'name':'200','value':234},{'name':'404','value':300},{'name':'502','value':250}]
   }
   return  json.dumps(result)
