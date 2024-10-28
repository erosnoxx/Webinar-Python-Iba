from typing import List
from src.domain.entities.TodoEntity import TodoEntity


class GetTodoOutputDto:
    def __init__(self, todo_entities: List[TodoEntity]) -> None:
        self.todo_entities = todo_entities
