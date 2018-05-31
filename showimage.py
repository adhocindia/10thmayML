#!/usr/bin/python3
#  loading  opencv module 
import  cv2
#  to create blank image 
img=cv2.imread('/home/do/Desktop/dog1.jpg',1)
# display 
cv2.imshow('myownimage',img)
cv2.waitKey(0)
#  to destroy one named window
#cv2.destroyWindows('myownimage')
cv2.destroyAllWindows()

