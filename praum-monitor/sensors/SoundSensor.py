import time
import math
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn


class SoundSensor():

    def __init__(self, Ro=10):
        self.Ro = Ro
        # create the spi bus
        spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

        # create the cs (chip select)
        # cs = digitalio.DigitalInOut(board.D8)
        cs = digitalio.DigitalInOut(board.D8)

        # create the mcp object
        mcp = MCP.MCP3008(spi, cs)

        # create an analog input channel on pin 3 for SoundSensor
        self.chan_SoundSensor = AnalogIn(mcp, MCP.P2)

        print("SoundSensor started")

    def read(self):
        return self.chan_SoundSensor.value
