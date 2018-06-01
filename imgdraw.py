#!/usr/bin/python3

import cv2,time
import numpy  as np
import matplotlib.pyplot as plt
# reading images 
img=cv2.imread('dogs.jpg',cv2.IMREAD_COLOR)
#img=np.zeros((512,512,3),np.uint8)
#img=img[0:100,0:200]
print(img.shape)
time.sleep(1)
cv2.line(img,(10,20),(200,200),(255,0,0),5)
cv2.rectangle(img,(150,150),(350,350),(20,30,200),2)
cv2.circle(img,(400,200),100,(220,130,200),-1)
cv2.circle(img,(400,200),100,(220,130,200),-1)
font=cv2.FONT_HERSHEY_SIMPLEX
#                         start_point,font,font_size
cv2.putText(img,'GOOGLE',(10,150),font,3,(0,0,255),10,cv2.LINE_AA)
cv2.imshow('draw',img)
k=cv2.waitKey(0)
if k == 27 :  #  for esc button 
    cv2.destroyAllWindows()
elif k == ord('s') :
    cv2.imwrite('save.jpg',img1)
    cv2.destroyAllWindows()



