from src.controllers.Resources.CreateTodoResource import CreateTodoResource
from src.controllers.Resources.GetTodoResource import GetTodoResource
from . import namespace


class TodoController:
    def __init__(self):
        self.namespace = namespace
        self.register_routes()

    def register_routes(self) -> None:
        self.namespace.add_resource(CreateTodoResource, '/create')
        self.namespace.add_resource(GetTodoResource, '/get')
