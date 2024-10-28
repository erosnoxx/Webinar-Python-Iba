from datetime import datetime
from src.application.usecases.dto.input.CreateTodoInputDto import CreateTodoInputDto
from src.application.usecases.dto.output.CreateTodoOutputDto import CreateTodoOutputDto
from src.data.repositories.TodoRepository import TodoRepository
from src.domain.entities.TodoEntity import TodoEntity


class CreateTodoUseCase:
    def __init__(self, todo_repository: TodoRepository):
        self.repository = todo_repository
    
    def execute(self, input_dto: CreateTodoInputDto) -> CreateTodoOutputDto:
        if isinstance(input_dto.due_date, str):
            input_dto.due_date = datetime.strptime(input_dto.due_date, '%Y-%m-%d')
            
        entity = TodoEntity(**input_dto.to_dict())
        todo_entity = self.repository.add(obj=entity)
        return CreateTodoOutputDto(todo_entity=todo_entity)
