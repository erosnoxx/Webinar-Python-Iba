from src.application.settings.Extensions import db
from src.data.repositories.TodoRepository import TodoRepository


class GlobalRepositories:
    def __init__(self):
        _session = db.session
        self.todo_repository = TodoRepository(session=_session)
