import time
import RPi.GPIO as GPIO

class MovementSensor():

    READ_SAMPLE_INTERVAL         = 100       # define the time interval(in milisecond) between each samples in
    READ_SAMPLE_TIMES            = 7         # define how many samples you are going to take in normal operation

    def __init__(self, gpio=4):
        self.gpio = gpio
        GPIO.setup(self.gpio, GPIO.IN)
        print("MovementSensor started")

    def read(self):
        raw_value = 0.0
        for i in range(self.READ_SAMPLE_TIMES):
            raw_value += GPIO.input(self.gpio)
            time.sleep(self.READ_SAMPLE_INTERVAL/1000.0)

        raw_value = raw_value / self.READ_SAMPLE_TIMES

        return raw_value
