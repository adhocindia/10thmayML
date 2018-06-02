#!/usr/bin/python3
import  cv2

img1=cv2.imread('dog1.jpg')
img2=cv2.imread('wall.jpg')

print(img1.shape)
print(img2.shape)
#  adding  image with equal contribution 
#  image shape must be common 
#newimg=cv2.add(img1,img2)

#  to  add some %  of image             #  alpha factor for image properties
#  alpha can be  o OR  1 
newimg=cv2.addWeighted(img1,0.8,img2,0.3,1)
newimg1=cv2.addWeighted(img1,0.8,img2,0.3,0)

cv2.imshow('windows',newimg)
cv2.imshow('windows22',newimg1)
cv2.waitKey(0)
cv2.destroyAllWindows()

