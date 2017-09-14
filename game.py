
"""Game logic for simonsays"""
import random

# Constants representing the differently colored lights
RED = 0
GREEN = 1
BLUE = 2

class Game(object):
    """Instance of simonsays game"""

    def __init__(self, lights=None, buzzer=None):
        """Initialize Game object with dict of lights and buzzer"""
        # Initialize lights, buttons, and buzzer
        if lights is None:
            self.lights = []
        else:
            self.lights = lights
        self.buzzer = buzzer
        # Initialize game variables
        self.current_sequence = []
        self.round_number = 0
        self.is_listening = False

    def add_light_with_button(self, index, light, button):
        """Adds light to list of lights"""
        self.lights[index] = (light, button)

    def add_buzzer(self, buzzer):
        """Adds buzzer"""
        self.buzzer = buzzer

    def handle_press(self, source):
        """Method for handling button press"""
        print("Button {} pressed".format(source))
        self.lights[source][0].blink(0.3, 0.3, 1)

    def create_sequence(self, seed=None):
        """Creates a random sequence for round"""
        # Apply the seed, uses system time if None
        random.seed(seed)
        # Create a random sequence of lights for the round
        self.current_sequence = []
        for _ in range(0, self.round_number):
            random_light = random.randint(0, (len(self.lights) - 1))
            self.current_sequence.append(random_light)

    def display_sequence(self):
        """Displays current sequence on lights"""
        pass

    def start_round(self):
        """Starts a new round"""
        pass

    def end_game(self):
        """Ends the game"""
        pass

    def start(self):
        """Starts the game"""
        pass
