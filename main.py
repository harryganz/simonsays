"""Main module that runs the game"""
from game import Game, RED, BLUE, GREEN
from _mocks import MockLight, MockButton

if __name__ == '__main__':
    GAME = Game(lights={RED: (MockLight(1), MockButton(2))})
    GAME.add_light_with_button(GREEN, MockLight(3), MockButton(4))
    GAME.start()