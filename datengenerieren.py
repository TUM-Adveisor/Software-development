import cv2
 
# read image as grey scale
grey_img = cv2.imread('/home/pi/Adveisor/Software/Software/adveisor.png', cv2.IMREAD_GRAYSCALE)
 
# save image
status = cv2.imwrite('//home/pi/Adveisor/Software/Software/adveisor.png',grey_img)