"""
Simon says game
"""
import gpiozero
from time import sleep

class Game(object):
    """
    Instance of simon says game
    """

    def __init__(self, light_pins, button_pins, led=gpiozero.LED, button=gpiozero.Button):
        """
        Create simon says game instance
        @param light_pins: array of pins to use for lights
        @param button_pins: array of pins to use for buttons
        @param led: Class used for lights (default gpiozero.LED)
        @param button: Class used for buttons (default gpiozero.Button)
        """
        # Add lights
        self.lights = []
        for pin in light_pins:
            self.lights.append(led(pin))
        self.buttons = []
        # Add buttons
        for pin in button_pins:
            self.buttons.append(button(pin))
        # Check that lights and buttons are same length
        if len(self.buttons) != len(self.lights):
            raise Exception("Must have the same nubmer of buttons and lights")

    def get_source(self):
        """
        Returns the index of the button that is being pressed
        If more than one button is being pressed, 
        returns the one with the lowest index
        """
        for i in range(0, len(self.buttons)):
            button = self.buttons[i]
            if button.is_pressed:
                return i
        return -1

    def handle_press(self):
        """
        Handles logic for when a button is 
        pressed
        """
        # Source of the press
        source = self.get_source()
        # If a button was pressed
        if source > -1:
            # Blink the corresponding LED
            self.lights[source].blink(0.3, 0.3, 1, background=True)

    def start(self):
        """
        Start main game loop
        """
        # Game loop to continue unless KeyBoardInterrupt
        try:
            print("Starting simonsays game")
            while True:
                self.handle_press()
                sleep(0.1)
        except KeyboardInterrupt:
            print("Stopping simonsays game")


# Start game if run as executable
if __name__ == '__main__':
    GAME = Game([17, 5, 19], [27, 6, 26])
    GAME.start()
