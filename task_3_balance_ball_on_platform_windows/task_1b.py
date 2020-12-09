'''
*****************************************************************************************
*
*        		===============================================
*           		Nirikshak Bot (NB) Theme (eYRC 2020-21)
*        		===============================================
*
*  This script is to implement Task 1B of Nirikshak Bot (NB) Theme (eYRC 2020-21).
*  
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*  
*  e-Yantra - An MHRD project under National Mission on Education using ICT (NMEICT)
*
*****************************************************************************************
'''

# Team ID:			[2139]
# Author List:		[Yash Varshney]
# Filename:			task_1b.py
# Functions:		applyPerspectiveTransform, detectMaze, writeToCsv
# 					[ Comma separated list of functions in this file ]
# Global variables:	
# 					[ List of global variables defined in this file ]


####################### IMPORT MODULES #######################
## You are not allowed to make any changes in this section. ##
## You have to implement this task with the three available ##
## modules for this task (numpy, opencv, csv)               ##
##############################################################
import numpy as np
import cv2 as cv
import csv
##############################################################


################# ADD UTILITY FUNCTIONS HERE #################
## You can define any utility functions for your code.      ##
## Please add proper comments to ensure that your code is   ##
## readable and easy to understand.                         ##
##############################################################






##############################################################


def applyPerspectiveTransform(input_img):

	"""
	Purpose:
	---
	takes a maze test case image as input and applies a Perspective Transfrom on it to isolate the maze

	Input Arguments:
	---
	`input_img` :   [ numpy array ]
		maze image in the form of a numpy array
	
	Returns:
	---
	`warped_img` :  [ numpy array ]
		resultant warped maze image after applying Perspective Transform
	
	Example call:
	---
	warped_img = applyPerspectiveTransform(input_img)
	"""

	warped_img = None

	##############	ADD YOUR CODE HERE	##############
	#Conversion into GrayScale
	

	ret,thresh1 = cv.threshold(input_img,230,255,cv.THRESH_BINARY_INV)
	#Applying Canny Edge Detection
	edged = cv.Canny(thresh1, 50, 200)
	

					



	#Finding Contours 
	cnts = cv.findContours(edged.copy(), cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)[0]
		


	#Sorting the Contours in decreasing order because Square containing the Maze is largest
	cnts = sorted(cnts, key = cv.contourArea, reverse = True)

	#Looping through the Contours and approxing Contours
	for c in cnts:
		peri = cv.arcLength(c, True)
		approx = cv.approxPolyDP(c, 0.05 * peri, True)
		#0.02
		
	# If length is 4 then it is ROI
		if len(approx) == 4:
			screenCnt = approx
			break

	# Reshaping Contours for further use
	pts = screenCnt.reshape(4, 2)

	#creating Array of Zero of Size(4,2)	
	rect = np.zeros((4, 2), dtype = "float32")

	#Ordering of points in Clockwise manner

	s = pts.sum(axis = 1)
	rect[0] = pts[np.argmin(s)]
	rect[2] = pts[np.argmax(s)]

	diff = np.diff(pts, axis = 1)
	rect[1] = pts[np.argmin(diff)]
	rect[3] = pts[np.argmax(diff)]
	(tl, tr, br, bl) = rect


	#Finding Maximum width

	
	maxWidth = 1280



	#Findinf Maximum height

	
	maxHeight = 1280

	#Destination Array of ROI
	

	dst = np.array([[0, 0],[maxWidth - 1, 0],[maxWidth - 1, maxHeight - 1],[0, maxHeight - 1]], dtype = "float32")


	#Applying perspective transform
	M = cv.getPerspectiveTransform(rect, dst)

	# Finally the warped image 
	warped_img = cv.warpPerspective(input_img, M, (maxWidth, maxHeight))
	#cv.imshow("window_name", warped_img) 
  
#waits for user to press any key  
#(this is necessary to avoid Python kernel form crashing) 
	#cv.waitKey(0)  
  
