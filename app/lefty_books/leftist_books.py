from flask import jsonify, Blueprint
from app.lefty_books.base_requests import BaseRequest

leftist_books_bp = Blueprint('leftist_books_bp', __name__)

@leftist_books_bp.route('/')
def get_books_on_marxism():
    books = BaseRequest(search='communism', subject='communism', author='marx').search_by_volumes()
    return books




        