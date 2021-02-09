from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

gpio_put_args = reqparse.RequestParser()
gpio_put_args.add_argument("status", type=int, help="Status of the GPIO is required", required=True)


def check_gpio(pin):
    if pin > 26:
        abort(404, message="Pin is not valid")


def check_status(status):
    if not status == 0 or status == 1:
        abort(404, message="Status is not valid")


class GPIOControl(Resource):
    def get(self, gpio):
        check_gpio(gpio)
        status = 1
        return {"gpio": gpio,
                "status": status
                }

    def put(self, pin):
        check_gpio(pin)
        args = gpio_put_args.parse_args()
        check_status(args["status"])
        return {"gpio": pin,
                "status": args["status"]
                }


def create_app():
    # create the app
    flask_app = Flask(__name__)
    # load the config from external file
    flask_app.config.from_pyfile("config.cfg")
    return flask_app


def create_api(app):
    api = Api(app)
    return api


app = create_app()
api = create_api(app)
api.add_resource(GPIOControl, '/gpio/<int:pin>/status')

if __name__ == '__main__':
    app.run()
