"""Main module, to be run"""
from time import sleep
from light import Light

if __name__ == '__main__':
    RED = Light.start(22).proxy()
    GREEN = Light.start(27).proxy()
    BLUE = Light.start(17).proxy()

    while True:
        try:
            GREEN.turn_on()
            RED.turn_on()
            BLUE.turn_on()
            sleep(1)
            RED.turn_off()
            GREEN.turn_off()
            BLUE.turn_off()
            sleep(1)
        except KeyboardInterrupt:
            RED.stop()
            GREEN.stop()
            BLUE.stop()
            break
