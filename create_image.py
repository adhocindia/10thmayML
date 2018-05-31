#!/usr/bin/python3
#  loading  opencv module 
import  cv2
#  to create blank image 
import numpy  as  np

#  creating  zero matrix arrays that is black  0  
img=np.zeros((512,512,3))

'''
print(img)
print(img.shape)

'''
cv2.line(img,(0,0),(100,120),(255,0,0),3)
# display 
cv2.imshow('myownimage',img)
cv2.waitKey(0)
#  to destroy one named window
#cv2.destroyWindows('myownimage')
cv2.destroyAllWindows()

