import RPi.GPIO as GPIO
import time
import io
import csv
import mh_z19

from DataDirectory import DataDirectory

from sensors.SoundSensor import SoundSensor
from sensors.ClimateSensor import ClimateSensor
from sensors.MovementSensor import MovementSensor

from devices.TrafficLight import TrafficLight
from devices.PiezoBuzzer import PiezoBuzzer
from devices.Piezo import Piezo


def format_value(val):
    return "{:.12f}".format(val)


class Controller():

    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        self.data_directory = DataDirectory("/srv/praum-monitor/data")
        self.soundSensor = SoundSensor()
        self.climateSensor = ClimateSensor()
        self.movementSensor = MovementSensor()

        self.buzzer = PiezoBuzzer()
        self.piezo = Piezo()

        self.tll = TrafficLight(gpio_green=17, gpio_yellow=27, gpio_red=22)
        self.tlc = TrafficLight(gpio_green=16, gpio_yellow=20, gpio_red=21)
        self.tlr = TrafficLight(gpio_green=26, gpio_yellow=19, gpio_red=13)

        self.loop_count = 0
        self.rec = False
        self.records = []
        self.before_start()

    def before_start(self):
        self.buzzer.play_for(0.3)
        self.piezo.melodey()

        self.tll.turn_on()
        self.tlc.turn_on()
        self.tlr.turn_on()

    def get_record(self):
        movSig = self.movementSensor.read()
        climateSig = self.climateSensor.read()
        soundSig = self.soundSensor.read()
        mh_z19Sig = mh_z19.read_from_pwm(gpio=25)

        rec = {
            "LOOP": self.loop_count,
            "MOV": movSig,
            "SOUND": soundSig,
            "CELSIUS": format_value(climateSig["CELSIUS"] or 0),
            "HUMIDITY": format_value(climateSig["HUMIDITY"] or 0),
            "CO2": mh_z19Sig["co2"] or 0,
        }

        print(rec)

        return rec

    def loop(self):
        self.rec = self.get_record()
        self.data_directory.add_record(self.rec)
        self.loop_count += 1
