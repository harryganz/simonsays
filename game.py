
"""Game logic for simonsays"""

RED = 0
GREEN = 1
BLUE = 2

class Game(object):
    """Instance of simonsays game"""

    def __init__(self, lights=None, buzzer=None):
        """Initialize Game object with dict of lights and buzzer"""
        if lights is None:
            self.lights = {}
        else:
            self.lights = lights
        self.buzzer = buzzer

    def add_light_with_button(self, name, light, button):
        """Adds light to list of lights"""
        self.lights[name] = (light, button)

    def add_buzzer(self, buzzer):
        """Adds buzzer"""
        self.buzzer = buzzer
    
    def handle_press(self, source):
        print("Button {} pressed".format(source))
        self.lights[source][0].blink(0.3, 0.3, 1)

    def handle_release(self, source):
        print("Button {} released".format(source))

    def start(self):
        """Starts the game"""
        for light in self.lights:
            button = self.lights[light][1]
            button.when_pressed = lambda : self.handle_press(light)
            button.when_released = lambda : self.handle_release(light)

        for light in self.lights:
            button = self.lights[light][1]
            button._press()
            button._release()