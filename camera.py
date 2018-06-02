#!/usr/bin/python3
import cv2
#  loading  camera
#  0 means  first  web cam , 1 means second and so on...
cam=cv2.VideoCapture(0)
#  checking for detection 
while  cam.isOpened() :
	print("working ...")
        #   real data of captured image stored in frame  
	#  processing and open status  of camera stored in status
	status,frame=cam.read()
	newimg=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	cv2.imshow('camera0',frame)
	cv2.imshow('camera2',frame)
	cv2.imshow('camera1',newimg)
	cv2.imshow('camera3',newimg)
			
	if  cv2.waitKey(1)  &  0xFF ==  ord('q')  :
		break
	
cv2.destroyAllWindows()
cam.release()







