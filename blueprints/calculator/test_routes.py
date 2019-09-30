from app import app

app.config['TESTING'] = True
client = app.test_client()

def test_multiply():
    response = client.get('/calculator/multiply?number=2')
    assert (response.status_code == 200)
