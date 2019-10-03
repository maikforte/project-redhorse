import json
from flask import request, jsonify
from flasgger import swag_from

from blueprints.calculator import calculator, controller


@calculator.route("/add", methods=["GET"])
@swag_from("open-api/add.yml")
def add():
    augend = int(request.args.get("augend"))
    addend = int(request.args.get("addend"))

    sum = controller.add(augend, addend)

    return jsonify({"sum": sum}), 200


@calculator.route("/subtract", methods=["POST"])
@swag_from("open-api/subtract.yml")
def subtract():
    data = json.loads(request.data)

    minuend = data["minuend"]
    subtrahend = data["subtrahend"]

    difference = controller.subtract(minuend, subtrahend)

    return jsonify({"difference": difference}), 200


@calculator.route("/multiply", methods=["PUT"])
@swag_from("open-api/multiply.yml")
def multiply():
    data = json.loads(request.data)

    multiplicand = data["multiplicand"]
    multiplier = data["multiplier"]

    product = controller.multiply(multiplicand, multiplier)

    return jsonify({"product": product}), 200
