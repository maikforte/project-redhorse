import json
from app import app

ENDPOINT = "/calculator"

app.config["TESTING"] = True
client = app.test_client()


def test_add():
    augend = 3
    addend = 3
    sum = augend + addend

    response = client.get("{}/add?augend={}&addend={}".format(ENDPOINT, augend, addend))

    response_data = json.loads(response.data)

    assert response.status_code == 200
    assert response_data["sum"] == sum


def test_subtract():
    request_body = {"minuend": 2, "subtrahend": 3}

    difference = request_body["minuend"] - request_body["subtrahend"]

    response = client.post(
        "{}/subtract".format(ENDPOINT), data=json.dumps(request_body)
    )

    response_data = json.loads(response.data)

    assert response.status_code == 200
    assert response_data["difference"] == difference


def test_multiply():
    request_body = {"multiplicand": 2, "multiplier": 3}

    product = request_body["multiplicand"] * request_body["multiplier"]

    response = client.put("{}/multiply".format(ENDPOINT), data=json.dumps(request_body))

    response_data = json.loads(response.data)

    assert response.status_code == 200
    assert response_data["product"] == product


def test_divide():
    request_body = {"dividend": 4, "divisor": 2}

    quotient = request_body["dividend"] / request_body["divisor"]

    response = client.delete(
        "{}/divide".format(ENDPOINT), data=json.dumps(request_body)
    )

    response_data = json.loads(response.data)

    assert response.status_code == 200
    assert response_data["quotient"] == quotient
