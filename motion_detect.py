#!/usr/bin/python3

import  cv2

#  function  to create image  diff

#   here x , y ,z  are 3  image frames 
def   create_image_diff(x,y,z):
	img1_df=cv2.absdiff(x,y)	
	img2_df=cv2.absdiff(y,z)	
	img3=cv2.bitwise_and(img1_df,img2_df)
	return img3

#  starting web cam
cap=cv2.VideoCapture(0)
tp1=cap.read()[1]
tp2=cap.read()[1]
tp3=cap.read()[1]

#  coverting to grayscale
gray1=cv2.cvtColor(tp1,cv2.COLOR_BGR2GRAY)
gray2=cv2.cvtColor(tp2,cv2.COLOR_BGR2GRAY)
gray3=cv2.cvtColor(tp3,cv2.COLOR_BGR2GRAY)

while True:
	# calling function
	new_img=create_image_diff(gray1,gray2,gray3)
	cv2.imshow('wind1',new_img)
	#  capture new image
	statu,frame=cap.read()
	cv2.imshow('original',frame)
	#  exachange image
	gray1=gray2
	gray2=gray3
	gray3=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)


	if cv2.waitKey(1)  &  0xFF == ord('q'):
		break

cv2.destroyAllWindows()
cap.release()


