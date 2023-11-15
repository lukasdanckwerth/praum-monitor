import time
import RPi.GPIO as GPIO

class MovementSensor():

    def __init__(self, gpio=4):
        self.gpio = gpio
        GPIO.setup(self.gpio, GPIO.IN)
        print("MovementSensor started")

    def read(self):
        return GPIO.input(self.gpio)
