from crypt import methods
from flask import Blueprint, render_template, request, redirect, url_for  #Request para leer los datos que vienen desde el from en la consola
from models.contact import Contact   # instanciarlos
from utils.db import db #para operar con la base utilizo la conexión que esta en db

contacts = Blueprint("contacts", __name__) # para evitar las referencias circulares y hacer la conexión con el app y app con este archivo


@contacts.route("/")
def home():
    consult = Contact.query.all()
    return render_template('index.html', consult=consult) #para la conexión con el archivo html

@contacts.route("/new", methods=['POST'])
def add_contact():
    fullname=request.form['fullname']
    email=request.form['email']
    phone=request.form['phone']
    cedula=request.form['cedula'] #recibo los datos
    parking_number = request.form['parking_number']
    vehicle_type = request.form['vehicle_type']
    apartment = request.form['apartment']


    new_contact = Contact(fullname, email, phone, cedula, parking_number, vehicle_type, apartment) #me permite definir un nuevo objeto que guardar y me devlverá un nuevo objeto
    
    db.session.add(new_contact) #para guardar los datos o instanciarlos en la base
    db.session.commit() #finaliza la conexión y guarda

    return redirect(url_for('contacts.home'))

@contacts.route("/update/<id>", methods = ['POST', 'GET'])
def update(id):
    consult = Contact.query.get(id) 

    if request.method == "POST":
        # para actualizar los datos que me esta pasando el método post
        consult.fullname=request.form['fullname']
        consult.email=request.form['email']
        consult.phone=request.form['phone']
        consult.cedula=request.form['cedula'] 
        consult.parking_number = request.form['parking_number']
        consult.vehicle_type = request.form['vehicle_type']
        consult.apartment = request.form['apartment']

        db.session.commit()
        
        return redirect(url_for('contacts.home'))

    return render_template('update.html', consult=consult) #si el requerimiento viene por el método get mestra el listado

@contacts.route("/delete/<id>")
def delete(id):
    consult = Contact.query.get(id)
    db.session.delete(consult)
    db.session.commit()
    return redirect(url_for('contacts.home'))