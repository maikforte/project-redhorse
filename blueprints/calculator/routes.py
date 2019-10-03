from flask import request, jsonify
from flasgger import swag_from

from blueprints.calculator import calculator, controller


@calculator.route('/multiply')
@swag_from('open-api/multiply.yml')
def multiply():
    multiplicand = int(request.args.get('multiplicand'))
    multiplier = int(request.args.get('multiplier'))

    product = controller.multiply(multiplicand, multiplier)

    return jsonify({ "product": product })
