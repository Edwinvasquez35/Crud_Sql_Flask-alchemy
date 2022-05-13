from utils.db import db

# para crear la tabla se hará una vez inicie la app, por eso la función para crearla estará en index
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True)
    phone = db.Column(db.String(20), nullable=False) 
    cedula = db.Column(db.Integer, unique=True, nullable=False)
    parking_number = db.relationship('Parking', backref='parking_number', lazy=True)

    def __init__(self, fullname:str , email:str, phone:str, cedula:int): # método constructor de la tabla
      
        self.fullname = fullname
        self.email = email
        self.phone = phone
        self.cedula = cedula

class Parking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    parking_number = db.Column(db.Integer)
    contact_id = db.Column(db.Integer, db.Foreignkey('contact.id'))
    contact = db.relationship('Contact')
    vehicle_type = db.Column(db.String(10))

    def __init__(self, parking_number:int, contact_id:int, vehicle_type:str ): # método constructor de la tabla
      
        self.parking_number = parking_number
        self.contact_id = contact_id
        self.vehicle_type = vehicle_type


