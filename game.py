"""
Simon says game
"""
from time import sleep
import random
import gpiozero

class Game(object):
    """
    Instance of simon says game
    """

    def __init__(self, light_pins, button_pins, buzzer_pin,
                 led=gpiozero.LED, button=gpiozero.Button, buzzer=gpiozero.Buzzer):
        """
        Create simon says game instance
        @param light_pins: array of pins to use for lights
        @param button_pins: array of pins to use for buttons
        @param buzzer_pin: io pin for the buzzer
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
        # Add buzzer
        self.buzzer = buzzer(buzzer_pin)
        # Game state variables
        self.is_active = False
        self.is_listening = True
        self.round_num = 0
        self.round_sequence = []
  
    def generate_sequence(self, seed=None):
        """
        Generates a random sequence of LEDs to
        blink for the current round
        @param seed: The random seed to use (default None)
        """
        # Set the random seed, uses system default if None
        random.seed(seed)

        # Create a sequence for the current round of length round_num
        self.round_sequence = []
        for _ in range(0, self.round_num):
            rand_led = random.randint(0, len(self.lights) - 1)
            self.round_sequence.append(rand_led)

    def display_sequence(self):
        """
        Displays the sequence of lights for this round
        on the LEDs
        """
        for light in self.round_sequence:
            self.lights[light].blink(0.3, 0.3, 1, background=False)

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
            # If game is not active, start it
            if not self.is_active:
                self.round_num = 0
                self.is_active = True
                self.is_listening = False
            else:
                # Blink the corresponding LED
                self.lights[source].blink(0.3, 0.3, 1, background=False)
                # Match source to first item in sequence
                if source == self.round_sequence[0]:
                    # Remove the first item
                    self.round_sequence = self.round_sequence[1:]
                    # If no more items, start next round (empty sequences are falsy)
                    if not self.round_sequence:
                        self.is_listening = False
                else:
                    # Game over, beep for game end
                    self.buzzer.beep(1, 0.3, 1, background=False)
                    # Deactivate game
                    self.is_active = False
                    self.is_listening = True

    def start_round(self):
        """
        Runs for a new round
        """
        # Beep Twice to signal new round
        self.buzzer.beep(0.3, 0.3, 2, background=False)
        # Change variables
        self.round_num = self.round_num + 1

        # Create and display sequence for current round
        self.generate_sequence()
        self.display_sequence()

        # Beep Twice and listen for input
        self.buzzer.beep(0.3, 0.3, 2, background=False)
        self.is_listening = True

    def start(self):
        """
        Start main game loop
        """
        # Game loop to continue unless KeyBoardInterrupt
        try:
            print("Starting simonsays game")
            while True:
                if self.is_listening:
                    self.handle_press()
                else:
                    self.start_round()
                sleep(0.1)
        except KeyboardInterrupt:
            print("Stopping simonsays game")


# Start game if run as executable
if __name__ == '__main__':
    GAME = Game([17, 5, 19], [27, 6, 26], 4)
    GAME.start()
