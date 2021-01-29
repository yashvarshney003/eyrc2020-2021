'''
*****************************************************************************************
*
*        		===============================================
*           		Nirikshak Bot (NB) Theme (eYRC 2020-21)
*        		===============================================
*
*  This script is to implement Task 5 of Nirikshak Bot (NB) Theme (eYRC 2020-21).
*  
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*  
*  e-Yantra - An MHRD (now MOE) project under National Mission on Education using ICT (NMEICT)
*
*****************************************************************************************
'''

# Team ID:          2139
# Author List:     Yash Varshney, Aman Tyagi
# Filename:         task_5.py
# Functions:        
#                   [ Comma separated list of functions in this file ]
# Global variables: 
# 					[ List of global variables defined in this file ]

# NOTE: Make sure you do NOT call sys.exit() in this code.

####################### IMPORT MODULES #######################
## You are not allowed to make any changes in this section. ##
##############################################################
import numpy as np
import cv2
import os, sys
import traceback
import time
import math
import json
##############################################################

# Importing the sim module for Remote API connection with 
try:
	import sim
	
except Exception:
	print('\n[ERROR] It seems the sim.py OR simConst.py files are not found!')
	print('\n[WARNING] Make sure to have following files in the directory:')
	print('sim.py, simConst.py and appropriate library - remoteApi.dll (if on Windows), remoteApi.so (if on Linux) or remoteApi.dylib (if on Mac).\n')
	

#Import 'task_1b.py' file as module
try:
	import task_1b

except ImportError:
	print('\n[ERROR] task_1b.py file is not present in the current directory.')
	print('Your current directory is: ', os.getcwd())
	print('Make sure task_1b.py is present in this current directory.\n')
	
	
except Exception as e:
	print('Your task_1b.py throwed an Exception. Kindly debug your code!\n')
	traceback.print_exc(file=sys.stdout)
	


# Import 'task_1a_part1.py' file as module
try:
	import task_1a_part1

except ImportError:
	print('\n[ERROR] task_1a_part1.py file is not present in the current directory.')
	print('Your current directory is: ', os.getcwd())
	print('Make sure task_1a_part1.py is present in this current directory.\n')
	
	
except Exception as e:
	print('Your task_1a_part1.py throwed an Exception. Kindly debug your code!\n')
	traceback.print_exc(file=sys.stdout)
	


# Import 'task_2a.py' file as module
try:
	import task_2a

except ImportError:
	print('\n[ERROR] task_2a.py file is not present in the current directory.')
	print('Your current directory is: ', os.getcwd())
	print('Make sure task_2a.py is present in this current directory.\n')
	
	
except Exception as e:
	print('Your task_2a.py throwed an Exception. Kindly debug your code!\n')
	traceback.print_exc(file=sys.stdout)
	

# Import 'task_2b.py' file as module
try:
	import task_2b

except ImportError:
	print('\n[ERROR] task_2b.py file is not present in the current directory.')
	print('Your current directory is: ', os.getcwd())
	print('Make sure task_2b.py is present in this current directory.\n')
	
	
except Exception as e:
	print('Your task_2b.py throwed an Exception. Kindly debug your code!\n')
	traceback.print_exc(file=sys.stdout)
	

# Import 'task_3.py' file as module
try:
	import task_3

except ImportError:
	print('\n[ERROR] task_3.py file is not present in the current directory.')
	print('Your current directory is: ', os.getcwd())
	print('Make sure task_3.py is present in this current directory.\n')
	

except Exception as e:
	print('Your task_3.py throwed an Exception. Kindly debug your code!\n')
	traceback.print_exc(file=sys.stdout)
	


# Import 'task_4a.py' file as module
try:
	import task_4a

except ImportError:
	print('\n[ERROR] task_4a.py file is not present in the current directory.')
	print('Your current directory is: ', os.getcwd())
	print('Make sure task_4a.py is present in this current directory.\n')

try:
	with open('ball_details.json') as file:
		ball_details = json.load(file)

except ImportError:
	print('\n[ERROR] ball_details.json file is not present in the current directory.')
	print('Your current directory is: ', os.getcwd())
	print('Make sure ball_details.json is present in this current directory.\n')
	
	
except Exception as e:
	print('Your task_4a.py throwed an Exception. Kindly debug your code!\n')
	traceback.print_exc(file=sys.stdout)

########################Global variables######################
vision_sensor_1 = -1
vision_sensor_2 = -1
vision_sensor_3 = -1
vision_sensor_4 = -1
vision_sensor_5 = -1
encoded_maze_t4 = None
encoded_maze_t1 = None
encoded_maze_t3 = None
encoded_maze_t2 = None

map_start = {
	"T4":[(0,5)],
	"T3":[(4,9)],
	"T2":[(0,4)],
	"T1":[(5,0)]
	}# do mapping of start and end point on the basis of color and json file.

map_end = {
"T4":[(5,9), (9,4), (4,0)],
"T3":[(9,5), (5,0), (0,4)],
"T2":[(4,9), (9,5), (5,0)],
"T1":[(0,4), (4,9), (9,5)]
} 

t4_path = None#path to table req
aux_path = None#path to req cb

path_map = {#pixel path
"T1":[],
"T2":[],
"T3":[],
"T4":[]
}

maze_map ={
	'T4':encoded_maze_t4,
	'T1':encoded_maze_t1,
	'T2':encoded_maze_t2,
	'T3':encoded_maze_t3
}

