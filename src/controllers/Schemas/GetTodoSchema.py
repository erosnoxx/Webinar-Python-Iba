from flask_restx import Model, fields
from src.application.settings.Api import api


class GetTodoSchemas:

    @staticmethod
    def get_todo_output_schema() -> Model:
        return api.model('Get todo', {
            'title': fields.String,
            'status': fields.String,
            'description': fields.String,
            'due_date': fields.DateTime,
            'owner_name': fields.String,
        })
