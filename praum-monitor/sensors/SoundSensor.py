import time
import RPi.GPIO as GPIO

class SoundSensor():

    READ_TOTAL_TIME              = 1         # 1 second
    READ_SAMPLE_TIMES            = 500       # define how many samples you are going to take in normal operation
    DEVIATION                    = 0.5

    def __init__(self, gpio=18):
        self.gpio = gpio
        GPIO.setup(self.gpio, GPIO.IN)
        print("SoundSensor started")

    def read(self):
        raw_value = 0.0

        for i in range(self.READ_SAMPLE_TIMES):
            raw_value += GPIO.input(self.gpio)
            time.sleep(self.READ_TOTAL_TIME / self.READ_SAMPLE_TIMES)

        rel_value = raw_value / self.READ_SAMPLE_TIMES

        value_reversed = (1 - rel_value) 
        value_rounded = round(value_reversed, 2)

        print("rel_value: " + str(rel_value))

        # raw_value = GPIO.input(self.gpio)

        if value_rounded < 0.051:
            return 0
        else:
            return value_rounded
