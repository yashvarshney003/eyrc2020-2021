'''
*****************************************************************************************
*
*        		===============================================
*           		Nirikshak Bot (NB) Theme (eYRC 2020-21)
*        		===============================================
*
*  This script is to implement Task 4A of Nirikshak Bot (NB) Theme (eYRC 2020-21).
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

# Team ID:			2139
# Author List: 		Anurag Saxena
# Filename:			task_4a.py
# Functions:		find_path, read_start_end_coordinates
# 					[ Comma separated list of functions in this file ]
# Global variables:	
# 					[ List of global variables defined in this file ]

####################### IMPORT MODULES #######################
## You are not allowed to make any changes in this section. ##
## You have to implement this task with the six available   ##
## modules for this task (numpy, opencv, os, traceback,     ##
## sys, json)												##
##############################################################
import numpy as np
import cv2
import os
import traceback
import sys
import json
import time


# Import 'task_1b.py' file as module
try:
	import task_1b

except ImportError:
	print('\n[ERROR] task_1b.py file is not present in the current directory.')
	print('Your current directory is: ', os.getcwd())
	print('Make sure task_1b.py is present in this current directory.\n')
	sys.exit()
		
except Exception as e:
	print('Your task_1b.py throwed an Exception, kindly debug your code!\n')
	traceback.print_exc(file=sys.stdout)
	sys.exit()

##############################################################


################# ADD UTILITY FUNCTIONS HERE #################
## You can define any utility functions for your code.      ##
## Please add proper comments to ensure that your code is   ##
## readable and easy to understand.                         ##
##############################################################





##############################################################


def find_path(maze_array, start_coord, end_coord):
	
	"""
	Purpose:
	---
	Takes a maze array as input and calculates the path between the
	start coordinates and end coordinates.

	Input Arguments:
	---
	`maze_array` :   [ nested list of lists ]
		encoded maze in the form of a 2D array

	`start_coord` : [ tuple ]
		start coordinates of the path

	`end_coord` : [ tuple ]
		end coordinates of the path
	
	Returns:
	---
	`path` :  [ list of tuples ]
		path between start and end coordinates
	
	Example call:
	---
	path = find_path(maze_array, start_coord, end_coord)
	"""

	path = []
	

	################# ADD YOUR CODE HERE #################

	children_list=[]	#list of all the possible cells on which ball can move from the current cell(current cell = parent cell of all moveable cells).
	prev_parent =(-1,-1)	#stores the parent of the current cell
	alternative =[]		#stores all those cells which are not selected OR alternative cells
	alternative_parent=[]	#stores all the alternative cells after 1 path is calculated.
	all_paths=[]	#stores all the possible paths.

	current_x_coord = start_coord[0]	#current cell x index
	current_y_coord = start_coord[1]	#current cell y index
	
	while(1):
		if ((current_x_coord==end_coord[0]) and current_y_coord==end_coord[1]): #if current cell is equal to end cell => path is calculated
			path.append((current_x_coord,current_y_coord))
			
			#******************************************
			all_paths.append(path[:])

			if (len(all_paths)==1):	#condition after the 1st path calculated
				alternative_parent = alternative

			if (len(alternative_parent)==0):
				break
			else:
				#pop from the alternative
				next_parent=alternative_parent.pop()
				alternative=[]	#after calculating 1st path clear the alternative list for the second path
				current_x_coord=next_parent[1]
				current_y_coord=next_parent[2]
				prev_parent=(next_parent[3],next_parent[4])
				#need to delete some elements of path here if selected path is closed to delete all the previous path cells untill the we get the altenative parent.
				try:
					position=path.index(prev_parent)
					while(len(path)>(position+1)):
						popped_element=path.pop()	#for printing and checking
						
				except ValueError:
					print("Vlauerror")
		
		#generating binary for each of the element 
		n = maze_array[current_x_coord][current_y_coord]			
		number = n		#for printing and checking
		binary =[]
		if(n==0):
			binary.append(0)
			binary.append(0)
			binary.append(0)
			binary.append(0)
		else:
			if(n==1):
				binary.append(0)
				binary.append(0)
				binary.append(0)
				binary.append(1)
			else:
				for b in range(4):
					if (n==1):
						binary.append(1)
						n=n-1
					elif (n==0):
						binary.append (0)
					else:
						if (n%2 == 1):
							binary.append(n%2)
							n=n-1
							n=n/2
						elif (n%2==0):
							binary.append(n%2)
							n=n/2
				binary.reverse()	#generated binary number
	#	print(number,"-->",binary)
		for l in range(0,4):
			bit = binary[l]
			if (bit==0): #means there is no wall
				if current_x_coord<9: #for south boyndary condition
					if l==0: #south block
						distance=((end_coord[0]-(current_x_coord+1))**2)+((end_coord[1]-(current_y_coord))**2) #distance of the block to the target in this step for priority by assuming current_x_coord,current_y_coord indexing as x,y co-ordinates
						children=(distance,current_x_coord+1,current_y_coord,current_x_coord,current_y_coord)	#(distance between the child block and target block(current_x_coord+1,current_y_coord),index of child block,index of parent block(current_x_coord,current_y_coord))
				if current_y_coord<9: #for east boundary condition
					if l==1: #east block
						distance=((end_coord[0]-(current_x_coord))**2)+((end_coord[1]-(current_y_coord+1))**2)
						children=(distance,current_x_coord,current_y_coord+1,current_x_coord,current_y_coord)
				if current_x_coord>0: #for north boundary condition
					if l==2: #north block
						distance=((end_coord[0]-(current_x_coord-1))**2)+((end_coord[1]-(current_y_coord))**2)
						children=(distance,current_x_coord-1,current_y_coord,current_x_coord,current_y_coord)
				if current_y_coord>0: #for south boundary condition
					if l==3: #south block
						distance=((end_coord[0]-(current_x_coord))**2)+((end_coord[1]-(current_y_coord-1))**2)
						children=(distance,current_x_coord,current_y_coord-1,current_x_coord,current_y_coord)
				#************************************************************************
				if ((children[1]!=prev_parent[0]) or (children[2]!=prev_parent[1])): #if children is not the previous parent then append the children
					children_list.append(children)
		children_list.sort(reverse = True)		#sorting the list in children cells accordig to the distance between cells and last cell.
		prev_parent =(current_x_coord,current_y_coord)

		try:
			repeat = -1
			repeat = path.index(prev_parent)
			if (repeat >= 0):
				break
		except:
			pass

		path.append(prev_parent)
		if(len(children_list)>0):
			next_parent = children_list.pop()	#selecting the children with priority.
			current_x_coord = next_parent[1]
			current_y_coord = next_parent[2]
			if(len(children_list)>0):
				for a in range(0,len(children_list)):
					alternative.append(children_list[a])	# all other children cells stored in the alternative list
				children_list= []		#clearing children_list for next iteration
		else:
			#Path does not exist case {if all_paths & alternative both the lists are empty then path does not exist}
			if ((len(all_paths) ==0) and (len(alternative)==0)):
				print(f" Path between start_coord :{start_coord} and end_coord: {end_coord} for this maze does not exist.")
				path = None
				break

			#if alternative list is not empty, pop from the alternative to select new cell.
			if (len(alternative)!=0):
				next_parent=alternative.pop()
				current_x_coord=next_parent[1]
				current_y_coord=next_parent[2]
				prev_parent=(next_parent[3],next_parent[4])
				#need to delete some elements of path here, deleting all the wrong cells untill the we get the altenative parent.
				try:
					position=path.index(prev_parent)
					while(len(path)>(position+1)):
						popped_element=path.pop()
						#print("popped_element =",popped_element)
				except ValueError:
					print("Vlauerror")
					

			else:
				#pop from the alternative_parent list to select new cell, if alternative list is empty
				if (len(alternative_parent)!=0):
					next_parent=alternative_parent.pop()
					alternative=[]	#after calculating 1st path clear the alternative list for the second path
					current_x_coord=next_parent[1]
					current_y_coord=next_parent[2]
					prev_parent=(next_parent[3],next_parent[4])
					#need to delete some elements of path here to delete all the previous path cells untill the we get the altenative parent.
					try:
						position=path.index(prev_parent)
						while(len(path)>(position+1)):
							popped_element=path.pop()
						
					except ValueError:
						print(f"prev_parent {prev_parent} is not present in the path list.")
				else:	#break the loop if alternative and alternative_parent both lists are empty but all_paths list is non-empty
					break
	if (len(all_paths)!=0):
		all_paths.sort(key=len,reverse=True)	#sorting list accordig to length of the lists inside it
		
		while(True):
			continuity_flag = True	# to check if generated path has continuity means only x and y is changing at a time with difference of 1.
			path = all_paths.pop()
			if (len(path)==len(set(path))):		#checking there should not be duplicate element in the list
				for i in range(0,(len(path)-2)):	#checking the continuity of the elements in the list "there should be difference of 1 in x or y of the successive element"
					if ( ((path[i][0]==path[i+1][0])and( abs(path[i][1]-path[i+1][1])==1 ))  or  ((abs(path[i][0]-path[i+1][0])==1)and(path[i][1]==path[i+1][1])) ):
						pass
					else:
						continuity_flag = False
				if (continuity_flag == True):
					break
	

		





		

	######################################################
	shortest_path=[]	#stores the shortest path after removing all the un-necessary elements in a straight path
	shortest_path.append(path[0])
	i=0
	while(i<(len(path)-2)):
		if (shortest_path[len(shortest_path)-1][0]==path[i+1][0]):
			while((shortest_path[len(shortest_path)-1][0]==path[i+1][0]) and (i<(len(path)-2))):
				i=i+1
			shortest_path.append(path[i])
		if (shortest_path[len(shortest_path)-1][1]==path[i+1][1]):
			while((shortest_path[len(shortest_path)-1][1]==path[i+1][1]) and (i<(len(path)-2))):
				i=i+1
			shortest_path.append(path[i])
	shortest_path.append(path[len(path)-1])
	print("shortest_path =",shortest_path)
	
	
	return shortest_path


def read_start_end_coordinates(file_name, maze_name):
	"""
	Purpose:
	---
	Reads the corresponding start and end coordinates for each maze image
	from the specified JSON file
	
	Input Arguments:
	---
	`file_name` :   [ str ]
		name of JSON file

	`maze_name` : [ str ]
		specify the maze image for which the start and end coordinates are to be returned.

	Returns:
	---
	`start_coord` : [ tuple ]
		start coordinates for the maze image

	`end_coord` : [ tuple ]
		end coordinates for the maze image
	
	Example call:
	---
	start, end = read_start_end_coordinates("start_end_coordinates.json", "maze00")
	"""

	start_coord = None
	end_coord = None


	################# ADD YOUR CODE HERE #################
	with open(file_name) as file:
		data = json.load(file)
	start_coord = (data[maze_name]["start_coord"][0],data[maze_name]["start_coord"][1])
	end_coord = (data[maze_name]["end_coord"][0],data[maze_name]["end_coord"][1])
	
		
	######################################################

	return start_coord, end_coord


# NOTE:	YOU ARE NOT ALLOWED TO MAKE ANY CHANGE TO THIS FUNCTION
# 
# Function Name:    main
#        Inputs:    None
#       Outputs:    None
#       Purpose:    This part of the code is only for testing your solution. The function first takes 'maze00.jpg'
# 					as input and reads the corresponding start and end coordinates for this image from 'start_end_coordinates.json'
# 					file by calling read_start_end_coordinates function. It then applies Perspective Transform
# 					by calling applyPerspectiveTransform function, encodes the maze input in form of 2D array
# 					by calling detectMaze function and finds the path between start, end coordinates by calling
# 					find_path function. It then asks the user whether to repeat the same on all maze images
# 					present in 'test_cases' folder or not. Write your solution ONLY in the space provided in the above
# 					read_start_end_coordinates and find_path functions.
if __name__ == "__main__":

	# path directory of images in 'test_cases' folder
	img_dir_path = 'test_cases/'

	file_num = 0

	maze_name = 'maze0' + str(file_num)

	# path to 'maze00.jpg' image file
	img_file_path = img_dir_path + maze_name + '.jpg'

	# read start and end coordinates from json file
	start_coord, end_coord = read_start_end_coordinates("start_end_coordinates.json", maze_name)

	print('\n============================================')
	print('\nFor maze0' + str(file_num) + '.jpg')
	
	# read the 'maze00.jpg' image file
	input_img = cv2.imread(img_file_path)

	# get the resultant warped maze image after applying Perspective Transform
	warped_img = task_1b.applyPerspectiveTransform(input_img)

	if type(warped_img) is np.ndarray:

		# get the encoded maze in the form of a 2D array
		maze_array = task_1b.detectMaze(warped_img)

		if (type(maze_array) is list) and (len(maze_array) == 10):

			print('\nEncoded Maze Array = %s' % (maze_array))
			print('\n============================================')

			path = find_path(maze_array, start_coord, end_coord)

			if (type(path) is list):

				print('\nPath calculated between %s and %s is %s' % (start_coord, end_coord, path))
				print('\n============================================')

			else:
				print('\n Path does not exist between %s and %s' %(start_coord, end_coord))
		
		else:
			print('\n[ERROR] maze_array returned by detectMaze function is not complete. Check the function in code.\n')
			exit()
	
	else:
		print('\n[ERROR] applyPerspectiveTransform function is not returning the warped maze image in expected format! Check the function in code.\n')
		exit()
	
	choice = input('\nDo you want to run your script on all maze images ? => "y" or "n": ')

	if choice == 'y':

		for file_num in range(1,10):

			maze_name = 'maze0' + str(file_num)

			img_file_path = img_dir_path + maze_name + '.jpg'

			# read start and end coordinates from json file
			start_coord, end_coord = read_start_end_coordinates("start_end_coordinates.json", maze_name)

			print('\n============================================')
			print('\nFor maze0' + str(file_num) + '.jpg')
	
			# read the 'maze00.jpg' image file
			input_img = cv2.imread(img_file_path)

			# get the resultant warped maze image after applying Perspective Transform
			warped_img = task_1b.applyPerspectiveTransform(input_img)

			if type(warped_img) is np.ndarray:

				# get the encoded maze in the form of a 2D array
				maze_array = task_1b.detectMaze(warped_img)

				if (type(maze_array) is list) and (len(maze_array) == 10):

					print('\nEncoded Maze Array = %s' % (maze_array))
					print('\n============================================')

					path = find_path(maze_array, start_coord, end_coord)

					if (type(path) is list):

						print('\nPath calculated between %s and %s is %s' % (start_coord, end_coord, path))
						print('\n============================================')

					else:
						print('\n Path does not exist between %s and %s' %(start_coord, end_coord))

				else:
					print('\n[ERROR] maze_array returned by detectMaze function is not complete. Check the function in code.\n')
					exit()

			else:				
				print('\n[ERROR] applyPerspectiveTransform function is not returning the warped maze image in expected format! Check the function in code.\n')
				exit()
	
	else:
		print()

