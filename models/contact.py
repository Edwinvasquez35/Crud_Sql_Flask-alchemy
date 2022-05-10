from utils.db import db

# para crear la tabla se hará una vez inicie la app, por eso la función para crearla estará en index
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100))
    phone = db.Column(db.String(20), nullable=False) 
    cedula = db.Column(db.Integer, unique=True, nullable=False)

    def __init__(self, fullname, email, phone, cedula): # método constructor de la tabla
        self.fullname = fullname
        self.email = email
        self.phone = phone
        self.cedula = cedula