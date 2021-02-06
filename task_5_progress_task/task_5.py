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
import multiprocessing
#import concurrent.features
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
servo_handle_x_t4 = -1
servo_handle_y_t4 = -1
servo_handle_x_t3 = -1
servo_handle_y_t3 = -1
servo_handle_x_t2 = -1
servo_handle_y_t2 = -1
servo_handle_x_t1 = -1
servo_handle_y_t1 = -1



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
def traverse_ball(tabel_no,servohandle_x,servohandle_y,vision_sensor_handle,pixel_path):
	global client_id
	
	print(f" client is  {client_id}")
	print(f" traverse function called{pixel_path}")
	rt_code, prev_time = sim.simxGetStringSignal(client_id,'time',sim.simx_opmode_streaming)
	print(prev_time)
	current_time = ''
	while(len(current_time) == 0  ):
		rt_code,current_time =sim.simxGetStringSignal(client_id,'time',sim.simx_opmode_buffer)
		print("didbdibdibdibd",current_time)
	
	
	j = 0
	k= 0
	for i in pixel_path:
		if(i == pixel_path[-1]):
			i[0] = i[0]+20
		i.reverse()
		task_3.change_setpoint(i)
		while(1):
			j+=1
			k+=1
			print("#########################################################################")
			#print(j)
			name1 = "table_"+ str(tabel_no)+ "__"+str(j) + ".png"
			name2 = "table_"+ str(tabel_no)+ "__"+str(k)+"k123.png"
			
			
			vision_sensor_image, image_resolution, return_code = task_2a.get_vision_sensor_image(vision_sensor_handle)
			transformed_image = task_2a.transform_vision_sensor_image(vision_sensor_image,image_resolution)
			
			
			warped_img = task_1b.applyPerspectiveTransform(transformed_image,j,tabel_no)
			print(name2)
			
			#cv2.imwrite(name1,transformed_image)
			#cv2.imwrite(name2,warped_img)
			
			
			
			
			
			shapes = task_1a_part1.scan_image(warped_img,k)

			if(shapes):
				#print(f"client id in task 4b{client_id}")
				#print(f"sent this {i[1]} and {i[0]}")
				
				#print(f"here1 {shapes} and {i} ")
				#print(shapes['Circle'][1]-i[0],abs(shapes['Circle'][2]-i[1]))
				
				warped_img = cv2.cvtColor(warped_img,cv2.COLOR_GRAY2RGB)
				warped_img = cv2.circle(warped_img,(shapes['Circle'][1],shapes['Circle'][2]),5,(0,255,0),2)
				warped_img = cv2.circle(warped_img,(i[0],i[1]),5,(255,0,0),2)
				
					
				
				if(abs(shapes['Circle'][1]-i[0]) <= 30  and abs(shapes['Circle'][2]-i[1]) <= 30):
					#print("here2")
					#print("her-------------------------------------------------------------------------------------")
					break
					
				else:
					task_3.control_logic(client_id,shapes['Circle'][1],shapes['Circle'][2],servohandle_x,servohandle_y)
	return 1
		









	
def make_connection():
	global vision_sensor_5,vision_sensor_4,vision_sensor_3,vision_sensor_2,vision_sensor_1,servo_handle_x_t1,servo_handle_y_t1,servo_handle_x_t4,servo_handle_y_t4
	return_code,servo_handle_x_t1   = sim.simxGetObjectHandle(client_id,"revolute_joint_ss_t1_1",sim.simx_opmode_blocking)
	return_code,servo_handle_y_t1   = sim.simxGetObjectHandle(client_id,"revolute_joint_ss_t1_2",sim.simx_opmode_blocking)
	return_code,servo_handle_x_t4   = sim.simxGetObjectHandle(client_id,"revolute_joint_ss_t4_1",sim.simx_opmode_blocking)
	return_code,servo_handle_y_t4   = sim.simxGetObjectHandle(client_id,"revolute_joint_ss_t4_2",sim.simx_opmode_blocking)
	print("all handles")
	print(servo_handle_x_t1,servo_handle_y_t1,servo_handle_y_t4,servo_handle_x_t4)
	



	return_code,vision_sensor_1 = sim.simxGetObjectHandle(client_id,"vision_sensor_1",sim.simx_opmode_blocking)
	#return_code,vision_sensor_2 = sim.simxGetObjectHandle(client_id,"vision_sensor_2",sim.simx_opmode_blocking)
	#return_code,vision_sensor_3 = sim.simxGetObjectHandle(client_id,"vision_sensor_3",sim.simx_opmode_blocking)
	return_code,vision_sensor_4 = sim.simxGetObjectHandle(client_id,"vision_sensor_4",sim.simx_opmode_blocking)
	return_code,vision_sensor_5 = sim.simxGetObjectHandle(client_id,"vision_sensor_5",sim.simx_opmode_blocking)
	print(f"vision_sensor is {vision_sensor_1} and {vision_sensor_4} and {vision_sensor_5} ")

