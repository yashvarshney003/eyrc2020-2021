import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
def nothing():
	pass
img9 = cv.imread('maze09.jpg',0)
img8 = cv.imread('maze08.jpg',0)
img7 = cv.imread('maze07.jpg',0)
img6 = cv.imread('maze06.jpg',0)
img5 = cv.imread('maze05.jpg',0)
img4 = cv.imread('maze04.jpg',0)
img3 = cv.imread('maze03.jpg',0)
img2 = cv.imread('maze02.jpg',0)
img1 = cv.imread('maze01.jpg',0)
img0 = cv.imread('maze00.jpg',0)
cv.namedWindow('threshold')
cv.createTrackbar("Max", "threshold",0,255,nothing)
cv.createTrackbar("Min", "threshold",0,255,nothing)

while True:
	min1 = cv.getTrackbarPos("Min", "threshold")
	max1 = cv.getTrackbarPos("Max", "threshold")
	ret9,thresh9  = cv.threshold(img9,min1,max1,cv.THRESH_BINARY)
	ret8,thresh8 = cv.threshold(img8,min1,max1,cv.THRESH_BINARY)
	ret7,thresh7 = cv.threshold(img7,min1,max1,cv.THRESH_BINARY)
	ret6,thresh6 = cv.threshold(img6,min1,max1,cv.THRESH_BINARY)
	ret5,thresh5 = cv.threshold(img5,min1,max1,cv.THRESH_BINARY)
	ret4,thresh4 = cv.threshold(img4,min1,max1,cv.THRESH_BINARY)
	ret3,thresh3 = cv.threshold(img3,min1,max1,cv.THRESH_BINARY)
	ret2,thresh2 = cv.threshold(img2,min1,max1,cv.THRESH_BINARY)
	ret1,thresh1 = cv.threshold(img1,min1,max1,cv.THRESH_BINARY)
	ret0,thresh0 = cv.threshold(img0,min1,max1,cv.THRESH_BINARY)
	titles = ['img9','img8','img7','img6','img5','img4','img3','img2','img1','img0']
	images = [thresh9,thresh8,thresh7,thresh6,thresh5,thresh4,thresh3,thresh2,thresh1,thresh0]
	print("so this is the value",thresh1[100,200])

	for i in range(10):
		plt.subplot(5,2,i+1),plt.imshow(images[i],'gray')
		
    	

	plt.show()
	

 
   
 
 
	

