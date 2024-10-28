from src.domain.entities.TodoEntity import TodoEntity


class CreateTodoOutputDto:
    def __init__(self, todo_entity: TodoEntity) -> None:
        self.todo_entity = todo_entity
