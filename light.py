"""module containing logic for lights"""
import pykka
from gpiozero import LED

ON = 1
OFF = 0

class Light(pykka.ThreadingActor):
    """An LED light"""

    def __init__(self, pin=None, initial_value=OFF):
        super(Light, self).__init__()
        self.led = LED(pin)
        if initial_value == OFF:
            self.led.off()
        else:
            self.led.on()

    def turn_on(self):
        """Turns on LED"""
        self.led.on()

    def turn_off(self):
        """Turns off LED"""
        self.led.off()