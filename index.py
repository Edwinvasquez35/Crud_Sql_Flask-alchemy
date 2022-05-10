from app import app
from utils.db import db
from models.contact import Contact

with app.app_context():#crear las tablas una vez inicie la app
    db.create_all()

if __name__ == "__main__":  # condicional básica de incio
    app.run(debug=True)