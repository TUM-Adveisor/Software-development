import gcodelib
import time

class Bewegungssystem():
    def __init__(self):
        connection = gcodelib.Connection("/dev/ttyUSB0")
        connection.console_read()
        connection.home()
    def bewege_von_nach(self,x_start,y_start,x_end,y_end, note):
        pass