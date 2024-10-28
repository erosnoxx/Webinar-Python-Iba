from sqlalchemy.orm import Session
from src.application.contracts.data.repositories.ITodoRepository import ITodoRepository
from src.domain.entities.TodoEntity import TodoEntity


class TodoRepository(ITodoRepository):
    def __init__(self, session: Session):
        super().__init__(session, TodoEntity)
