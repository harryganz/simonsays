
"""Game logic for simonsays"""
import random

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
        self.is_active = False

    def add_light_with_button(self, light, button):
        """Adds light to list of lights"""
        self.lights.append((light, button))

    def add_buzzer(self, buzzer):
        """Adds buzzer"""
        self.buzzer = buzzer

    def handle_press(self, source):
        """Method for handling button press"""
        if self.is_listening:
            # Flash current source light
            self.lights[source][0].flash(0.3, 0.3, 1, background=False)
            # Check if source matches next item in current_sequence
            next_item = self.current_sequence[0]
            if source == next_item:
                # Check if round is over
                if len(self.current_sequence) == 1:
                    # If no more items, start next round
                    self.start_round()
                else:
                    # Else clear next item
                    self.current_sequence = self.current_sequence[1:]
            else:
                # If the game is active end it
                if self.is_active:
                    self.end_game()
                # Otherwise start a new game
                else:
                    self.start_game()

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
        for i in range(0, len(self.current_sequence)):
            # Flash each light in the sequence
            self.lights[self.current_sequence[i]][0].flash(0.3, 0.3, 1, background=False)

    def start_round(self):
        """Starts a new round"""
        # Turn off listening
        self.is_listening = False
        # Play buzzer to indicate new round
        self.buzzer.beep(0.5, 0, 1, background=False)
        # Increment round number
        self.round_number = self.round_number + 1
        # Create sequence for this round
        self.create_sequence()
        # Display new sequence
        self.display_sequence()
        # Play buzzer to indicate that it is now listening
        self.buzzer.beep(0.5, 0, 1, background=False)
        # Start listening for input
        self.is_listening = True

    def end_game(self):
        """Ends the game"""
        # Play the buzzer three times
        self.buzzer.beep(0.3, 0.3, 3, background=False)
        # Set is_active to false
        self.is_active = False

    def start_game(self):
        """Starts the game"""
        # Set is_active to True
        self.is_active = True
        # Reset round_number to zero
        self.round_number = 0
        # Start a new round
        self.start_round()
