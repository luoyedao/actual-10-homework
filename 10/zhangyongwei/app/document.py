from flask import render_template
from . import app

@app.route('/server_deploy/')
def server_deploy():
    return render_template('server_deploy.html')


@app.route('/server_pass/')
def server_pass():
    return render_template('server_pass.html')

