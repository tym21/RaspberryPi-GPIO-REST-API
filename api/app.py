from flask import Flask, Blueprint
from flask_restful import Api, Resource, reqparse, abort

from api.resources.gpio_state import GPIOState


def create_app():
    # create the app
    flask_app = Flask(__name__)
    # load the config from external file
    flask_app.config.from_pyfile("config.cfg")
    return flask_app


def create_api(app):
    # create the api
    api = Api(app)
    return api


app = create_app()

api_bp = Blueprint("api", __name__)
api = create_api(api_bp)

api.add_resource(GPIOState, '/gpio/<int:gpio>/state')

app.register_blueprint(api_bp)

if __name__ == '__main__':
    # flask doc: allows to access the server in your local network
    app.run(host="0.0.0.0")
