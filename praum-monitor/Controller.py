import RPi.GPIO as GPIO
import time
import io
import csv

from DataDirectory import DataDirectory
from sensors.MQ4 import MQ4
from sensors.MQ135 import MQ135
from sensors.SoundSensor import SoundSensor
from devices.TrafficLight import TrafficLight
from devices.PiezoBuzzer import PiezoBuzzer

MQ4_GASES = ["CH4", "LPG", "H2", "SMOKE", "ALCOHOL", "CO"]
MQ135_GASES = ["ACETON", "TOLUENO", "ALCOHOL", "CO2", "NH4", "CO"]


def format_value(val):
    return "{:.16f}".format(val)


class Controller():

    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        self.data_directory = DataDirectory("data")
        self.mq4 = MQ4()
        self.mq135 = MQ135()
        self.soundSensor = SoundSensor()

        self.loop_count = 0
        self.rec = False
        self.records = []

        self.tl1 = TrafficLight(gpio_green=21, gpio_yellow=22, gpio_red=23)
        # self.tl2 = TrafficLight(gpio_green=21, gpio_yellow=22, gpio_red=23)
        # self.tl3 = TrafficLight(gpio_green=21, gpio_yellow=22, gpio_red=23)

        self.buzzer = PiezoBuzzer(gpio=26)

    def get_record(self):
        perc4 = self.mq4.MQPercentage()
        perc135 = self.mq135.MQPercentage()
        rec = {
            "LOOP": self.loop_count,

            "CH4": format_value(perc4["CH4"]),
            "LPG": format_value(perc4["LPG"]),
            "H2": format_value(perc4["H2"]),
            "SMOKE": format_value(perc4["SMOKE"]),
            "ALCOHOL": format_value(perc4["ALCOHOL"]),
            "CO": format_value(perc4["CO"]),

            "ACETON": format_value(perc135["ACETON"]),
            "TOLUENO": format_value(perc135["TOLUENO"]),
            "ALCOHOL_2": format_value(perc135["ALCOHOL"]),
            "CO2": format_value(perc135["CO2"]),
            "NH4": format_value(perc135["NH4"]),
            "CO_2": format_value(perc135["CO"]),

            "VOL": 0,
            "MOV": 0,
        }
        return rec

    def loop(self):
        self.rec = self.get_record()
        self.data_directory.add_record(self.rec)
        self.loop_count += 1
