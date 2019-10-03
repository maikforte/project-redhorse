from blueprints.calculator import controller


def test_add():
    augend = 3
    addend = 3
    sum = augend + addend

    result = controller.add(augend, addend)

    assert result == sum


def test_subtract():
    minuend = 3
    subtrahend = 3
    difference = minuend - subtrahend

    result = controller.subtract(minuend, subtrahend)

    assert result == difference


def test_multiply():
    multiplicand = 2
    multiplier = 3
    product = multiplicand * multiplier

    result = controller.multiply(multiplicand, multiplier)

    assert result == product
