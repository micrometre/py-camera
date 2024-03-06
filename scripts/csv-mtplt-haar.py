
import cv2
from matplotlib import pyplot as plt
   
# Opening image
img = cv2.imread('static/img2.jpg',0)
   
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
stop_data = cv2.CascadeClassifier('haarcascades/stop_data.xml')
found = stop_data.detectMultiScale(img_rgb, 
                                   minSize =(20, 20))
# Don't do anything if there's 
# no sign
amount_found = len(found)
# Creates the environment 
# of the picture and shows it

if amount_found != 0:
       
    # There may be more than one
    # sign in the image
    for (x, y, width, height) in found:
           
        # We draw a green rectangle around
        # every recognized sign
        cv2.rectangle(img_rgb, (x, y), 
                      (x + height, y + width), 
                      (0, 255, 0), 5)


plt.subplot(1, 1, 1)
plt.imshow(img_rgb)
plt.show()