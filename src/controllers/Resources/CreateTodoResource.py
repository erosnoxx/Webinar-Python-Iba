from src.application.usecases.CreateTodoUseCase import CreateTodoUseCase
from src.application.usecases.dto.input.CreateTodoInputDto import CreateTodoInputDto
from src.controllers.Schemas.CreateTodoSchema import TodoSchemas
from .. import namespace
from flask import Response, make_response, request, current_app
from flask_restx import Resource


class CreateTodoResource(Resource):
    @namespace.doc('Cria uma tarefa')
    @namespace.expect(TodoSchemas.create_todo_input_schema())
    @namespace.response(201, 'Created', TodoSchemas.create_todo_output_schema())
    def post(self) -> Response:
        data = request.json
        input_dto = CreateTodoInputDto(
            title=data.get('title'),
            description=data.get('description'),
            status=data.get('status'),
            due_date=data.get('due_date'),
            owner_name=data.get('owner_name'))
        
        usecase: CreateTodoUseCase = current_app.usecases.create_todo_usecase
        output = usecase.execute(input_dto=input_dto)

        response_data = {
            'success': True,
            'message': 'Tarefa Criada',
            'statuscode': 201
        }
        response = make_response(response_data, 201)
        response.headers['Content-Type'] = 'application/json'

        return response
