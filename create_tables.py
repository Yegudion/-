from app import app, db
from models import User, Book

with app.app_context():
    db.drop_all()
    db.create_all()
    print("Tables created successfully")
