from gpiozero import LED


class TrafficLight:

    def __init__(self, gpio_green, gpio_yellow, gpio_red):
        self.gpio_green = gpio_green
        self.green = LED(gpio_green)

        self.gpio_yellow = gpio_yellow
        self.yellow = LED(gpio_yellow)

        self.gpio_red = gpio_red
        self.red = LED(gpio_red)

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
