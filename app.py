from flask import Flask
from blueprints.calculator import calculator
from flasgger import Swagger

app = Flask(__name__)
app.debug = True

app.register_blueprint(calculator, url_prefix='/calculator')

swagger = Swagger(app)

if __name__ == '__main__':
    app.run()
