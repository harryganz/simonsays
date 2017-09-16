"""
Simon says game
"""
import gpiozero

class Game(object):
    """
    Instance of simon says game
    """

    def __init__(self, light_pins, led=gpiozero.LED):
        """
        Create simon says game instance
        @param light_pins: array of pins to use for lights
        @param led: Class to use to handle lights (default gpiozero.LED)
        """
        self.lights = []
        for pin in light_pins:
            self.lights.append(led(pin))

    def start(self):
        """
        Start main game loop
        """
        # Game loop to continue unless KeyBoardInterrupt
        try:
            print("Starting simonsays game")
            while True:
                for light in self.lights:
                    light.blink(0.3, 0.3, 1, background=False)
        except KeyboardInterrupt:
            print("Stopping simonsays game")


# Start game if run as executable
if __name__ == '__main__':
    GAME = Game([17, 5, 19])
    GAME.start()
