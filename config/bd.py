from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_socketio import SocketIO
from flask_cors import CORS
from geventwebsocket.gunicorn.workers import GeventWebSocketWorker

app = Flask(__name__)

TK = 'writtenby'

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://bebedb_s2zt_user:OQKy9W2LHW5hrjZ47OW2Kz8d9jerIRFb@dpg-ctu51erv2p9s738ovetg-a/bebedb_s2zt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = 'ltPanel'

CORS(app)
db = SQLAlchemy(app)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='gevent')
ma = Marshmallow(app)

@app.after_request
def apply_cors(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST,PUT,OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'content-type'
    return response

#eche
