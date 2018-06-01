#!/usr/bin/python3

import cv2
import matplotlib.pyplot as plt
# reading images 
img=cv2.imread('dogs.jpg',cv2.IMREAD_COLOR)
img1=cv2.imread('dogs.jpg',cv2.IMREAD_GRAYSCALE)
img2=cv2.imread('dogs.jpg',cv2.IMREAD_UNCHANGED)
#print(img.shape)
# showing image
cv2.imshow('windwo',img)
cv2.imshow('windwo1',img1)
cv2.imshow('windwo2',img2)

k=cv2.waitKey(0)
if k == 27 :  #  for esc button 
    cv2.destroyAllWindows()
elif k == ord('s') :
    cv2.imwrite('save.jpg',img1)
    cv2.destroyAllWindows()



