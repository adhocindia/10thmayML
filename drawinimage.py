#!/usr/bin/python3
#  loading  opencv module 
import  cv2
#  to create blank image 
img=cv2.imread('/home/do/Desktop/dog1.jpg',1)
#  print shape
print(img.shape)
# to draw  a line into the image
#        image , start,end, color, width
cv2.line(img,(0,0),(150,200),(120,140,20),6)
#  to draw a rectange 
cv2.rectangle(img,(20,50),(500,700),(0,255,0),2)
#  circle 
cv2.circle(img,(146,250),100,(255,0,0),-1)

#   polygon, eclipse , text 

# display 
cv2.imwrite('newdog.jpg',img)
cv2.imshow('myownimage',img)
cv2.waitKey(0)
#  to destroy one named window
#cv2.destroyWindows('myownimage')
cv2.destroyAllWindows()





