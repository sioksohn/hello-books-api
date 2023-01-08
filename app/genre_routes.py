from app import db
from book_routes import validate_model
from flask import Blueprint, abort, make_response, request, jsonify

genre_bp = Blueprint("genre_bp", __name__, url_prefix = "/genres")

@genre_bp.route("", methods=["POST"])
def create_genre():
    request_body = request.get_json()
    new_genre = Genre.from_dict(request_body)

    db.session.add(new_genre)
    db.session.commit()

    return make_response(jsonify(f"Genre {new_genre.name} successfully created"), 201)

@genre_bp.route("", methods=["GET"])
def read_all_genres():
    genres = Genre.query.all()

    genres_response = []
    for genre in genres:
        genres_response.append(genre.to_dict())
    
    return jsonify(genres_response)

@genre_bp.route("/<genre_id>/books", methods=["POST"])
def create_boot_to_genre(genre_id):
    genre = validate_model(Genre, genre_id)

    request_body = request.get_json()
    new_book = Book.from_dict(request_body)

    db.session.add(new_book)
    db.session.commit()

    return make_response(jsonify(f"Book {new_book.title} by {new_book.author.name} successfully created"), 201)

@genre_bp.route("/<genre_id>/books", methods=["GET"])
def read_all_books_by_genre(genre_id):
    genre = validate_model(Genre, genre_id)

    books_response = []
    for book in genre.books:
        books_response.append(book.to_dict())

    return books_response