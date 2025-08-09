import cv2
import numpy as np
import matplotlib.pyplot as plt


def show(img,cma=['gray']):
    fig=plt.figure(figsize=(12,10))
    ax=fig.add_subplot(111)
    ax.imshow(img,*cma)
    
# sepcoins=cv2.imread(r'Computer-Vision-with-Python\DATA\pennies.jpg',1)

# show(sepcoins)

# #median blur to remove faces
# # binary threshold to make Black and white and contours

# scb=cv2.medianBlur(sepcoins,25)
# # show(scb)

# gscb=cv2.cvtColor(scb,cv2.COLOR_BGR2GRAY)
# show(gscb)
