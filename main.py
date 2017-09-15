"""Main module that runs the game"""
from gpiozero import LED, Buzzer, Button
from game import Game

if __name__ == '__main__':
    GAME = Game(lights=[(LED(17), Button(27))], buzzer=Buzzer(4))
    GAME.start_game()
    while True:
        continue
