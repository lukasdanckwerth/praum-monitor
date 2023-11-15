import random

import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BCM)

# The frequencies in this code was based on the note frequencies found at:
# https://pages.mtu.edu/~suits/notefreqs.html
# Tuned at A4 = 440Hz.

FREQ_C0 = 16.35
FREQ_C4 = 261.63
FREQ_D4 = 293.66
FREQ_E4 = 329.63
FREQ_F4 = 349.23
FREQ_G4 = 392.00
FREQ_A4 = 440.00
FREQ_H4 = 493.88
FREQ_A5 = 523.25

FREQS = [
    FREQ_C0,
    FREQ_C4,
    FREQ_D4,
    FREQ_E4,
    FREQ_F4,
    FREQ_G4,
    FREQ_A4,
    FREQ_H4,
    FREQ_A5
]

DUTY_CYCLE = 30

TONE_DURATION = 0.1
SLEEP_DURATION = 1.6


class Piezo():

    def __init__(self, gpio=5):
        GPIO.setup(gpio, GPIO.OUT)

        self.gpio = gpio
        self.pin = GPIO.PWM(self.gpio, FREQ_C0)

    def play(self, freq=FREQ_C0):
        GPIO.output(self.gpio, GPIO.HIGH)
        self.pin.start(50)
        self.pin.ChangeFrequency(freq)

    def stop(self):
        GPIO.output(self.gpio, GPIO.LOW)
        self.pin.stop()

    def set_frequency(self, freq):
        self.pin.ChangeFrequency(freq)

    def play_frequency(self, freq):
        self.set_frequency(freq)
        self.play()

    def alarm(self, count=5):
        index = 0
        while index < count:
            self.play()
            sleep(TONE_DURATION)
            self.pause()
            sleep(SLEEP_DURATION)
            index += 1

    def melodey(self):

        self.play(FREQS[1])
        sleep(0.25)

        self.stop()
        sleep(0.1)

        self.play(FREQS[1])
        sleep(0.25)

        self.stop()
        sleep(0.1)

        self.play(FREQS[2])
        sleep(0.5)

        self.play(FREQS[1])
        sleep(0.25)

        self.stop()
        sleep(0.1)

        self.play(FREQS[1])
        sleep(0.25)

        self.stop()
        sleep(0.1)

        self.play(FREQS[3])
        sleep(0.5)

        self.stop()

        # for freq in FREQS:
        #     self.play(freq)
        #     sleep(SLEEP_DURATION)
