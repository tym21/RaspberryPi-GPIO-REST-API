from flask_restful import Resource


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
