import cv2
from cv2 import imread
import numpy as np

import matplotlib.pyplot as plt
# func is cv2.imread((path,flag))
# flag is the way of reading 
img=imread("isac_potrait.jpg",1) #the 1 is cv2.IMREAD_COLOR 0 is cv2.IMREAD_GRAYSCALE, -1 is cv2.IMREAD_UNCHANGED
# cv2.imshow("image",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# plt.imshow(img)
# plt.waitforbuttonpress()
# plt.close('all')

#cv2 uses BGR and matplotlib uses RGB

#BGR to RGB is done by a func called cvtColor(img,cv2.COLOR_BGR2RGB)
RGB_img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

# plt.imshow(RGB_img)
# plt.waitforbuttonpress()
# plt.close("all")

GS_img=imread("isac_potrait.jpg",0)
# cv2.imshow("image",GS_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# plt.imshow(GS_img)
# plt.waitforbuttonpress()
# plt.close("all")

# shape atribute of imread obj lyk the size
# print(img.shape)

# save an image with imwrite("path",img_obj)
# cv2.imwrite(r"D:\zaynu\Documents\pythonfiles\CV_mod\newimg.jpg",img)
# im read returns none if image not read cirrectly

#cv2.imshow("image1",img)#first param is name of Window
#cv2.imshow("image2",img)
#key=cv2.waitKey(0)#waitkey returns the key entered
# if key==ord("q"):
#     print("q pressed")
#print(key)
#cv2.destroyAllWindows()
#cv2.destroyWindow("image")takes the name of window to destroy
#cv2.split() returns the colour codes seperrated in ( B,G,R)
B,G,R=cv2.split(img)

# cv2.add(img1,img2) 
# cv2.addweighted(img1,wt1,image2,wt2,gamma val).is used to fix images gamma 
#gamma is measurement of light
saitama=imread(r"CV_mod\imagestouse\acid rain saitama.jpg")
oceanimg=imread(r"CV_mod\imagestouse\Screenshot 2023-05-08 214541.png")

'''

weightedimg=cv2.addWeighted(saitama,0.6,oceanimg,0.3,0)

'''
#must be of same size
# cv2.imshow("weighted",weightedimg)
# cv2.waitKey(0)
# cv2.destroyAllWindows()





#image substraction via substract(img1,img2)

# bitwise AND OR NOT XOR


                                            # UDEMY COURSE

imgad=r"D:\zaynu\Pictures\dumb photos\evil anya.png"

img=cv2.imread(imgad)
fixed=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# cv2.imshow("anya",img)
plt.imshow(fixed)
plt.waitforbuttonpress()
# while True:
    
#     if cv2.waitKey(1) & 0XFF == 27:
#         break

while True:
    
    if cv2.waitKey(0)  == ord('q'):
        break
plt.close("all")
# cv2.destroyAllWindows()




