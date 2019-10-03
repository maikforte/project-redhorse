from flask import Flask
from flasgger import Swagger
from dotenv import load_dotenv

from blueprints import calculator

load_dotenv(".env")


def create_app():
    app = Flask(__name__)
    app.debug = True

    app.register_blueprint(calculator, url_prefix="/calculator")

    Swagger(app, template=get_swagger_template())
    print("test")
    return app


def get_swagger_template():
    return {
        "info": {
            "title": "Project RedHorse",
            "description": "Quick demonstration of Flask for Knowledge Tree",
            "contact": {
                "responsibleDeveloper": "Michael 'Maik' Ardan",
                "email": "michael.ardan2000@gmail.com",
            },
            "version": "1.0.0",
        },
        "schemes": ["http"],
    }
