import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

if __name__=="__main__": 
	img2 = cv.imread('maze08.jpg',0	)
	ret2,thresh2 = cv.threshold(img2,100,255,cv.THRESH_BINARY)
	print(thresh2.shape)
	sum1 =100000
	li =[]
	x =600
	y = 600
	for i in range(10,100):
		for j in range(10,100):
			if(thresh2[j,i]==0 and j+i < sum1):
				x =j
				y =i
				sum1 = min(sum1,j+i)
	print(x,y)
	templi =[x,y]
	li.append(templi)
	

	x = 0
	
	for i in range(10,100):
		for j in range(300,500):
			if(thresh2[j,i]==0 and j > x):
				x =j
				y=i
	print(x,y)
	templi =[x,y]
	li.append(templi)
	y = 0
	
	for i in range(300,500):
		for j in range(10,100):
			if(thresh2[j,i]==0 and i>y):
				x =j
				y= i
	print(x,y)
	templi =[x,y]
	li.append(templi)
	sum1 =0
	x = 0
	y = 0  
	for i in range(300,500):
		for j in range(300,500):
			if(thresh2[j,i]==0 and j+i > sum1):
				x =j
				y =i
				sum1 = max(sum1,j+i)
	print(x,y)
	templi =[x,y]
	li.append(templi)
	print(li)
	x0 = li[0][0] 
	y0 = li[0][1] 
	x1 = li[1][0] 
	y1 = li[1][1] 
	x2 = li[2][0] 
	y2 = li[2][1] 
	x3 = li[3][0]
	y3 = li[3][1] 
    
	pts1 = np.float32([[x0,y0],[x1,y1],[x2,y2],[x3,y3]])
	pts2 = np.float32([[0,0],[510,0],[0,510],[510,510]])
	M = cv.getPerspectiveTransform(pts1,pts2)
	dst = cv.warpPerspective(img2,M,(510,510))
	cv.imshow('destination', dst) 
	
	cv.waitKey(0) 
	  
	    # close the window 
	cv.destroyAllWindows()  