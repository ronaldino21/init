from flask import request, blueprints, redirect,session, render_template, jsonify
from models.User import User, db, UserSchema

users_routes = blueprints.Blueprint("users", __name__)

@users_routes.route('/getUsers', methods=['GET'])
def getUsers():
    users = User.query.all()
    schema = UserSchema(many=True)
    result = schema.dump(users)
    return jsonify(result)

@users_routes.route('/addUser', methods=['POST'])
def addUser():
    name = request.json['name']
    password = request.json['password']
    is_admin = request.json['is_admin']
    user = User(name, password, is_admin)
    db.session.add(user)
    db.session.commit()
    return jsonify('Usuario agregado exitosamente')

@users_routes.route('/deleteUser/<id>', methods=['DELETE'])
def deleteUser(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify('Usuario eliminado exitosamente')

@users_routes.route('/login', methods=['GET', 'POST'])
def login():
    
    error_message = None
    
    if 'username' in session:
        if 'is_admin' in session and session['is_admin']:
            return redirect('/admin')
        else:
            return redirect('/monitoring')
    request.method == 'POST'
    username = request.form['username']
    password = request.form['password']
    
    user = User.query.filter_by(name=username).first()
    
    if user is None or user.password != password:
        error_message = 'Usuario no encontrado o contraseña incorrecta'
    else:
        session['username'] = username
        session['is_admin'] = user.is_admin
        if user.is_admin:
            return redirect('/admin')
        else:
            return redirect('/monitoring')
        
    return render_template('login.html', error_message=error_message)
    
@users_routes.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username')
    if 'is_admin' in session:
        session.pop('is_admin')

    return redirect('/')