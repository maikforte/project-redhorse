import json
from app import app

ENDPOINT = '/calculator'

app.config['TESTING'] = True
client = app.test_client()

def test_multiply():
    multiplicand = 2
    multiplier = 3
    product = multiplicand * multiplier

    response = client.get('{}/multiply?multiplicand={}&multiplier={}'.format(ENDPOINT, multiplicand, multiplier))
    response_data = json.loads(response.data)

    assert (response.status_code == 200)
    assert (response_data['product'] == product)
