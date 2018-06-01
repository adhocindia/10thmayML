import cv2

img=cv2.imread('dogs.jpg',0)
img1=cv2.imread('dogs.jpg',1)

cv2.imshow('show',img)
cv2.imshow('show11',img1)

cv2.waitKey(0)
cv2.destroyAllWindows()

