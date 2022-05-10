from flask import Flask
from routes.contacts import contacts  # conexión con routes/contacts
from flask_sqlalchemy import SQLAlchemy #para poder instanciar

app = Flask(__name__)  # para inicializar el servidor

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:EDWINjosue35@localhost/dataurb' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.register_blueprint(contacts)  # para importarlo o añadirlo a la aplicación
