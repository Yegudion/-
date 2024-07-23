from flask import request, jsonify, render_template
from app import app, db
from models import User, Book

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['GET'])
def users():
    users = User.query.all()
    return render_template('users.html', users=users)

@app.route('/books', methods=['GET'])
def books():
    books = Book.query.all()
    return render_template('books.html', books=books)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(name=data['name'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    new_book = Book(title=data['title'], author=data['author'], owner_id=data['owner_id'])
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message': 'Book added successfully'}), 201

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify({
        'id': user.id,
        'name': user.name,
        'email': user.email,
        'books': [{'id': book.id, 'title': book.title, 'author': book.author} for book in user.books]
    })

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.query.get_or_404(book_id)
    return jsonify({
        'id': book.id,
        'title': book.title,
        'author': book.author,
        'owner': {'id': book.owner.id, 'name': book.owner.name, 'email': book.owner.email}
    })
