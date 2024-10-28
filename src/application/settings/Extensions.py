from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()


class Extensions:
    def __init__(self, app: Flask) -> None:
        db.init_app(app=app)
        Migrate(app=app, db=db)
