from flask import Flask
from flask_restful import Api


def create_app():
    # create the app
    flask_app = Flask(__name__)
    # load the config from external file
    flask_app.config.from_pyfile("config.cfg")

    @flask_app.route('/hello')
    def hello():
        return 'Hello, World!'

    return flask_app


if __name__ == '__main__':
    app = create_app()
    app.run()
