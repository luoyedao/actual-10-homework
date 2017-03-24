from flask import render_template
from . import app

@app.route('/online_players/')
def online_players():
    return render_template('online_players.html')

@app.route('/server_status/')
def server_status():
    return render_template('server_status.html')