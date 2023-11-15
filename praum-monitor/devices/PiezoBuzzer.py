import random

import RPi.GPIO as GPIO
from time import sleep

TONE_DURATION = 0.6
SLEEP_DURATION = 0.6

class PiezoBuzzer():

    def __init__(self, gpio=6):
        GPIO.setup(gpio, GPIO.OUT)
        self.gpio = gpio

    def play(self):
        GPIO.output(self.gpio, GPIO.HIGH)

    def pause(self):
        GPIO.output(self.gpio, GPIO.LOW)

    def play_for(self, duration=0.06):
        self.play()
        sleep(duration)
        self.pause()

    def alarm(self, count=3):
        index = 0
        while index < count:
            self.play()
            sleep(TONE_DURATION)
            self.pause()
            sleep(SLEEP_DURATION)
            index += 1
