from app import db
from flask import Blueprint, abort, make_response, request, jsonify

genre_bp = Blueprint("genre_bp", __name__, url_prefix = "/genres")

@genre_bp.route("", methods=["POST"])
def creat_genre():
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
