from app import db
from flask import Blueprint, jsonify, abort, make_response, request

author_bp = Blueprint("author_bp", __name__, url_prefix="/authors")

