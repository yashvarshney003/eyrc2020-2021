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
# Theme:            Nirikshak Bot (NB)
# Author List:     Yash Varshney, Aman Tyagi
# Filename:         task_6.py
# Functions:       color_get,traverse_ball,send_data_to_draw_path, make_connection,set_path,complete_all_mapping_path,get_color  
#                   [ Comma separated list of functions in this file ]
# Global variables: vision_sensor_1, vision_sensor_2,vision_sensor_3,vision_sensor_4,
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
import json
import matplotlib.pyplot as plt
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
handle_list = {}

# Opening json file and converting json object into python dictionary
try:
	with open('ball_details.json') as file:
		ball_details = json.load(file)

except ImportError:
	print('\n[ERROR] ball_details.json file is not present in the current directory.')
	print('Your current directory is: ', os.getcwd())
	print('Make sure ball_details.json is present in this current directory.\n')

# map_start_coord_coord : This is the dictionary contain  tha starting and coordinates of mazes.
map_start_coord = {
	"T4":[(0,5)],
	"T3":[(4,9)],
	"T2":[(0,4)],
	"T1":[(5,0)]
	}
# do mapping of start and end point on the basis of color and json file.
# map_end_coord_coord : This is the dictionary contain ending coordinates of mazes.
map_end_coord = {
"T4":[(4,0),(5,9), (9,4) ],
"T3":[(9,5), (5,0), (0,4)],
"T2":[(4,9), (9,5), (5,0)],
"T1":[(0,4), (4,9), (9,5)]
}

# t4_path : This is the pixel path to traverse by current ball to drop ball on another table
# aux_path : This is the pixel path to traverse by current ball to drop ball on collection_ball
#  
t4_path = None			#path to table req
aux_path = None			#path to req cb

# path_map : This is the dictionary which hold the pixel path to all end of given table.

path_map = {			#pixel path to each exit point on the table
"T1":[],
"T2":[],
"T3":[],
"T4":[]
}

# path_box_map : This is the dictionary which hold the pixel path to all end of given tables in terms of row and column.
path_box_map = {		#box coordinates path to draw path on the tables
"T1":[],
"T2":[],
"T3":[],
"T4":[]
}

# maze_map : This dictionary contain all the encoded maze_array.
maze_map ={
}


# collection_box : " Integer variable to store the number of the collection box"
collection_box = None	


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
	color_and_cb = [ball_color + '::' + collection_box_name]
	
	inputBuffer = bytearray()
	return_code, retInts, retFloats, retStrings, retBuffer = sim.simxCallScriptFunction(client_id,'evaluation_screen_respondable_1',
							sim.sim_scripttype_childscript,'color_and_cb_identification',[],[],color_and_cb,inputBuffer,sim.simx_opmode_blocking)






################# ADD UTILITY FUNCTIONS HERE #################
## You can define any utility functions for your code.      ##
## Please add proper comments to ensure that your code is   ##
## readable and easy to understand.                         ##
##############################################################






def invert_model_properties(object_handle):
    # NOTE: This function will be used to invert model properties such that the model which is not to be
    # 		traversed in the current iteration can be partially disabled thereby saving the computational
    #		resources.

    global client_id
    _, curr_model_prop = sim.simxGetModelProperty(client_id,object_handle,sim.simx_opmode_blocking)
    if(curr_model_prop == 0):
        # Overrides the required model props as NOT measureable, NOT dynamic, NOT collidable, NOT
        # renderable, NOT detectable, NOT respondable and Invisible to other model's bounding boxes.
        return_code = sim.simxSetModelProperty(client_id,object_handle,1135,sim.simx_opmode_blocking)
    else:
        return_code = sim.simxSetModelProperty(client_id,object_handle,0,sim.simx_opmode_blocking)



