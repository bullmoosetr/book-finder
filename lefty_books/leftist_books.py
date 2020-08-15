from flask import jsonify, Blueprint
from general.request import BaseRequest

leftist_books_bp = Blueprint('leftist_books_bp', __name__)

@leftist_books_bp.route('/')
def get_lefty_books():
    books = BaseRequest().search_by_works('communism').text
    return books




        