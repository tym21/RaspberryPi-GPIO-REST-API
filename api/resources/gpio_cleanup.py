class GPIOCleanup:
    def post(self):
        GPIO.cleanup()