client_id = -1
############################################################
##############################################################


# NOTE:	YOU ARE NOT ALLOWED TO MAKE ANY CHANGE TO THIS FUNCTION
# 
# Function Name:    send_color_and_collection_box_identified
#        Inputs:    ball_color and collection_box_name
#       Outputs:    None
#       Purpose:    1. This function should only be called when the task is being evaluated using
# 					   test executable.
#					2. The format to send the data is as follows:
#					   'color::collection_box_name'				   
def send_color_and_collection_box_identified(ball_color, collection_box_name):

	global client_id

	color_and_cb = ball_color + '::' + collection_box_name
	inputBuffer = bytearray()
	return_code, retInts, retFloats, retStrings, retBuffer = sim.simxCallScriptFunction(client_id,'evaluation_screen_respondable_1',
							sim.sim_scripttype_childscript,'color_and_cb_identification',[],[],color_and_cb,inputBuffer,sim.simx_opmode_blocking)

################# ADD UTILITY FUNCTIONS HERE #################
## You can define any utility functions for your code.      ##
## Please add proper comments to ensure that your code is   ##
## readable and easy to understand.                         ##
##############################################################
def set_path(color):
	table, collection_box = ball_details[color][0].split('_')
	# path_start = map_start[table]
	# path_end = map_end[table][int(collection_box[-1])-1]
	t4_path=path_map['T4'][int(table[-1])-1]
	aux_path = path_map[table][int(collection_box[-1])-1]
	###
	#Traverese the ball now 
	###
	ball_details[color].pop(0)

#set oath according to pixel
def complete_all_mapping_path (tablenum):#, start_coord, end_coord):
	global map_start,map_end,maze_map,path_map
	for i in range(3):
		start_coord= map_start[tablenum][0]
		end_coord= map_end[tablenum][i]
		mazearray = maze_map[tablenum]
		path = task_4a.find_path(mazearray, start_coord, end_coord)	
		resolution_x = 1280
		resolution_y = 1280
		x_increment = resolution_x//10
		y_increment = resolution_y//10
		pixel_path = []
		for i in range(len(path)):
			pixel_path.append([])

		for i in range(len(path)):
			x_pixel = (x_increment//2) + path[i][0]*x_increment
			y_pixel = (y_increment//2) + path[i][1]*y_increment
			pixel_path[i].append(x_pixel)
			pixel_path[i].append(y_pixel)
		path_map[tablenum][i]= pixel_path

	
def get_color():
	global vision_sensor_5,client_id
	return_code ,image_resolution,vision_sensor_image =sim.simxGetVisionSensorImage(client_id,vision_sensor_handle_5,1,sim.simx_opmode_blocking)
	print(f"length {len(vision_sensor_image)} and  {return_code}")
	
	
	return_code ,image_resolution,vision_sensor_image =sim.simxGetVisionSensorImage(client_id,vision_sensor_handle,1,sim.simx_opmode_buffer)
	color = task_1a_part1.color(vision_sensor_image)
	return color






##############################################################


def main(rec_client_id):
	"""
	Purpose:
	---
	Teams are free to design their code in this task.
	The test executable will only call this function of task_5.py.
	init_remote_api_server() and exit_remote_api_server() functions are already defined
	in the executable and hence should not be called by the teams.
	The obtained client_id is passed to this function so that teams can use it in their code.
	However NOTE:
	Teams will have to call start_simulation() and stop_simulation() function on their own. 
	Input Arguments:
	---
	`rec_client_id` 	:  integer
		client_id returned after calling init_remote_api_server() function from the executable.
	
	Returns:
	---
	None
	Example call:
	---
	main(rec_client_id)
	
	"""
	##############	ADD YOUR CODE HERE	##############
	global maze_map,encoded_maze_t1,encoded_maze_t2,encoded_maze_t3,encoded_maze_t4
	img_t4 = cv2.imread("maze_t4.JPG")
	warped_t4 = task_1b.applyPerspectiveTransform(img_t4)
	encoded_maze_t4 = task_1b.detectMaze(warped_t4) 
	return_code = task_2b.send_data(rec_client_id,encoded_maze_t4,"t4")

	print(f"Encoded maze of t4  is {encoded_maze_t4}")
	
	img_t1 = cv2.imread("maze_t1.JPG")
	warped_t1 = task_1b.applyPerspectiveTransform(img_t1)
	encoded_maze_t1 = task_1b.detectMaze(warped_t1) 
	return_code = task_2b.send_data(rec_client_id,encoded_maze_t1,"t1")

	print(f"Encoded maze of t1  is {encoded_maze_t1}")
	print(path_map)
	complete_all_mapping_path('T1')
	complete_all_mapping_path('T4')
	print(path_map)
	# complete_all_mapping_path('T1')
	# complete_all_mapping_path('T1')
	return_code = task_2a.start_simulation()
	color = get_color()
	if(color):
		t4_path,aux_path = set_path(color)
	
	
		
		





	



	##################################################


# Function Name:    main (built in)
#        Inputs:    None
#       Outputs:    None
#       Purpose:    To call the main(rec_client_id) function written by teams when they
#					run task_5.py only.

# NOTE: Write your solution ONLY in the space provided in the above functions. This function should not be edited.
if __name__ == "__main__":
	client_id = task_2a.init_remote_api_server()
	
	main(client_id)