from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")
gpio_put_args = reqparse.RequestParser()
gpio_put_args.add_argument("status", type=int, help="Status of the GPIO is required", required=True)


def check_gpio(pin):
    if pin > 26:
        abort(404, message="Pin is not valid")


def check_status(status):
    if not status == 0 or status == 1:
        abort(404, message="Status is not valid")


def set_GPIO(gpio, state): #witch check
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(gpio, GPIO.OUT)
    GPIO.output(gpio, state)
    state = GPIO.input(gpio)
    GPIO.cleanup(gpio)
    return state

def get_GPIO(gpio):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(gpio, GPIO.OUT)
    state = GPIO.input(gpio)
    GPIO.cleanup(gpio)
    return state



class GPIOControl(Resource):
    def get(self, gpio):
        check_gpio(gpio)
        status = 1
        return {"gpio": gpio,
                "status": status
                }

    def put(self, gpio):
        check_gpio(gpio)
        args = gpio_put_args.parse_args()
        check_status(args["status"])
        set_GPIO(gpio, args["status"])
        return {"gpio": gpio,
                "status": args["status"]
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
api.add_resource(GPIOControl, '/gpio/<int:pin>/status')

if __name__ == '__main__':
    app.run(host="0.0.0.0")
