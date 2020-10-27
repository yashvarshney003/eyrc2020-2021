import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import imutils
from skimage.filters import threshold_local
def make_border(img):
	
  
# Using cv2.copyMakeBorder() method 
	image = cv.copyMakeBorder(img, 10,10,10,10, cv.BORDER_CONSTANT,value=[0,0,0]) 
	cv.imshow("borde",image)
	cv.imwrite("getPerspectiveTransformbinaryborder.jpg",image)
	return image
if __name__ == '__main__':
	thresh2 = cv.imread("getperspectivetransformbinary.jpg")
	
	thresh2 = make_border(thresh2)
	thresh1 = thresh2
	cv.imshow("thresh2",thresh2)
	kernel = np.ones((5,5),np.uint8)
	erosion = cv.erode(thresh2,kernel,iterations = 1)
	cv.imwrite("getPerspectiveTransformbinaryborderirosion.jpg",erosion)
	cv.imshow("erosion",erosion)
	
	cv.imshow("dddddd",thresh1)
	edged = cv.Canny(thresh2, 75, 200)
	
	#cv.imshow("dddddd",thresh2)
	y = 50

	label = 0 
	
	for i in range(0,erosion.size[0],40):
		if(label==0):
			label+=1
			img_temp = erosion[5:50,10:i+40]
			cv.imshow("ddcccc",img_temp)
			cv.imshow("dddddd",erosion)
		else:
			img_temp = thresh2[5:50,i:i+40]
			cv.imshow("ddcccc",img_temp)
			cv.imshow("dddddd",erosion)
	
		cv.waitKey(10000//2)
		cv.destroyAllWindows()
			


	cv.imshow("ddcccc",edged)
	
	cv.waitKey(0)
	cv.destroyAllWindows()