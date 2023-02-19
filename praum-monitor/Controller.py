import RPi.GPIO as GPIO
import time
from threading import Thread
from DataDirectory import DataDirectory
from sensors.MQ4 import MQ4
from sensors.MQ135 import MQ135
from sensors.SoundSensor import SoundSensor
from devices.TrafficLight import TrafficLight
from devices.PiezoBuzzer import PiezoBuzzer

MQ4_GASES = ["CH4", "LPG", "H2", "SMOKE", "ALCOHOL", "CO"]
MQ135_GASES = ["ACETON", "TOLUENO", "ALCOHOL", "CO2", "NH4", "CO"]


class Controller():

    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        self.data_directory = DataDirectory("data")
        self.mq4 = MQ4()
        self.mq135 = MQ135()
        self.soundSensor = SoundSensor()

        self.tl1 = TrafficLight(gpio_green=21, gpio_yellow=22, gpio_red=23)
        # self.tl2 = TrafficLight(gpio_green=21, gpio_yellow=22, gpio_red=23)
        # self.tl3 = TrafficLight(gpio_green=21, gpio_yellow=22, gpio_red=23)

        self.buzzer = PiezoBuzzer(gpio=26)

    def loop(self):
        try:
            index = 0
            while True:
                perc4 = self.mq4.MQPercentage()
                perc135 = self.mq135.MQPercentage()

                text = "MQ4_GASES:\n"
                for gas in MQ4_GASES:
                    text += gas.ljust(10) + " {:.16f}\n".format(perc4[gas])

                text += "\nMQ135_GASES:\n"
                for gas in MQ135_GASES:
                    text += gas.ljust(10) + " {:.16f}\n".format(perc135[gas])

                self.data_directory.add_record(text)

                # avoid overloading cpu
                time.sleep(1)

                index += 1
                print("Round: " + str(index), end="\r")

        except KeyboardInterrupt:
            print("User abort.")
            exit(0)

        except Exception as e:
            print("Error: " + str(e))
            exit(1)


def run_controller():
    print("Initializing controller")

    controller = Controller()

    print("Controller will loop forever\n")
    controller.loop()

    # def loop_forever(controller):
    #     print("controller starting\n")
    #     controller.loop()
    #     print("controller left infinite request loop")
    #
    # thread = Thread(target=loop_forever, args=(controller,))
    # thread.setDaemon(True)
    # thread.start()


if __name__ == '__main__':
    run_controller()
