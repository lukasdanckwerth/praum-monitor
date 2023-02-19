import RPi.GPIO as GPIO
import time

from DataDirectory import DataDirectory
from sensors.MQ4 import MQ4
from sensors.MQ135 import MQ135
from sensors.SoundSensor import SoundSensor
from devices.TrafficLight import TrafficLight
from devices.PiezoBuzzer import PiezoBuzzer

MQ4_GASES = ["CH4", "LPG", "H2", "SMOKE", "ALCOHOL", "CO"]
MQ135_GASES = ["ACETON", "TOLUENO", "ALCOHOL", "CO2", "NH4", "CO"]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data_directory = DataDirectory("data")

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    mq4 = MQ4()
    mq135 = MQ135()
    soundSensor = SoundSensor()

    tl1 = TrafficLight(gpio_green=21, gpio_yellow=22, gpio_red=23)
    # tl2 = TrafficLight(gpio_green=21, gpio_yellow=22, gpio_red=23)
    # tl3 = TrafficLight(gpio_green=21, gpio_yellow=22, gpio_red=23)

    pb = PiezoBuzzer(gpio=26)

    try:
        while True:
            perc4 = mq4.MQPercentage()
            perc135 = mq135.MQPercentage()

            text = "MQ4_GASES:\n"
            for gas in MQ4_GASES:
                text += gas.ljust(10) + " {:.16f}\n".format(perc4[gas])

            text += "\nMQ135_GASES:\n"
            for gas in MQ135_GASES:
                text += gas.ljust(10) + " {:.16f}\n".format(perc135[gas])

            # print(text)

            # print("Raw ADC Value: ", soundSensor.read(), end="\r")
            # print("ADC Voltage: " + str(chan.voltage) + "V")

            data_directory.add_record(text)

            # avoid overloading cpu
            time.sleep(1)

    except KeyboardInterrupt:
        print("User abort.")
        exit(0)

    except Exception as e:
        print("Error: " + str(e))
        exit(1)
