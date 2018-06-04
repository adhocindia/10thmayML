#!/usr/bin/python3
import  cv2
#  checking  height and width of current camera
'''
for i in dir(cv2):
	if  'FRAME' in i:
		print(i)
'''
#  starting with camera
cap=cv2.VideoCapture(0)

#  printing height and width of camera
#print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#  capturing  the frame width and height
width=cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

#  deciding video format              XVID for .avi format video
video_format=cv2.VideoWriter_fourcc(*'XVID')

#  saving video data as per format 
#                filename , video format , FPS , video w , h 
video_output=cv2.VideoWriter('adhoc.avi',video_format,50.0,(int(width),int(height)))
#  printing height and width of camera
#print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while cap.isOpened():
	status,frame=cap.read()
	cv2.imshow('live_frame',frame)
	video_output.write(frame)

	if cv2.waitKey(1) &  0xFF  ==  ord('q'):
		break


cv2.destroyAllWindows()
cap.release()






