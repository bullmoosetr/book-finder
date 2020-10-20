from flask import Flask
import os
from app import views


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config')

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    from app.lefty_books.leftist_books import leftist_books_bp

    app.register_blueprint(leftist_books_bp, url_prefix='/leftist_book_list')
    
    return app