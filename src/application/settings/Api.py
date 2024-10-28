from flask import Flask
from flask_restx import Api

api = Api(prefix='/', doc='/docs')


class Api:
    def __init__(self, app: Flask):
        api.init_app(app=app)
        api.add_namespace(app.controllers.todo_controller.namespace)
