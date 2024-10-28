from flask import Flask
from src.application.settings.Api import Api
from src.application.settings.Env import Env
from src.application.settings.Extensions import Extensions
from src.application.settings.Globals import Globals


class GlobalSettings:
    def __init__(self, app: Flask):
        self.env = Env(app=app)
        self.extensions = Extensions(app=app)
        self.globals = Globals(app=app)
        self.api = Api(app=app)
