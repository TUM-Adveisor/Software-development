import sys
sys.path.insert(1, '/home/pi/Adveisor/Hardware/gcodelib')
import gcodelib
import time

class Bewegungssystem():
    connection=None
    #nl=0
    def __init__(self):
        self.connection = gcodelib.Connection("/dev/ttyUSB0")
        self.connection.console_read()
        self.connection.home()
    def bewege_von_nach(self,x_start,y_start,x_end,y_end, note):
        #self.nl=self.nl+1
        #print(self.nl)
        if x_start<0 or y_start<0 or x_end>400 or y_end>405 or x_end<0 or y_end<0 or x_start>400 or y_start>405:
            print("moving out of range")
        else:
            print(note)
            self.connection.magnet_control(False)
            #print("magnet off")
            self.connection.send_coords(x_start,y_start)
            #print("header started")
            while (self.connection._status != "Idle"):
                #self.connection.print_coords()
                time.sleep(1/10)
            #print("header stopped")

            self.connection.magnet_control(True)
            #print("magnet on")
            self.connection.send_coords(x_end,y_end)
            #print("header started")
            while (self.connection._status != "Idle"):
                #self.connection.print_coords()
                time.sleep(1/10)
            #print("header stopped")
            self.connection.magnet_control(False)
            #print("magnet off")