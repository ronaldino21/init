from flask import Flask, request, jsonify, render_template, redirect, session
from models import *
from config.bd import db, app, socketio
from flask_socketio import SocketIO
from functools import wraps

from apis.user_route import users_routes
from apis.datatable_route import dataTables_routes
from apis.events_route import events_routes
from apis.trico_route import trico_routes

app.register_blueprint(users_routes, url_prefix='/users')
app.register_blueprint(dataTables_routes, url_prefix='/dataTables')
app.register_blueprint(events_routes, url_prefix='/events')
app.register_blueprint(trico_routes, url_prefix='/trico')


TK = 'initr'

def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.args.get('token')
        if not token or token != TK:
            return redirect("https://www.google.com")
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
@token_required
def index():
    return render_template('login.html')

@app.route('/monitoring')
def monitoring():
    if 'username' not in session:
        return redirect('/')
    else:
        if 'is_admin' in session and session['is_admin']:
            return redirect('/admin')
        else:
            return render_template('page.html')

@app.route('/admin')
def admin():
    if 'username' not in session:
        return redirect('/')
    else:
        if 'is_admin' in session and session['is_admin']:
            return render_template('admin.html')
        else:
            return redirect('/monitoring')
        

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    socketio.run(app, port=port, allow_unsafe_werkzeug=True)
