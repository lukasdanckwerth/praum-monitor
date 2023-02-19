from sensors import *
from MCP3008 import MCP3008

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

print("Press CTRL+C to abort.")

# mq = MQ4();
# mq135 = MQ135();

adc = MCP3008()

while True:
    # perc4 = mq.MQPercentage()
    # print("MQ4 measurment")
    # sys.stdout.write("\r")
    # sys.stdout.write("\033[K")
    # sys.stdout.write("Raw_value:   %g, \nCH4:         %g ppm, \nLPG:         %g ppm, \nH2:          %g ppm, \nSmoke:       %g ppm, \nAlcohol:     %g ppm, \nCO:          %g ppm" % (perc4["RAW_VALUE"], perc4["CH4"], perc4["LPG"], perc4["H2"], perc4["SMOKE"], perc4["ALCOHOL"], perc4["CO"]))
    # sys.stdout.flush()
    # print("\n\n")

    # perc135 = mq135.MQPercentage()
    # print("MQ135 measurment")
    # sys.stdout.write("\r")
    # sys.stdout.write("\033[K")
    # sys.stdout.write()
    # sys.stdout.flush()
    # print("\n\n")

    # print("\r", end='')
    # print("Raw_value:   %g, \nACETON:      %g ppm, \nTOLUENO:     %g ppm, \nALCOHOL:     %g ppm, \nCO2:         %g ppm, \nNH4:         %g ppm, \nCO:          %g ppm" % (perc135["RAW_VALUE"], perc135["ACETON"], perc135["TOLUENO"], perc135["ALCOHOL"], perc135["CO2"], perc135["NH4"], perc135["CO"]), end='')
    # sys.stdout.flush()

    # print('CO2: ' + str(perc135["CO2"]), end='\r')
    # print('SMOKE: ' + str(perc4["SMOKE"]), end='\r')
    
    value = adc.read(2)
    print("value: %.2f" % (value), end="\r")

    time.sleep(0.5)
    