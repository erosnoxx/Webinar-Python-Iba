from datetime import datetime
from src.domain.entities.common.BaseEntity import BaseEntity, db


class TodoEntity(BaseEntity):
    __tablename__ = 'todo'

    title = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(100))
    status = db.Column(db.String(15), nullable=False)
    due_date = db.Column(db.DateTime)
    owner_name = db.Column(db.String(50), nullable=False)

    def __init__(self, 
                title: str,
                status: str, 
                owner_name: str,
                description: str=None,
                due_date: datetime=None) -> None:
        self.title = title
        self.description = description
        self.status = status
        self.due_date = due_date
        self.owner_name = owner_name
