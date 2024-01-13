import RPi.GPIO as GPIO
import time
import io
import csv

from DataDirectory import DataDirectory
from sensors.MQ4 import MQ4
from sensors.MQ135 import MQ135
from sensors.SoundSensor import SoundSensor
from sensors.ClimateSensor import ClimateSensor
from devices.TrafficLight import TrafficLight
from sensors.MovementSensor import MovementSensor
from devices.PiezoBuzzer import PiezoBuzzer
from devices.Piezo import Piezo

MQ4_GASES = ["CH4", "LPG", "H2", "SMOKE", "ALCOHOL", "CO"]
MQ135_GASES = ["ACETON", "TOLUENO", "ALCOHOL", "CO2", "NH4", "CO"]


def format_value(val):
    return "{:.12f}".format(val)


class Controller():

    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        self.data_directory = DataDirectory("/srv/praum-monitor/data")
        self.mq4 = MQ4()
        self.mq135 = MQ135()
        self.soundSensor = SoundSensor()
        self.climateSensor = ClimateSensor()
        self.movementSensor = MovementSensor()

        self.buzzer = PiezoBuzzer()
        self.buzzer.play_for(0.3)

        self.piezo = Piezo()
        self.piezo.melodey()
        
        self.tll = TrafficLight(gpio_green=17, gpio_yellow=27, gpio_red=22)
        self.tlc = TrafficLight(gpio_green=16, gpio_yellow=20, gpio_red=21)
        self.tlr = TrafficLight(gpio_green=26, gpio_yellow=19, gpio_red=13)

        self.tll.turn_on()
        self.tlc.turn_on()
        self.tlr.turn_on()

        self.loop_count = 0
        self.rec = False
        self.records = []

    def get_record(self):
        perc4 = self.mq4.MQPercentage()
        perc135 = self.mq135.MQPercentage()
        movSig = self.movementSensor.read()
        climateSig = self.climateSensor.read()
        soundSig = self.soundSensor.read()

        rec = {
            "LOOP": self.loop_count,

            "CH4": format_value(perc4["CH4"]),
            "LPG": format_value(perc4["LPG"]),
            "H2": format_value(perc4["H2"]),
            "SMOKE": format_value(perc4["SMOKE"]),
            "ALCOHOL": format_value(perc4["ALCOHOL"]),
            "CO": format_value(perc4["CO"]),

            # "ACETON": format_value(perc135["ACETON"]),
            # "TOLUENO": format_value(perc135["TOLUENO"]),
            # "ALCOHOL_2": format_value(perc135["ALCOHOL"]),
            # "CO2": format_value(perc135["CO2"]),
            # "NH4": format_value(perc135["NH4"]),
            # "CO_2": format_value(perc135["CO"]),

            "MOV": movSig,
            "SOUND": soundSig,

            "CELSIUS": format_value(climateSig["CELSIUS"] or 0),
            "HUMIDITY": format_value(climateSig["HUMIDITY"] or 0)
        }
        
        # print("soundSig: " + str(soundSig))

        return rec

    def loop(self):
        self.rec = self.get_record()
        self.data_directory.add_record(self.rec)
        self.loop_count += 1
