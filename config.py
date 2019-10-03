import os

from dotenv import load_dotenv

from flask import Flask
from blueprints import calculator
from flasgger import Swagger

load_dotenv('.env')

def create_app():
    app = Flask(__name__)
    app.debug = True

    app.register_blueprint(calculator, url_prefix='/calculator')

    Swagger(app)

    return app
