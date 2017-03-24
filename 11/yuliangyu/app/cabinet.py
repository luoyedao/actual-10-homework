from flask import Flask,request,render_template,session,redirect
from . import app
import traceback
import json 
import db
import hashlib
import pdb

#app.secret_key = 'sldkfjljl'
salt = "aaaaa"


    
@app.route('/cabinet')
def cabinet():
    if not session.get('name',None):
	redirect('/login')
    fields = ['id','name','idc_id','u_num','power']
    idc_fields = ['id','name']
    table = 'cabinet'
    try:
        result = db.selectAll(fields,table)
#	print result
        data = [dict((k,row[i]) for i,k in enumerate(fields)) for row in result]
	print data
	idcs = db.selectAll(idc_fields,'idc')
#	pdb.set_trace()
	idcs = dict(idcs)
	print idcs
	#((7L, u'hp'), (1L, u'syq'), (8L, u'zhaowei'))
	for cabinet in data:
	    if cabinet['idc_id'] in idcs:
		cabinet['idc_id'] = idcs[cabinet['idc_id']]
	print data
        return  render_template('cabinet/cabinet.html', cabinets = data, info = session)
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
	return render_template('cabinet/addcabinet.html',info = session, idcs = data)

@app.route('/updatecab',methods=['GET','POST'])
def updatacab():
    if session.get('name',None):
	redirect('/login')
    if request.method == 'POST':
	data = dict(request.form)
	fields = ['name','idc_id','u_num','power']
	table = 'cabinet'
	condition = [ "%s='%s'" % (k,v[0]) for k,v in data.items() ]
	try:
	    db.update(condition, data['id'][0], table)
	    return json.dumps({'code':0, 'result': 'add cabinet success'})
	except:
	    print traceback.print_exc()
	    return json.dumps({'code':1,'errmsg':'update cabinet error'})
	
    else:
	id = request.args.get('id')
	print id
	fields = ['id','name','idc_id','u_num','power']
	table = 'cabinet'
	try:
	    result = db.selectId(fields,id,table) 
	    cabinet = dict((k,result[i]) for i,k in enumerate(fields))
	    table_idc = 'idc'
	    fields_idc = ['id','name']
	    result = db.selectAll(fields_idc,table_idc)
	    print result
	    idcs = [ dict((k,row[i]) for i,k in enumerate(fields_idc)) for row in result ]
	    return render_template('cabinet/updatecabinet.html',info = session, cabinet = cabinet, idcs = idcs)
	except:
	    print traceback.print_exc()
	    return json.dumps({'code':1, 'result':'select cabinetinfo failed'})


@app.route('/delcabinet',methods=['GET'])
def delcabinet():
    id = request.args.get('id')
    table = 'cabinet'
    try:
	db.delete(id,table)
	return json.dumps({'code':0, 'result': 'delete cabinet success'})
    except:
	print traceback.print_exc()
	return json.dumps({'code':1, 'result': 'delete cabinet failed'})

