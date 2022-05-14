from utils.db import db

# para crear la tabla se hará una vez inicie la app, por eso la función para crearla estará en index
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100))
    phone = db.Column(db.String(20), nullable=False) 
    cedula = db.Column(db.Integer, unique=True, nullable=False)
    parking_number = db.Column(db.Integer)
    vehicle_type = db.Column(db.String(20))
    apartment = db.Column(db.Integer)

    def __init__(self, fullname:str , email:str, phone:str, cedula:int, parking_number:int, vehicle_type:str, apartment:int): # método constructor de la tabla
        self.fullname = fullname
        self.email = email
        self.phone = phone
        self.cedula = cedula
        self.parking_number = parking_number
        self.vehicle_type = vehicle_type
        self.apartment = apartment