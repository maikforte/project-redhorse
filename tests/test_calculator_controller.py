from blueprints.calculator import controller


def test_multiply():
    multiplicand = 2
    multiplier = 3
    product = multiplicand * multiplier

    result = controller.multiply(multiplicand, multiplier)

    assert result == product
