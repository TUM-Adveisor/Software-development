import sys
sys.path.insert(1, '/home/pi/Desktop/Adveisor/Hardware/gcodelib')
import gcodelib
import time

class Bewegungssystem():
    connection=None
   
    config=None
    #nl=0
    def __init__(self,config):
        self.config=config
        self.connection = gcodelib.Connection("/dev/ttyUSB0")
        self.connection.console_read()
        self.aktuel=[0,0]
        self.neu=[0,0]
        
        self.connection.home()
    def bewege_von_nach(self,x_start,y_start,x_end,y_end, note):
        self.neu[0]=x_start
        self.neu[1]=y_start
        #self.nl=self.nl+1
        #print(self.nl)
        if y_start<0 or x_start<0 or y_end<0 or x_end<0: 
            
            #or y_start>410 or x_start>400 or y_end>=10 or x_end>400:
            print("moving out of range")
        else:
            print(note)
            self.connection.magnet_control(False)
            #print("magnet off")
            if self.neu!=self.aktuel:
            
                
                self.connection.send_coords(x_start,y_start)
                self.connection.wait_for_movement_start()
                #print("header started")
                while (self.connection._status != "Idle"):
                    #self.connection.print_coords()
                    time.sleep(2/10)
                #print("header stopped")

            self.connection.magnet_control(True)
            time.sleep(3/10)
            #print("magnet on")
            self.connection.send_coords(x_end,y_end)
            self.connection.wait_for_movement_start()
            #print("header started")
            while (self.connection._status != "Idle"):
                #self.connection.print_coords()
                time.sleep(2/10)
            #print("header stopped")
            self.connection.magnet_control(False)
            #print("magnet off")
            self.aktuel[0]=x_end
            self.aktuel[1]=y_end
    