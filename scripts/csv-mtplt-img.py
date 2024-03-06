import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('static/img1.jpg',0)
print(img)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.show()