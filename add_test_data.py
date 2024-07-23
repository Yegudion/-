from app import app, db
from models import User, Book

with app.app_context():
    user1 = User(name="Alice", email="alice@example.com")
    user2 = User(name="Bob", email="bob@example.com")

    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()

    book1 = Book(title="1984", author="George Orwell", owner_id=user1.id)
    book2 = Book(title="To Kill a Mockingbird", author="Harper Lee", owner_id=user2.id)

    db.session.add(book1)
    db.session.add(book2)
    db.session.commit()

    print("Test data added successfully")
