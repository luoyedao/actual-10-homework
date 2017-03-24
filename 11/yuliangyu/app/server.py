from flask import Flask,request,render_template,session,redirect
from . import app
import traceback
import json 
import db
import hashlib
import pdb

#app.secret_key = 'sldkfjljl'
salt = "aaaaa"


@app.route('/server')
def server():
    if not session.get('name',None):
	redirect('/login')
    fields = ['id','hostname','lan_ip','wan_ip','cabinet_id','op','phone']
    table = 'server'
    result = db.selectAll(fields,table)
    print result
    data = [ dict((k,row[i]) for i,k in enumerate(fields)) for row in result ]
    cabinet_fields = ['id','name']
    cabinets = db.selectAll(cabinet_fields,'cabinet')
    cabinets = dict(cabinets)
    print cabinets
    for server in data:
	print server
	print server['cabinet_id']
	if server['cabinet_id'] in cabinets:
	    print 'True'
	    server['cabinet_id'] = cabinets[server['cabinet_id']]
    print data
    return render_template('server/server.html', info = session, servers = data)


@app.route('/addserver',methods=['GET','POST'])
def addserver():
    if not session.get('name',None):
	redirect('/login')
    if request.method == 'POST':
	table = 'server'
	data =  dict((k,v[0]) for k,v in dict(request.form).items())
        fields = ['hostname','lan_ip','wan_ip','cabinet_id','op','phone']
	try:
	    db.insert(fields,data,table)
	    return json.dumps({'code':0, 'result':'add server success'})
	except:
            print traceback.print_exc()
            return json.dumps({'code':1,'errmsg':'add server error'})
    else:
	table = 'cabinet'
	fields = ['id','name']
	result = db.selectAll(fields,table)
	data = [ dict((k,row[i]) for i,k in enumerate(fields)) for row in result ]
	print data
        return render_template('server/addserver.html', info = session, cabinets = data)

@app.route('/updateser',methods=['GET','POST'])
def updateser():
    if request.method == 'POST':
	
	return True
    else:
	table = 'cabinet'
	fields = ['id','name']
	result = db.selectAll(fields,table)
	print result 
#	((6L, u'002'), (5L, u'005'), (8L, u'008'), (13L, u'100'), (14L, u'111'))
	print dict(result)
#	{8L: u'008', 14L: u'111', 5L: u'005', 6L: u'002', 13L: u'100'}
	data = [ dict((k,row[i]) for i,k in enumerate(fields)) for row in result ]
	print data
#       [{'id': 6L, 'name': u'002'}, {'id': 5L, 'name': u'005'}, {'id': 8L, 'name': u'008'}, {'id': 13L, 'name': u'100'}, {'id': 14L, 'name': u'111'}]
#	server = 
        return render_template('server/updateserver.html', info = session, cabinets = data) 
