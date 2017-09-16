"""
Simon says game
"""

class Game(object):
    """
    Instance of simon says game
    """

    def __init__(self):
        """
        Create simon says game instance
        """
        pass

    def start(self):
        """
        Start main game loop
        """
        # Game loop to continue unless KeyBoardInterrupt
        try:
            print("Starting simonsays game")
            while True:
                continue
        except KeyboardInterrupt:
            print("Stopping simonsays game")


# Start game if run as executable
if __name__ == '__main__':
    GAME = Game()
    GAME.start()
