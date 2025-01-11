from config.bd import db, ma, app

class User(db.Model):
    
    __tablename__ = "User"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70), unique=True)
    password = db.Column(db.String(100))
    is_admin = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def __init__(self, name, password, is_admin):
        self.name = name
        self.password = password
        self.is_admin = is_admin

with app.app_context():
    db.create_all()
    
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'password', 'is_admin', 'created_at')