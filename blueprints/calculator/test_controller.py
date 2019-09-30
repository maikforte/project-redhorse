from blueprints.calculator import controller

def test_multiply():
    number = 2
    result = controller.multiply(number)

    assert (result == (number * number))
