import cv2
import games
import config
import player #can be delatet later

#mport bewegungsystem
#config=config.Config()
#b=bewegungsystem.Bewegungssystem(config)
camera = cv2.VideoCapture(0)
return_value, image = camera.read()
cv2.imwrite('opencv'+str(1)+'.png', image)