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

        try:
            temp_temperature = self.dhtDevice.temperature
            temp_humidity = self.dhtDevice.humidity

            if temp_temperature != 0:
                self.temperature_c = self.dhtDevice.temperature

            if temp_humidity != 0:
                self.humidity = self.dhtDevice.humidity
 
        except RuntimeError as error:
            print(error.args[0])

        except Exception as error:
            print(error.args[0])

        val = {
            "CELSIUS": self.temperature_c,
            "HUMIDITY": self.humidity
        }

        return val
