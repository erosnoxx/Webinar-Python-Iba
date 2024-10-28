from src.application.usecases.dto.output.GetTodoOutputDto import GetTodoOutputDto
from src.data.repositories.TodoRepository import TodoRepository


class GetTodoUseCase:
    def __init__(self, todo_repository: TodoRepository):
        self.repository = todo_repository

    def execute(self) -> GetTodoOutputDto:
        todo_entities = self.repository.list()
        return GetTodoOutputDto(todo_entities=todo_entities)
