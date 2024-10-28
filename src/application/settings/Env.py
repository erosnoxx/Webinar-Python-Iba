import os
from dotenv import load_dotenv
from flask import Flask

load_dotenv()


class Env:
    def __init__(self, app: Flask):
        app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
        app.config['FLASK_DEBUG'] = os.getenv('FLASK_DEBUG')
        app.config['FLASK_ENV'] = os.getenv('FLASK_ENV')
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')

        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
