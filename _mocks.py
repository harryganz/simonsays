"""Module for mocking out lights, buttons, and buzzer"""

class MockLight(object):
    """A mock implementation of a light"""

    def __init__(self, pin):
        """Initialize with a pin"""
        self.pin = pin

    def blink(self, on_time=1, off_time=1, n=None, background=True):
        """Prints instead of blinking the light"""
        print(self.pin, on_time, off_time, n, background)

class MockButton(object):
    """A mock implementation of a button"""

    def __init__(self, pin):
        """Initializes MockButton with pin"""
        self.pin = pin
    def _press(self):
        self.when_pressed()

    def _release(self):
        self.when_released()

    def when_pressed(self):
        """Calls this method when pressed"""
        pass

    def when_released(self):
        """Calls this method when released"""
        pass
