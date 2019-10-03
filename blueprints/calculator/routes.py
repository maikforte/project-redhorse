from flask import request
from flasgger import swag_from

from blueprints.calculator import calculator, controller


@calculator.route('/multiply')
@swag_from('open-api/multiply.yml')
def multiply():
    number = request.args.get('number')
    response = controller.multiply(number)
    return str(response)
