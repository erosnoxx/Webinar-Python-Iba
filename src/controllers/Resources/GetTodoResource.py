from src.application.usecases.GetTodoUseCase import GetTodoUseCase
from src.controllers.Schemas.GetTodoSchema import GetTodoSchemas
from .. import namespace

from flask import Response, make_response, request, current_app
from flask_restx import Resource


class GetTodoResource(Resource):
    @namespace.doc('Retorna todas as tarefas')
    @namespace.response(200, 'Ok', GetTodoSchemas.get_todo_output_schema())
    @namespace.marshal_with(GetTodoSchemas.get_todo_output_schema(), as_list=True)
    def get(self) -> Response:
        usecase: GetTodoUseCase = current_app.usecases.get_todo_usecase

        output = usecase.execute()

        return output.todo_entities
