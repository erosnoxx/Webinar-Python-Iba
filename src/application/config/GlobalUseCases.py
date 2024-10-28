from src.application.config.GlobalRepositories import GlobalRepositories
from src.application.usecases.CreateTodoUseCase import CreateTodoUseCase
from src.application.usecases.GetTodoUseCase import GetTodoUseCase


class GlobalUseCases:
    def __init__(self, repositories: GlobalRepositories):
        self.create_todo_usecase = CreateTodoUseCase(
            todo_repository=repositories.todo_repository)
        self.get_todo_usecase = GetTodoUseCase(
            todo_repository=repositories.todo_repository)
