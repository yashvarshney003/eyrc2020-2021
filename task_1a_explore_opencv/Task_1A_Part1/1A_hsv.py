import cv2
import numpy as np 
from matplotlib import pyplot as plt
import math
#import time

image = cv2.imread("Sample1.png")
sub_image = image[200: 900, 0:800]

hsv = cv2.cvtColor(sub_image, cv2.COLOR_BGR2HSV)
#cv2.rectangle(image, pt1=(0,200), pt2=(800,900), color=(0,255), thickness=10)
print(hsv[400,600])
upper_red = np.array([0, 255, 255])
for x in range(0,256):
	for y in range(0,256):
		for z in range(0,256):
			lower_red = np.array([x, y, z])
			mask = cv2.inRange(hsv,lower_red,upper_red)
			contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
			for contours in contours:
				area = cv2.contourArea(contours)
				if (abs(284410.0-area)<2840):
					error=(abs(area-284410)*100)/284410
					temp_img=hsv
					print("**********************")
					print("HSV_values=",x,y,z)
					print("area=",area)
					print("error=",error)
					print("**********************")
					'''
					cv2.drawContours(hsv, contours, -1, (0, 255, 0), 3)
					cv2.imshow("subimage",hsv)
					cv2.waitKey(20)
					cv2.destroyAllWindows()
					'''
	print("~~~~~~~~~~~~~~~")

#cv2.rectangle(image, pt1=(399,599), pt2=(400,600), color=(0,255), thickness=10)
#cv2.imshow("hsv",image)
#cv2.waitKey(0)
#cv2.destroyAllWindows()