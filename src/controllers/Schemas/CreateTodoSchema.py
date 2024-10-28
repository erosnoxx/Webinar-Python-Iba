from flask_restx import Model, fields
from src.application.settings.Api import api


class TodoSchemas:
    @staticmethod
    def create_todo_input_schema() -> Model:
        return api.model('Create Todo', {
            'title': fields.String(description='O nome da tarefa', required=True),
            'description': fields.String(description='A descrição da tarefa'),
            'status': fields.String(description='O status da tarefa', required=True, example="pending"),
            'due_date': fields.String(description='A data de vencimento da tarefa no formato YYYY-MM-DD'),
            'owner_name': fields.String(description='Nome do responsável pela tarefa', required=True)
        })

    @staticmethod
    def create_todo_output_schema() -> Model:
        return api.model('Create Todo Output', {
            'success': fields.Boolean(description='Indica se a operação foi bem-sucedida', default=True),
            'statuscode': fields.Integer(description='Código de status HTTP da resposta', default=200),
            'message': fields.String(
                description='Mensagem detalhada sobre o status da operação')
        })
