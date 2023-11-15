import time
import board
import adafruit_dht

class ClimateSensor():

    def __init__(self, gpio=12):
        self.dhtDevice = adafruit_dht.DHT22(board.D12, use_pulseio=False)
        self.temperature_c = 0
        self.humidity = 0
        print("ClimateSensor started")

    def read(self):

        val = {}
        # val["CELSIUS"] = self.temperature_c
        # val["HUMIDITY"] = self.humidity

        val["CELSIUS"] = 0
        val["HUMIDITY"] = 0

        try:
            self.temperature_c = self.dhtDevice.temperature
            self.humidity = self.dhtDevice.humidity

            val["CELSIUS"] = self.temperature_c
            val["HUMIDITY"] = self.humidity
 
        except RuntimeError as error:
            print(error.args[0])

        except Exception as error:
            print(error.args[0])

        return val