'''	Function name: color_get
	Inputs: Image from vision sensor
	Outputs: Color of the ball detected in the image
	Usage: Takes in the image from the vision sensors and returns the color of the ball detected in the image
	Example call: color_get(image_from_vision_sensor)

'''	
def get_color(img_file_path):
	#print("color get called")
	if(img_file_path is None):
		return

    #Read the image
    
	if type(img_file_path) == type(str()):
		img_file_path = cv2.imread(img_file_path)
	else:
		img_file_path= img_file_path
    #cv2.imwrite("colorefromrailing.png",img_file_path)
    
	imageFrame = cv2.GaussianBlur(img_file_path,(5,5),cv2.BORDER_TRANSPARENT)
	hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV) 
    
    #To create a mask for red colour
	red_lower = np.array([0, 50, 50]) 
	red_upper = np.array([10, 255, 255]) 
	red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)
	kernal = np.ones((5, 5))
	red_gray=cv2.threshold(red_mask, 245,225, cv2.THRESH_BINARY)[1]
	gray_blur_red= cv2.Canny(red_gray,100,255)
	
	
	

    #Create a mask for blue colour
	blue_lower = np.array([94, 20, 0], np.uint8) 
	blue_upper = np.array([140,255 ,255], np.uint8) 
	blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper) 
	kernal = np.ones((5, 5))  
	blue_mask = cv2.dilate(blue_mask, kernal)
	blue_gray=cv2.threshold(blue_mask, 245,225, cv2.THRESH_TRUNC)[1]
	gray_blur_blue= cv2.Canny(blue_gray,100,255)
    
    #Create a mask for green colour
	green_lower = np.array([25, 52, 72], np.uint8) 
	green_upper = np.array([102, 255, 255], np.uint8) 
	green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)
	kernal = np.ones((5, 5))
	green_mask = cv2.dilate(green_mask, kernal)
	green_gray=cv2.threshold(green_mask, 250,255, cv2.THRESH_BINARY)[1]
	gray_blur_green = cv2.Canny(green_gray,100,255)
	#find contours on blue mask
	cnts= cv2.findContours(gray_blur_blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	if type(cnts[-1]) !=type(None):
			if len(cnts) == 2:
				cnts = cnts[0]
			elif len(cnts) == 3:
				cnts = cnts[1]
			if (len(cnts)):
				return 'blue'
				#Find red contours in the image
	cnts= cv2.findContours(gray_blur_red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
	if type(cnts[-1]) !=type(None) :
		if len(cnts) == 2:
			cnts = cnts[0]
		elif len(cnts) == 3:
			cnts = cnts[1]
		if (len(cnts)):
				print("here red")
				return 'red'
	# Find green contours in the image
	cnts= cv2.findContours(gray_blur_green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	if type(cnts[-1]) !=type(None) :
		if len(cnts) == 2:
			cnts = cnts[0]
		elif len(cnts) == 3:
			cnts = cnts[1]
		if(len(cnts)):
			return 'green'
# #########
def tilt(servo_handle_x, servo_handle_y, pixel_path):
	global servo_handle_x_t1
	y_diff = pixel_path[1][1] - pixel_path[0][1]
	x_diff = pixel_path[1][0] - pixel_path[0][0]

	tilt_dir = [x_diff!=0, y_diff!=0]
	if (tilt_dir[0]):
		return [-(x_diff//abs(x_diff)), 0]
	elif(tilt_dir[1]):
		return [0, (y_diff//abs(y_diff))]
	


'''	Function name: traverse_ball
	Usage: traverses the ball from starting coordinate of maze to end coordinate to pass ball from one maze to
			to another or drop ball in collection box. 
	Inputs: servo handles(x and y), vision sensor to be read and pixel path which the ball has to follow
	Outputs: None
	Example Call : traverse_ball(servohandle_x_t4, servo_handle_y_t4, visionsensor_4, t4_path)
'''
def traverse_ball(servohandle_x,servohandle_y,vision_sensor_handle,pixel_path):
	tilt_value_x, tilt_value_y = tilt(pixel_path[0], pixel_path[1])
	print(f" {tilt_value_x * 0.36} and  {tilt_value_y *0.36}")
	

	global client_id
	_, prev_time = sim.simxGetStringSignal(client_id,'time',sim.simx_opmode_streaming)
	current_time = ''
	while(len(current_time) == 0  ):
		_,current_time =sim.simxGetStringSignal(client_id,'time',sim.simx_opmode_buffer)
	
	j = 0
	k= 0
	for i in pixel_path:
		i.reverse()
		task_3.change_setpoint(i)
		while(1):
			
			
			vision_sensor_image, image_resolution,_ = task_2a.get_vision_sensor_image(client_id,vision_sensor_handle)
			transformed_image = task_2a.transform_vision_sensor_image(vision_sensor_image,image_resolution)
			warped_img = task_1b.applyPerspectiveTransform(transformed_image)
			#plt.imshow(warped_img)
			#plt.show()




			shapes = task_1a_part1.scan_image(warped_img)
			
			if(shapes):
				if(shapes.get('Circle')[2]>=88):
					warped_img = cv2.cvtColor(warped_img,cv2.COLOR_GRAY2RGB)
					warped_img = cv2.circle(warped_img,(shapes['Circle'][1],shapes['Circle'][2]),5,(0,255,0),2)
					warped_img = cv2.circle(warped_img,(i[0],i[1]),5,(255,0,0),2)
				
					
				
					if(abs(shapes['Circle'][1]-i[0]) <= 30  and abs(shapes['Circle'][2]-i[1]) <= 25):
						j+=1
						break
						
					else:
						task_3.control_logic(client_id,shapes['Circle'][1],shapes['Circle'][2],servohandle_x,servohandle_y)
				else:
					
					returnCode=sim.simxSetJointTargetPosition(client_id,servohandle_x,tilt_value_x * 0.36,sim.simx_opmode_oneshot) # for x
					#print(returnCode)
					#print(f" after trim  {angle_x} and  { angle_x} ")
					
					returnCode=sim.simxSetJointTargetPosition(client_id,servohandle_y,tilt_value_y * 0.36,sim.simx_opmode_oneshot) 
			else:
				
				returnCode=sim.simxSetJointTargetPosition(client_id,servohandle_x,tilt_value_x*0.36,sim.simx_opmode_oneshot) # for x
					#print(returnCode)
					#print(f" after trim  {angle_x} and  { angle_x} ")
					
				returnCode=sim.simxSetJointTargetPosition(client_id,servohandle_y,tilt_value_y*0.36,sim.simx_opmode_oneshot) 

				
	
		
''' 	Function name: send_data_to_draw_path
	Usage: Draws path on the table in Coppleiasim scene
	Inputs: table no and the box path to be drawn
	Outputs: None
	Example call: send_data_to_draw_path('T4', pixel_path_list)
'''
def send_data_to_draw_path(table,path):
		global client_id
		

		##############	IF REQUIRED, CHANGE THE CODE FROM HERE	##############

		coppelia_sim_coord_path = []
		table_name = "top_plate_respondable_t" + str(table) + "_" + '1'
		
		for coord in path:
			for element in coord:
				coppelia_sim_coord_path.append(((10*element) - 45)/100)

		inputBuffer = bytearray()

		return_code, retInts, retFloats, retStrings, retBuffer = sim.simxCallScriptFunction(client_id, \
							table_name, sim.sim_scripttype_customizationscript, 'drawPath', [], \
							coppelia_sim_coord_path, [], inputBuffer, sim.simx_opmode_oneshot)

'''	
Function name: make_connection 
	Usage: Establishes connection with the Coppleiasim server and populates the global variable handle list with the updated values of servo handle and vision sensors
	Inputs: None
	Outputs: None
	Example call: make_connection()
'''
def make_connection():
	global client_id,handle_list
	global vision_sensor_5,vision_sensor_4,vision_sensor_3,vision_sensor_2,vision_sensor_1,servo_handle_x_t1,servo_handle_y_t1,servo_handle_x_t4,servo_handle_y_t4
	return_code,servo_handle_x_t1   = sim.simxGetObjectHandle(client_id,"revolute_joint_ss_t1_1",sim.simx_opmode_blocking)
	return_code,servo_handle_y_t1   = sim.simxGetObjectHandle(client_id,"revolute_joint_ss_t1_2",sim.simx_opmode_blocking)
	return_code,servo_handle_x_t4   = sim.simxGetObjectHandle(client_id,"revolute_joint_ss_t4_1",sim.simx_opmode_blocking)
	return_code,servo_handle_y_t4   = sim.simxGetObjectHandle(client_id,"revolute_joint_ss_t4_2",sim.simx_opmode_blocking)
	return_code,servo_handle_x_t2   = sim.simxGetObjectHandle(client_id,"revolute_joint_ss_t2_1",sim.simx_opmode_blocking)
	return_code,servo_handle_y_t2   = sim.simxGetObjectHandle(client_id,"revolute_joint_ss_t2_2",sim.simx_opmode_blocking)
	return_code,servo_handle_x_t3   = sim.simxGetObjectHandle(client_id,"revolute_joint_ss_t3_1",sim.simx_opmode_blocking)
	return_code,servo_handle_y_t3   = sim.simxGetObjectHandle(client_id,"revolute_joint_ss_t3_2",sim.simx_opmode_blocking)
	

	return_code,vision_sensor_1 = sim.simxGetObjectHandle(client_id,"vision_sensor_1",sim.simx_opmode_blocking)
	return_code,vision_sensor_2 = sim.simxGetObjectHandle(client_id,"vision_sensor_2",sim.simx_opmode_blocking)
	return_code,vision_sensor_3 = sim.simxGetObjectHandle(client_id,"vision_sensor_3",sim.simx_opmode_blocking)
	return_code,vision_sensor_4 = sim.simxGetObjectHandle(client_id,"vision_sensor_4",sim.simx_opmode_blocking)
	return_code,vision_sensor_5 = sim.simxGetObjectHandle(client_id,"vision_sensor_5",sim.simx_opmode_blocking)
	handle_list = {'T4' : [servo_handle_x_t4,servo_handle_y_t4,vision_sensor_4],
					'T3' : [servo_handle_x_t3,servo_handle_y_t3,vision_sensor_3],
					'T2' : [servo_handle_x_t2,servo_handle_y_t2,vision_sensor_2],
					'T1' : [servo_handle_x_t1,servo_handle_y_t1,vision_sensor_1]
					}



'''	Function name: set_path
	Usage: sets variables used to make the ball reach to its destination collection box according to the color using ball_details json dictionary.
	It calls send_data_to_draw_path to draw the path on the table.
	Inputs: color of the detected ball : string
	Outputs: None
	Example call: set_path('green')
'''
def set_path(color):
	global t4_path,aux_path
	
	table, collection_box = ball_details[color][0].split('_')
	t4_path=path_map['T4'][int(table[-1])-1]
	t4_path_drawn = path_box_map['T4'][int(table[-1])-1]
	send_data_to_draw_path(4,t4_path_drawn)
	aux_path = path_map[table][int(collection_box[-1])-1]
	aux_path_drawn = path_box_map[table][int(collection_box[-1])-1]
	send_data_to_draw_path(int(table[1]),aux_path_drawn)
	ball_details[color].pop(0)

'''	Function name: complete_all_mapping_path
	Usage: Sets all mapping path according to the values of entry and exit points of the table and the maze.
			It also manipulates the setpoints according to the required collection box collection box
			(line no 452-478) to make the ball fall in the collection box.
	Inputs: Table number for which the paths have to be set : string
	Outputs: None
	Example Call: complete_all_mapping_path('T4')

'''

def complete_all_mapping_path (tablenum):
	global map_start_coord,map_end_coord,maze_map,path_map,encoded_maze_t1,path_box_map
	# for all exit points we are calculating path
	for i in range(3):
		# starting coordinates for maze.
		start_coord= map_start_coord[tablenum][0]
		# end coordinates.
		end_coord= map_end_coord[tablenum][i]
		# encoded_path of maze from maze_map of given tablenum.
		mazearray = maze_map[tablenum]
		# extracting path for given start and end coordinates using task_4a
		path = task_4a.find_path(mazearray, start_coord, end_coord)
		# storing path for further work
		path_box_map[tablenum].append(path)	
		# In actual image we have dimension 1280 but all four side have walls which make walls of 1120 pixels 
		resolution_x = 1120#1280
	
		resolution_y = 1120#1280

		x_increment = resolution_x//10
		y_increment = resolution_y//10
		pixel_path = []
		for i in range(len(path)):
			pixel_path.append([])

		for i in range(len(path)):
			# to change the pixel trim: change 180 with pixel*10 and 18 with pixel
			x_pix_trim = int(((180*path[i][0])/45)-18)
			y_pix_trim = int(((180*path[i][1])/45)-18)

			x_pixel = ((x_increment//2) + path[i][0]*x_increment) + 80 + x_pix_trim
			y_pixel = ((y_increment//2) + path[i][1]*y_increment) + 80 + y_pix_trim
			pixel_path[i].append(x_pixel)
			pixel_path[i].append(y_pixel)
		if (tablenum == 'T1'):
			if (path[len(path)-1] == map_end_coord[tablenum][0]):		#(0,4) decrease y pixel [tilt in +ve y]
				pixel_path.append( [ pixel_path[len(pixel_path)-1][0]- (y_increment//2 + 32), pixel_path[len(pixel_path)-1][1]])
			elif (path[len(path)-1] == map_end_coord[tablenum][1]):	#(4,9) increase x pixel [tilt in +ve x]
				pixel_path.append( [ pixel_path[len(pixel_path)-1][0] , pixel_path[len(pixel_path)-1][1] + (x_increment//2 + 32)])
			elif (path[len(path)-1] == map_end_coord[tablenum][2]):	#(9,5) increase y pixel [tilt in -ve y]
				pixel_path.append( [ pixel_path[len(pixel_path)-1][0] + (y_increment//2 + 32), pixel_path[len(pixel_path)-1][1] ])
			else:
				print("Unexpected element in the end of the path in maze T1")

		if (tablenum == 'T2'):
			if (path[len(path)-1] == map_end_coord[tablenum][0]):		#(4,9) increase x pixel [tilt in +ve x]
				pixel_path.append( [ pixel_path[len(pixel_path)-1][0]  , pixel_path[len(pixel_path)-1][1]+(x_increment//2 + 32)] )
			elif (path[len(path)-1] == map_end_coord[tablenum][1]):	#(9,5) increase y pixel [tilt in -ve y]
				pixel_path.append( [ pixel_path[len(pixel_path)-1][0] + (y_increment//2 + 32), pixel_path[len(pixel_path)-1][1] ])
			elif (path[len(path)-1] == map_end_coord[tablenum][2]):	#(5,0) decrease x pixel [tilt in -ve x]
				pixel_path.append( [ pixel_path[len(pixel_path)-1][0] , pixel_path[len(pixel_path)-1][1] - (x_increment//2 + 32)])
			else:
				print("Unexpected element in the end of the path in maze T2")

		if (tablenum == 'T3'):
			if (path[len(path)-1] == map_end_coord[tablenum][0]):		#(9,5) increase y pixel [tilt in -ve y]
				pixel_path.append( [ pixel_path[len(pixel_path)-1][0] + (y_increment//2 + 32), pixel_path[len(pixel_path)-1][1] ])
			elif (path[len(path)-1] == map_end_coord[tablenum][1]):	#(5,0) decrease x pixel [tilt in -ve x]
				pixel_path.append( [ pixel_path[len(pixel_path)-1][0]  , pixel_path[len(pixel_path)-1][1] - (x_increment//2 + 32)])
			elif (path[len(path)-1] == map_end_coord[tablenum][2]):	#(0,4) decrease y pixel [tilt in +ve y]
				pixel_path.append( [ pixel_path[len(pixel_path)-1][0]- (y_increment//2 + 32), pixel_path[len(pixel_path)-1][1]])
			else:
				print("Unexpected element in the end of the path in maze T3")

		if (tablenum == 'T4'):
			if (path[len(path)-1] == map_end_coord[tablenum][0]):		#(5,9) increase x pixel [tilt in +ve x]
				pixel_path.append( [ pixel_path[len(pixel_path)-1][0]  , pixel_path[len(pixel_path)-1][1] + (x_increment//2 + 32)] )
			elif (path[len(path)-1] == map_end_coord[tablenum][1]):	#(9,4) increase y pixel [tilt in -ve y]
				pixel_path.append( [ pixel_path[len(pixel_path)-1][0] + (y_increment//2 + 32), pixel_path[len(pixel_path)-1][1]])
			elif (path[len(path)-1] == map_end_coord[tablenum][2]):	#(4,0) decrease x pixel [tilt in -ve x]
				pixel_path.append( [ pixel_path[len(pixel_path)-1][0]  , pixel_path[len(pixel_path)-1][1]- (x_increment//2 + 32)])
			else:
				print("Unexpected element in the end of the path in maze T4")

		if ((path[len(path)-3][0] == path[len(path)-1][0]) or (path[len(path)-3][1] == path[len(path)-1][1])):
			path.pop(len(path)-2)
			
			
		path_map[tablenum].append(pixel_path)





'''	Function name: get_color 
	Usage: It sends the vision sensor image to the color_get function repeatedly and waits until the called function returns a color.
	Inputs: None
	Outputs: color of the detected ball
'''





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
	global servo_handle_x_t4,servo_handle_y_t4,path_box_map,collection_box
	global client_id,ball_details
	client_id = rec_client_id

# Firstly we are calculating all the possible path exist for all mazes and storing them in form of dictionary or arrays

	# Reading image maze_t4

	img_t4 = cv2.imread("maze_t4.JPG")


	#applying Perspective transform to separate maze from  given image
	warped_t4 = task_1b.applyPerspectiveTransform(img_t4)

	# Encoding maze into array form 
	encoded_maze_t4 = task_1b.detectMaze(warped_t4)

	# storing maze in maze_map dictionary 
	maze_map['T4'] = encoded_maze_t4
	print('encoded maze t4', maze_map['T4'])

	# sending data to draw path on top_plate repectively
	return_code = task_2b.send_data(rec_client_id,encoded_maze_t4,"t4")
	
	img_t1 = cv2.imread("maze_t1.JPG")
	warped_t1 = task_1b.applyPerspectiveTransform(img_t1)
	encoded_maze_t1 = task_1b.detectMaze(warped_t1) 
	# print(f" encoded maze t1 {encoded_maze_t1}")
	maze_map['T1'] = encoded_maze_t1
	return_code = task_2b.send_data(rec_client_id,encoded_maze_t1,"t1")


	img_t2 = cv2.imread("maze_t2.JPG")
	warped_t2 = task_1b.applyPerspectiveTransform(img_t2)
	encoded_maze_t2 = task_1b.detectMaze(warped_t2) 
	maze_map['T2'] = encoded_maze_t2
	return_code = task_2b.send_data(rec_client_id,encoded_maze_t2,"t2")

	img_t3 = cv2.imread("maze_t3.JPG")
	warped_t3 = task_1b.applyPerspectiveTransform(img_t3)
	encoded_maze_t3 = task_1b.detectMaze(warped_t3) 
	maze_map['T3'] = encoded_maze_t3
	return_code = task_2b.send_data(rec_client_id,encoded_maze_t3,"t3")

	# calling complete_all_mapping_path to find all the possible path to drop in any collection box. 

	complete_all_mapping_path('T1')
	
	complete_all_mapping_path('T3')
	complete_all_mapping_path('T2')
	complete_all_mapping_path('T4')
	

	

	make_connection()
	# Starting simulation


	return_code = task_2a.start_simulation(rec_client_id)
	i = 0
	# This while loop run till the list of all keys of dictionary become empty.
	"""
	  First we call get_color function to find the color of ball passing underneath vision sensor 5
	  then collection box and table is identified using ball_details dictionary and then traverse fucntion
	  is called to traverse the ball on maze till it dropped in assigned collection box.

	"""

	while(any([len(i)!=0 for i in list(ball_details.values())])):
		print([len(i) != 0 for i in list(ball_details.values())])
		color = None
		while(color is None ):
			return_code ,image_resolution,vision_sensor_image = sim.simxGetVisionSensorImage(client_id,vision_sensor_5,0,sim.simx_opmode_blocking)
			
			
			if(len(vision_sensor_image)):
				vision_sensor_image = task_2a.transform_vision_sensor_image(vision_sensor_image,image_resolution)
				
				
				color = get_color(vision_sensor_image)

		if(color):
			print('identified color:', color)
			collection_box = ball_details[color][0]
			table = ball_details[color][0].split('_')[0]
			print(f"  table  {table}")
			
			send_color_and_collection_box_identified(color, collection_box)
			set_path(color)
		
		traverse_ball(handle_list["T4"][0],handle_list["T4"][1],handle_list["T4"][2],t4_path)
		traverse_ball(handle_list[table][0],handle_list[table][1],handle_list[table][2],aux_path)
		print("complete ho gaya task")
		print(len(list(ball_details.values())))
		print(f"  i is {i} ")
	time.sleep(5)

	# Stopping the simulation
	task_2a.stop_simulation(rec_client_id)
	
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
