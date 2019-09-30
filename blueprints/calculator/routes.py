from blueprints.calculator import calculator, controller
from flask import request
from flasgger import swag_from

@calculator.route('/multiply')
@swag_from('test.yml')
def multiply():
    number = request.args.get('number')
    response = controller.multiply(number)
    return str(response)
