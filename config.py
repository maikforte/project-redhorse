import os
from flask import Flask
from flasgger import Swagger
from dotenv import load_dotenv

from blueprints import calculator

load_dotenv('.env')

def create_app():
    app = Flask(__name__)
    app.debug = True

    app.register_blueprint(calculator, url_prefix='/calculator')

    Swagger(app)

    return app
