from flask import Flask
from lefty_books.leftist_books import leftist_books_bp
app = Flask(__name__)

app.register_blueprint(leftist_books_bp, url_prefix='/leftist_book_list')