from flask import (jsonify, Blueprint,
redirect, render_template, request, url_for)
from app.lefty_books.base_requests import BaseRequest

leftist_books = Blueprint('leftist_books', __name__)

@leftist_books.route('/')
def index():
    book_list = {}
    marxist_books = BaseRequest(search='marx', subject='philosophy', author='marx').search_by_volumes()
    communism = BaseRequest(search='communism', subject='communism').search_by_volumes_no_author()
    
    # What to display on index
    # Need Book Title
    # Author
    # Description
    # TODO Links on what independent book store sells them
    # TODO Search by Zip code what stores sell the books - Will likely require either a web spider or api access either way need research
    
    # The list contains a list of dictionaries with Title, description, Author
    book_list['marxism'] = [i.get('volumeInfo') for i in marxist_books.get('items')]
    book_list['communism'] = [i.get('volumeInfo') for i in communism.get('items')]
    return render_template('lefty_books/index.html', books=book_list)

