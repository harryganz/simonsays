"""
Game logic for simon says game
@author Harry Ganz
@date September 14, 2017
@version 0.1.0
"""

import random

class Game(object):
    """
    Instance of simon says game

    Attributes:
        lights: An array of gpiozero.LED objects
        buttons: An array of gpiozero.Button objects
        buzzer: A gpiozero.Buzzer object
    """

    def __init__(self, lights, buttons, buzzer):
        """
        Initializes Game object
        @param lights: An array of gpiozero.LED instances
        @param buttons: An array of gpiozero.Button instances
        @param buzzer: A gpiozero.Buzzer instance
        @raise Exception: throws exception if lights and button arrays
        are not the same size
        """
        if len(lights) != len(buttons):
            raise Exception("lights array and button array must be the same size")

        self.lights = lights
        self.buttons = buttons
        self.buzzer = buzzer
        for i in range(0, len(buttons)):
            self.buttons[i].when_pressed = lambda : self.on_press(i)

        # Initialize game variables
        self.round_num = 0
        self.current_sequence = []
        self.is_active = False
        self.is_ready = False
        self.is_listening = False

    def on_press(self, source):
        """
        Method to carry out when button is pressed
        @source: The index of the pressed button
        """
        if self.is_listening:
            if self.is_active:
                self.lights[source].blink(0.3, 0.1, 1, background=False)
                if source == self.current_sequence[0]:
                    if len(self.current_sequence) == 1:
                        self.is_ready = True
                    else:
                        self.current_sequence = self.current_sequence[1:]
                else:
                    self.is_ready = True
                    self.is_active = False
            else:
                self.is_ready = True
                self.is_active = True

    def start_round(self):
        """Starts the current round"""

        # Reset round variables
        self.current_sequence = []
        self.is_ready = False
        self.is_listening = False
        # Increment round number
        self.round_num = self.round_num + 1
        # Create new sequence
        self.create_sequence()
        # Display current round sequence
        self.display_sequence()
        # Beep buzzer twice to indicate start of round
        self.buzzer.beep(0.3, 0.3, 2, background=False)
        # Set listening to true
        self.is_listening = True
        # Until is_ready is true, wait
        while not self.is_ready:
            # Wait
            continue
        if self.is_active:
            self.start_round()
        else:
            self.game_over()

    def create_sequence(self, seed=None):
        """
        Creates the sequence to use in the current round
        @param seed: The random seed to use. If None (default)
        will get seed from system
        """
        random.seed(seed)
        for _ in range(0, self.round_num):
            random_light = random.randint(0, len(self.lights) - 1)
            self.current_sequence.append(random_light)

    def display_sequence(self):
        """
        Displays the current sequence of lights
        """
        for i in range(0, len(self.current_sequence)):
            self.lights[i].blink(0.3, 0.3, 1, background=False)
        # Beep buzzer once to indicate beggining of listening
        self.buzzer.beep(0.3, 0.3, 1, background=False)

    def game_over(self):
        """When game is over, waits for input to restart"""
        self.buzzer.beep(1, 0, 1, background=False)
        self.is_ready = False
        self.is_listening = True
        while not self.is_ready:
            # Wait
            continue
        self.game_start()

    def game_start(self):
        """Starts game"""
        try:
            self.start_round()
        except KeyboardInterrupt:
            print("Exiting...")
