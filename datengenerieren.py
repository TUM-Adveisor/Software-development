import cv2
import games
import config
import player 
import bewegungsystem
import random
import time
bewegungsytem=None
feldgröße_y=1
feldgröße_x=1
felderstart_x=1
felderstart_y=1
start_pos_y=1
start_pox_x=1
max_varation=10

config=config.Config()
b=bewegungsystem.Bewegungssystem(config)
b.bewege_von_nach(40,40,300,300,"test")
b.bewege_von_nach(300,300,400,400,"test")

#b.bewege_von_nach(300,300,30,30,"test")
"""""time.sleep(1)
camera = cv2.VideoCapture(0)
XY_Matrix=[]
def real_to_logic_postion(x_pos,y_pos):
        höhe_feld=feldgröße_x
        breite_feld=feldgröße_y

        for i in range(8):
        
            if y_pos // höhe_feld<i:
                y_pos=i
        
        for i in range(8):
            if x_pos // breite_feld <i:
                x_pos=i
        return[x_pos,y_pos]

def logic_to_real_postion(x_pos,y_pos):

    real_postion_y=felderstart_x+((y_pos)*feldgröße_y)
    real_postion_x=felderstart_x+((x_pos)*feldgröße_x)
    return [real_postion_x,real_postion_y]

for x in range(8):
    for y in range(8):
        for i in range(1):#10 einfügen
            rgb=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]
            end=logic_to_real_postion((x+(random.randint(0,max_varation))),(y+(random.randint(0,max_varation))))
            print(x,y)
            b.bewege_von_nach(start_pox_x,start_pos_y,end[0],end[1],"test")
            start_pox_x=end[0]
            start_pos_y=end[1]
            #return_value, image = camera.read()
            #cv2.imwrite(str(x)+str(y)+str(i)+'figurenname+'+''.png', image)                                         
                
                
                """