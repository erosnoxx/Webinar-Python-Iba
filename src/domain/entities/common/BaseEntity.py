import os
from datetime import datetime
from src.application.settings.Extensions import db

Base = db.Model

class BaseEntity(Base):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime)