#closing all open windows  
	#cv.destroyAllWindows() 
	
	
	

	##################################################

	return warped_img


def detectMaze(warped_img):

	"""
	Purpose:
	---
	takes the warped maze image as input and returns the maze encoded in form of a 2D array

	Input Arguments:
	---
	`warped_img` :    [ numpy array ]
		resultant warped maze image after applying Perspective Transform
	
	Returns:
	---
	`maze_array` :    [ nested list of lists ]
		encoded maze in the form of a 2D array

	Example call:
	---
	maze_array = detectMaze(warped_img)
	"""

	maze_array = []

	##############	ADD YOUR CODE HERE	##############

	#Converting into grayscale
	warped_img_gray = cv.cvtColor(warped_img, cv.COLOR_BGR2GRAY)
	#Applying Gaussian Blur
	warped_img_gray = cv.GaussianBlur(warped_img_gray,(5,5),0)

	#Some part is washed out by perpective transform to make uniform border in all direction 
	thresh = cv.copyMakeBorder(warped_img_gray,5,5,5,5, cv.BORDER_CONSTANT,value=[0,0,0]) 

	#Converting into binary(Pixel value 0 and 255 only)
	thresh = cv.threshold(thresh,135,255,cv.THRESH_BINARY)[1]

	# Resizing the image into (400,400) to make uniform
	resized_image = cv.resize(thresh, (400, 400)) 
	#Assumption that Each Block will be now (40,40)

	jincrement = resized_image.shape[0]//10
	iincrement = resized_image.shape[1]//10
	
	#Inverting the Image for ease of calculation
	ret2,resized_image = cv.threshold(resized_image,100,255,cv.THRESH_BINARY_INV)

	#Looping through the Maze block by block
	
	for i in range(0,resized_image.shape[0],iincrement):
		
		maze_array.append([])
		if(i==0):
			y = i
			iiicrement = 44
		else:
			y = i-1
			iiicrement = 43
		for j in range(0,resized_image.shape[1],jincrement):
				
				if(j==0):
					
					img_temp = resized_image[y:y+iiicrement,j:j+44]
				else:
					img_temp = resized_image[y:y+iiicrement,j-5:j+44]
					
				value = 0

				#Finding the center of block Image
				x_center = img_temp.shape[1]//2
				y_center = img_temp.shape[0]//2
				
				
				#Now from center moving in all direction if pixel value comes out as specied then there is Grid otherwise not.
				dir = 0
				while(y_center - dir >= 0):
					if(img_temp[y_center-dir, x_center] == 255):
						
						value += 2
						break
					dir +=1
					
					
				dir = 0
				while(y_center + dir  < img_temp.shape[0]):
					if(img_temp[y_center+dir,x_center] == 255):
						value += 8
						
						break
					dir+=1
					
					
				dir = 0
				while(x_center + dir <  img_temp.shape[1] ):
					if(img_temp[y_center,x_center+dir] == 255  or img_temp[15,x_center+dir]):
						value += 4
						break
					dir+=1
					
				dir =0
				while(x_center-dir >= 0):
					if(img_temp[y_center,x_center-dir] == 255):
								value  +=1
								break
					dir +=1
				
				

				


				


			#Final Encoded maze array
				maze_array[i//40].append(value)
##################################################

	return maze_array


# NOTE:	YOU ARE NOT ALLOWED TO MAKE ANY CHANGE TO THIS FUNCTION
def writeToCsv(csv_file_path, maze_array):

	"""
	Purpose:
	---
	takes the encoded maze array and csv file name as input and writes the encoded maze array to the csv file

	Input Arguments:
	---
	`csv_file_path` :	[ str ]
		file path with name for csv file to write
	
	`maze_array` :		[ nested list of lists ]
		encoded maze in the form of a 2D array
	
	Example call:
	---
	warped_img = writeToCsv('test_cases/maze00.csv', maze_array)
	"""

	with open(csv_file_path, 'w', newline='') as file:
		writer = csv.writer(file)
		writer.writerows(maze_array)


# NOTE:	YOU ARE NOT ALLOWED TO MAKE ANY CHANGE TO THIS FUNCTION
# 
# Function Name:    main
#        Inputs:    None
#       Outputs:    None
#       Purpose:    This part of the code is only for testing your solution. The function first takes 'maze00.jpg'
# 					as input, applies Perspective Transform by calling applyPerspectiveTransform function,
# 					encodes the maze input in form of 2D array by calling detectMaze function and writes this data to csv file
# 					by calling writeToCsv function, it then asks the user whether to repeat the same on all maze images
# 					present in 'test_cases' folder or not. Write your solution ONLY in the space provided in the above
# 					applyPerspectiveTransform and detectMaze functions.

if __name__ == "__main__":

	# path directory of images in 'test_cases' folder
	img_dir_path = 'test_cases/'

	# path to 'maze00.jpg' image file
	file_num = 0
	img_file_path = img_dir_path + 'maze0' + str(file_num) + '.jpg'

	print('\n============================================')
	print('\nFor maze0' + str(file_num) + '.jpg')

	# path for 'maze00.csv' output file
	csv_file_path = img_dir_path + 'maze0' + str(file_num) + '.csv'
	
	# read the 'maze00.jpg' image file
	input_img = cv.imread(img_file_path)

	# get the resultant warped maze image after applying Perspective Transform
	warped_img = applyPerspectiveTransform(input_img)

	if type(warped_img) is np.ndarray:

		# get the encoded maze in the form of a 2D array
		maze_array = detectMaze(warped_img)

		if (type(maze_array) is list) and (len(maze_array) == 10):

			print('\nEncoded Maze Array = %s' % (maze_array))
			print('\n============================================')
			
			# writes the encoded maze array to the csv file
			writeToCsv(csv_file_path, maze_array)

			cv.imshow('warped_img_0' + str(file_num), warped_img)
			cv.waitKey(0)
			cv.destroyAllWindows()
		
		else:

			print('\n[ERROR] maze_array returned by detectMaze function is not complete. Check the function in code.\n')
			exit()
	
	else:

		print('\n[ERROR] applyPerspectiveTransform function is not returning the warped maze image in expected format! Check the function in code.\n')
		exit()
	
	choice = input('\nDo you want to run your script on all maze images ? => "y" or "n": ')

	if choice == 'y':

		for file_num in range(1, 10):
			
			# path to image file
			img_file_path = img_dir_path + 'maze0' + str(file_num) + '.jpg'

			print('\n============================================')
			print('\nFor maze0' + str(file_num) + '.jpg')

			# path for csv output file
			csv_file_path = img_dir_path + 'maze0' + str(file_num) + '.csv'
			
			# read the image file
			input_img = cv.imread(img_file_path)

			# get the resultant warped maze image after applying Perspective Transform
			warped_img = applyPerspectiveTransform(input_img)

			if type(warped_img) is np.ndarray:

				# get the encoded maze in the form of a 2D array
				maze_array = detectMaze(warped_img)

				if (type(maze_array) is list) and (len(maze_array) == 10):

					print('\nEncoded Maze Array = %s' % (maze_array))
					print('\n============================================')
					
					# writes the encoded maze array to the csv file
					writeToCsv(csv_file_path, maze_array)

					cv.imshow('warped_img_0' + str(file_num), warped_img)
					cv.waitKey(0)
					cv.destroyAllWindows()
				
				else:

					print('\n[ERROR] maze_array returned by detectMaze function is not complete. Check the function in code.\n')
					exit()
			
			else:

				print('\n[ERROR] applyPerspectiveTransform function is not returning the warped maze image in expected format! Check the function in code.\n')
				exit()

	else:

		print('')