def set_path(color):
	global t4_path,aux_path
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
	global map_start,map_end,maze_map,path_map,encoded_maze_t1
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
		path_map[tablenum].append(pixel_path)
		#print(f"{tablenum} and {pixel_path}")
		#print("-------------------------------------------------------------------")

	
def get_color():
	global vision_sensor_5,client_id
	color = None
	print(f"vsision sensor i s{vision_sensor_5}")
	return_code ,image_resolution,vision_sensor_image =sim.simxGetVisionSensorImage(client_id,vision_sensor_5,0,sim.simx_opmode_blocking)
	print(len(vision_sensor_image))
	i = 0 
	
	while(color is None ):
		i+=1
		return_code ,image_resolution,vision_sensor_image = sim.simxGetVisionSensorImage(client_id,vision_sensor_5,0,sim.simx_opmode_blocking)
		#print(f"lengthgggggggggggggggggg  {len(vision_sensor_image)} and  {return_code}")
		
		
		if(len(vision_sensor_image)):
			#print(f"aa hi gaye {len(vision_sensor_image)}")
			vision_sensor_image = task_2a.transform_vision_sensor_image(vision_sensor_image,image_resolution)
			#cv2.imwrite("vision5image.png",vision_sensor_image)
			#print(f"number of iteration run  {i} ")
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
	global maze_map,encoded_maze_t1,encoded_maze_t2,encoded_maze_t3,encoded_maze_t4,t4_path,aux_path,servo_handle_x_t1,servo_handle_y_t1
	global servo_handle_x_t4,servo_handle_y_t4
	img_t4 = cv2.imread("maze_t4.JPG")
	warped_t4 = task_1b.applyPerspectiveTransform(img_t4,0,-1)
	encoded_maze_t4 = task_1b.detectMaze(warped_t4) 
	maze_map['T4'] = encoded_maze_t4
	return_code = task_2b.send_data(rec_client_id,encoded_maze_t4,"t4")

	#print(f"Encoded maze of t4  is {encoded_maze_t4}")
	
	img_t1 = cv2.imread("maze_t1.JPG")
	warped_t1 = task_1b.applyPerspectiveTransform(img_t1,0,-1)
	encoded_maze_t1 = task_1b.detectMaze(warped_t1) 
	maze_map['T1'] = encoded_maze_t1
	#print(f"here it is{maze_map}")
	
	return_code = task_2b.send_data(rec_client_id,encoded_maze_t1,"t1")
	print(f"return_code is {return_code}")

	#print(f"Encoded maze of t1  is {encoded_maze_t1}")
	#print(path_map)
	#print(maze_map)
	complete_all_mapping_path('T1')
	complete_all_mapping_path('T4')
	
	make_connection()
	# print("path of t4 is ")
	# print(f" {path_map}")
	
	
	# complete_all_mapping_path('T1')
	# complete_all_mapping_path('T1')
	return_code = task_2a.start_simulation()
	color = get_color()
	print(f" color is found is {color}")
	if(color):
		set_path(color)
		print(f" we find tha path {t4_path} and {aux_path}")
	
	return_code = traverse_ball(4,servo_handle_x_t4,servo_handle_y_t4,vision_sensor_4,t4_path)
	return_code = traverse_ball(1,servo_handle_x_t1,servo_handle_y_t1,vision_sensor_1,aux_path)
	print(" ab hame sahi se bekaar ke print and saving statement hatha ke karna hai saari chezze ek baar check karlena kyuki ek bhi galti 0 makrs")

		

		

	
		
		





	



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