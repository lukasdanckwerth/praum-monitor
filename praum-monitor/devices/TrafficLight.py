from gpiozero import LED
from time import sleep


class TrafficLight:
    warning_varlue = 0.5
    alert_varlue = 0.75

    def __init__(self, gpio_green, gpio_yellow, gpio_red):
        self.gpio_green = gpio_green
        self.green = LED(gpio_green)

        self.gpio_yellow = gpio_yellow
        self.yellow = LED(gpio_yellow)

        self.gpio_red = gpio_red
        self.red = LED(gpio_red)

        self.value = 0

    def turn_off(self):
        self.green.off()
        self.yellow.off()
        self.red.off()

    def turn_on(self):
        self.green.on()
        self.yellow.on()
        self.red.on()

    def green_on(self):
        self.green.on()

    def green_off(self):
        self.green.off()

    def yellow_on(self):
        self.yellow.on()

    def yellow_off(self):
        self.yellow.off()

    def red_on(self):
        self.red.on()

    def red_off(self):
        self.red.off()

    def set_value(self, value):
        self.value = value
        if value > self.alert_varlue:
            self.red_on()
            self.yellow_off()
            self.green_off()
        elif value > self.warning_varlue:
            self.red_off()
            self.yellow_on()
            self.green_off()
        else:
            self.red_off()
            self.yellow_off()
            self.green_on()

    def animate(self):
        self.green_on()
        sleep(0.33)
        self.green_off()
        self.yellow_on()
        sleep(0.33)
        self.yellow_off()
        self.red_on()
        sleep(0.33)
        self.red_off()
