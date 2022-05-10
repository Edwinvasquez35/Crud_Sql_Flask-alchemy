from flask import Blueprint, render_template, request  #Request para leer los datos que vienen desde el from en la consola
from models.contact import Contact   # instanciarlos
from utils.db import db #para operar con la base utilizo la conexión que esta en db

contacts = Blueprint("contacts", __name__) # para evitar las referencias circulares y hacer la conexión con el app y app con este archivo


@contacts.route("/")
def home():
    return render_template('index.html') #para la conexión con el archivo html

@contacts.route("/new", methods=['POST'])
def add_contact():
    fullname=request.form['fullname']
    email=request.form['email']
    phone=request.form['phone']
    cedula=request.form['cedula'] #recibo los datos
    
    new_contact = Contact(fullname, email, phone, cedula) #me permite definir un nuevo objeto que guardar y me devlverá un nuevo objeto
    
    db.session.add(new_contact) #para guardar los datos o instanciarlos en la base
    db.session.commit() #finaliza la conexión y guarda

    return "saving a contact"

@contacts.route("/update")
def update():
    return "update contact"  

@contacts.route("/delete")
def delete():
    return "delete a contact"