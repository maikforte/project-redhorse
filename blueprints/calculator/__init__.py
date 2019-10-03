from flask import Blueprint

calculator = Blueprint("calculator", __name__)

from blueprints.calculator import routes
