from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print(
        "Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by "
        "using 'sudo' to run your script")

gpio_put_args = reqparse.RequestParser()
gpio_put_args.add_argument("state", type=int, help="Status of the GPIO is required", required=True)


def check_gpio_valid(gpio):
    if gpio > 26:
        abort(404, message="Pin is not valid")


def check_state_valid(status):
    if not (status == 0 or status == 1):
        abort(404, message="Status is not valid")


def set_gpio(gpio, state):  # witch check
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(gpio, GPIO.OUT)
    GPIO.output(gpio, state)
    state = GPIO.input(gpio)
    return state


def get_gpio(gpio):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(gpio, GPIO.OUT)
    state = GPIO.input(gpio)
    return state

class GPIOCleanup:
    def post(self):
        GPIO.cleanup()


class GPIOState(Resource):
    @staticmethod
    def get(gpio):
        check_gpio_valid(gpio)
        return {"gpio": gpio,
                "state": get_gpio(gpio)
                }

    @staticmethod
    def put(gpio):
        check_gpio_valid(gpio)
        args = gpio_put_args.parse_args()
        requested_state = args["state"]
        check_state_valid(requested_state)
        state = set_gpio(gpio, requested_state)
        return {"gpio": gpio,
                "state": state
                }


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
api = create_api(app)
api.add_resource(GPIOState, '/gpio/<int:gpio>/state')


if __name__ == '__main__':
    # flask doc: allows to access the server in your local network
    app.run(host="0.0.0.0")
