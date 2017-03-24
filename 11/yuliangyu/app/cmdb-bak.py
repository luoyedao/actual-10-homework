from flask import Flask,request,render_template,session,redirect
from . import app
import traceback
import json 
import db
import hashlib

#app.secret_key = 'sldkfjljl'
salt = "aaaaa"


@app.route('/idc')
def idc():
    if not session.get('name',None):
	return redirect('/login')
    fields = ['id','name','name_cn','address','adminer','phone']
    table = 'idc'
    result = db.selectAll(fields,table)
    data = [dict((k,row[i]) for i,k in enumerate(fields)) for row in result]
    return render_template('idc.html',idcs=data,info=session)

@app.route('/addidc',methods=['GET','POST'])
def addidc():
    if not session.get('name',None):
        return redirect('/login')
#    if session.get('role') != 'admin':
#        errmsg = "you are not admin, can not register idc"
#	return json.dumps({'code':1,'errmsg':'you are not admin, can not add idc'})
    if request.method == 'POST':
	print '---------reuqst.form-----'
	print request.form
	print '---------dict(reuqst.form)-----'
	print dict(request.form)
	print '---------dict(reuqst.form).items()-----'
	print dict(request.form).items()
        data = {}
        data = dict((k,v[0]) for k,v in dict(request.form).items())
        print data
        # data = request.get_json()
        fields = ['name','name_cn','address','adminer','phone']
	table = 'idc'
        if not data["name"]:
            errmsg = "name null"
            return render_template("idc.html", result=errmsg)
        try:
            db.insert(fields,data,table)
	    return json.dumps({'code':0,'result':'add idc success'})
        except:
            print traceback.print_exc()
	    return json.dumps({'code':1,'errmsg':'add idc error'})
    else:
        return render_template("addidc.html", info = session)

@app.route('/delidc',methods=['GET'])
def delidc():
#    if not session.get('username',None):
#        return redirect('/login')
    id = request.args.get('id')
    print id
    table = 'idc'
    try:
        db.delete(id,table)
	return json.dumps({'code':0, 'result':'delete idc success'})
    except:
        print traceback.print_exc()
	return json.dumps({'code':1, 'result':'delete idc failed'})
    

@app.route('/updateidc', methods=['GET','POST'])
def updateidc():
    table = 'idc'
    if not session.get('name',None):
        return redirect('/login')
    if request.method == "POST":
        data = dict(request.form)
	print data
	print data['id'][0]
        condition = [ "%s='%s'" % (k,v[0]) for k,v in data.items() ]
	print condition
        try:
            db.update(condition, data['id'][0], table)
	    return json.dumps({'code':0,'result':'update idc success'})
        except:
            print traceback.print_exc()
	    return json.dumps({'code':1,'result':'update idc failed'})
    else:
        id = request.args.get('id')
	print id
        fields = ['id','name','name_cn','address','adminer','phone']
        try:
            res = db.selectId(fields,id,table)
            idc = dict((k,res[i]) for i,k in enumerate(fields))
	    print idc
	    return json.dumps({'code':0, 'result':idc})
        except:
            print traceback.print_exc()
	    return json.dumps({'code':1, 'result':'select idcinfo failed'})

    
@app.route('/cabinet')
def cabinet():
    if not session.get('name',None):
	redirect('/login')
    fields = ['id','name','idc_id','u_num','power']
    table = 'cabinet'
    try:
        result = db.selectAll(fields,table)
	print result
        data = [dict((k,row[i]) for i,k in enumerate(fields)) for row in result]
	print data
        return  render_template('cabinet.html', cabinets = data, info = session)
    except:	
        print traceback.print_exc()
        return json.dumps({'code':1,'result':'select cabinet failed'})


@app.route('/addcabinet',methods=['GET','POST'])
def addcabinet():
    if session.get('name',None):
	redirect('/login')
    if request.method == 'POST':
	data = dict((k,v[0]) for k,v in dict(request.form).items())
	fields = ['name','idc_id','u_num','power']
	table = 'cabinet'
	try:
	    db.insert(fields,data,table)
	    return json.dumps({'code':0, 'result': 'add cabinet success'})
	except:
            print traceback.print_exc()
	    return json.dumps({'code':1,'errmsg':'add cabinet error'})
	    
    else:
	table = 'idc'
	fields = ['id','name']
	result = db.selectAll(fields,table)
	print result
	data = [ dict((k,row[i]) for i,k in enumerate(fields)) for row in result ]
	print data
	return render_template('addcabinet.html',info = session, idcs = data)

@app.route('/updatecab',methods=['GET','POST'])
def updatacab():
    if session.get('name',None):
	redirect('/login')


@app.route('/server')
def server():
    return render_template('server.html')
