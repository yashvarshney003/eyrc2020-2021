# version 1.0.0
# #org for those which was original but i changed them for convineance
# #notim for those which i inicluded externally and not used anywhere

'''
*****************************************************************************************
*
*        		===============================================
*           		Nirikshak Bot (NB) Theme (eYRC 2020-21)
*        		===============================================
*
*  This script is to implement Task 3 of Nirikshak Bot (NB) Theme (eYRC 2020-21).
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
# Author List:      Yash Varshney,Anurag Saxena
# Filename:         task_3.py
# Functions:        init_setup(rec_client_id), control_logic(center_x,center_y), change_setpoint(new_setpoint)
#                   [ Comma separated list of functions in this file ]
# Global variables: client_id, setpoint=[],vision_sensor_handle,dt,current_time,prev_time,perror,derror,ierror,prev_error,kp,ki,kd,x_limit,y_limit,servohandle_x,servihandle_y
# 					[ List of global variables defined in this file ]


####################### IMPORT MODULES #########################
## You are not allowed to make any changes in this section.   ##
## You have to implement this task with the six available     ##
## modules for this task (numpy,opencv,os,sys,traceback,time) ##
################################################################
import numpy as np
import cv2
import os, sys
import traceback
import time


##############################################################

# Importing the sim module for Remote API connection with CoppeliaSim
try:
	import sim
	
except Exception:
	print('\n[ERROR] It seems the sim.py OR simConst.py files are not found!')
	print('\n[WARNING] Make sure to have following files in the directory:')
	print('sim.py, simConst.py and appropriate library - remoteApi.dll (if on Windows), remoteApi.so (if on Linux) or remoteApi.dylib (if on Mac).\n')
	sys.exit()


# Global variable "client_id" for storing ID of starting the CoppeliaSim Remote connection
# NOTE: DO NOT change the value of this "client_id" variable here
client_id = -1

# Global list "setpoint" for storing target position of ball on the platform/top plate
# The zeroth element stores the x pixel and 1st element stores the y pixel
# NOTE: DO NOT change the value of this "setpoint" list
setpoint = [640,640]

# Global variable "vision_sensor_handle" to store handle for Vision Sensor
# NOTE: DO NOT change the value of this "vision_sensor_handle" variable here


# You can add your global variables here
##############################################################
vision_sensor_handle = 0
dt = 0
current_time =0
prev_time = 0


perror = [0,0] #for x and y error values initialization
derror = [0,0]
ierror = [0,0]
prev_error = [0,0]

 #set accordingly
'''kp = [0.0035,0.0035]#[0.004,0.004]
kd = [0.007,0.007]#[0.009,0.009]
ki = [0.000009,0.000009]#[0.000,0.000] [0.000001,0.0000001]
'''
kp = [0.00179,0.00179]#[0.004,0.004]
kd = [0.0049,0.0049]#[0.009,0.009]
ki = [0.00001,0.00001]

x_limit = [-0.7,0.7] # min limit and maximum limit in degrees
y_limit = [-0.7,0.7]









##############################################################


################# ADD UTILITY FUNCTIONS HERE #################
## You can define any utility functions for your code.      ##
## Please add proper comments to ensure that your code is   ##
## readable and easy to understand.                         ##
##############################################################
servohandle_x = -1
servohandle_y = -1




##############################################################


def init_setup(rec_client_id):
	"""
	Purpose:
	---
	This function should:
	
	1. Get all the required handles from the CoppeliaSim scene and store them in global variables.
	2. Initialize the vision sensor in 'simx_opmode_streaming' operation mode (if required). 
	   Teams are allowed to choose the appropriate the oeration mode depending on their code and logic.
	Input Arguments:
	---
	`rec_client_id` 	:  [ integer ]
		the client_id generated from start connection remote API in Task 2A, should be stored in a global variable
	
	Returns:
	---
	None
	
	Example call:
	---
	init_setup()
	
	"""
	global client_id, vision_sensor_handle,servohandle_x,servohandle_y
	# since client_id is defined in task_2a.py file, it needs to be assigned here as well.
	client_id = rec_client_id

	##############	ADD YOUR CODE HERE	##############
	return_code,vision_sensor_handle = sim.simxGetObjectHandle(client_id,"vision_sensor_1",sim.simx_opmode_blocking)
	#print(f" return code{return_code} vsision hadnle {vision_sensor_handle}")

	returnCode, servohandle_x =sim.simxGetObjectHandle(client_id,"revolute_joint_ss_1", sim.simx_opmode_blocking)	
	#print(f" servihandle1 {returnCode} and {servohandle_x}")	#change object name as required
	returnCode, servohandle_y =sim.simxGetObjectHandle(client_id,"revolute_joint_ss_2", sim.simx_opmode_blocking)
	#print(f" servihandle2 {returnCode} and {servohandle_y}")
	
	
	##################################################


def control_logic(center_x,center_y):
	"""
	Purpose:
	---
	This function should implement the control logic to balance the ball at a particular setpoint on the table.
	The orientation of the top table should "ONLY" be controlled by the servo motor as we would expect in a 
	practical scenario.
	Hence "ONLY" the shaft of the servo motor or in other words the revolute joint between servo and servo fin 
	should have 'motor enabled' and 'control loop enabled option' checked. Refer documentation for further understanding of 
	these options.
	This function should use the necessary Legacy Python Remote APIs to control the revolute joints.
	NOTE: In real life, a 180 degree servo motor can rotate between -90 to +90 degrees or -1.57 to 1.57 radians only. 
		  Hence the command to be sent to servo motor should be between this range only. When the top plate is parallel to
		  base plate, the revolute joint between servo and servo fin should be at 0 degrees orientation. Refer documentation
		  for further understanding.
	NOTE: Since the simulation is dynamic in nature there should not by any bottlenecks in this code due to which the 
		  processing may take a lot of time. As a result 'control_logic' function should be called in every iteration of 
		  the while loop. Use global variables instead of reinitialising the varibles used in this function.
	
	Input Arguments:
	---
	`center_x` 	:  [ int ]
		the x centroid of the ball
	
	`center_y` 	:  [ int ]
		the y centroid of the ball
	
	Returns:
	---
	None
	
	Example call:
	---
	control_logic(center_x,center_y)
	
	"""
	##############	ADD YOUR CODE HERE	##############
	
	global setpoint, client_id,current_time,prev_time,dt,perror,derror,ierror,prev_error,servohandle_y,servohandle_x
	
	
	rt_code,current_time =sim.simxGetStringSignal(client_id,'time',sim.simx_opmode_buffer)
	#print(rt_code)
	current_time = float(current_time)



	sample_time = 0.25

	
	dt = current_time - prev_time
	#print("dt called")
	#print(f" dt time is {dt}")
	#print(dt,current_time,prev_time)

	if (dt>=0.25): # code is running 	for a sample time
		#print("value of dt:",dt)
		perror[0] = center_x-setpoint[0]
		perror[1] = center_y- setpoint[1]

		derror[0] = (perror[0] - prev_error[0])/dt
		derror[1] = (perror[1] - prev_error[1])/dt

		ierror[0] += perror[0]*dt
		ierror[1] +=  perror[1]*dt
		#print(f"print {perror} and {derror} and {ierror}")
		
		#print(f"{kp[0]*perror[0]} and {kd[0]*derror[0]} and {ki[0]*ierror[0]*dt}")
		if(abs(setpoint[0] -center_x) < 100):
		
			angle_x = 0 + (kp[0]*perror[0]) + (kd[0]*derror[0]) + (ki[0]*ierror[0])
		else:
			angle_x = 0 + (kp[0]*perror[0]) + (kd[0]*derror[0]) 
		if(abs(setpoint[1]-center_y)< 100):
			angle_y = 0 + (kp[1]*perror[1]) + (kd[1]*derror[1]) + (ki[1]*ierror[1])
		else:
			angle_y = 0 + (kp[1]*perror[1]) + (kd[1]*derror[1]) 


		angle_x = angle_x  #if any trim required
		angle_y = angle_y 
		#print("x_tilt:",angle_x,"    y_tilt",angle_y)
		#limiting maximum and minimum values of the output angle in degrees
	#	print(f"set value of algo {angle_x} and angle y {angle_y}")
	#	print("--------------------------------------------")
		if (angle_x < x_limit[0]):
			angle_x = x_limit[0]
		if (angle_x > x_limit[1]):
			angle_x = x_limit[1]
		
		if (angle_y < y_limit[0]):
			angle_y = y_limit[0]
		if (angle_y > y_limit[1]):
			angle_y = y_limit[1]

	#	print("************")
		#print("setpoint:",setpoint)
		#angle_x = 0.0
		#angle_y = -0.5

		#angle_y = -angle_y
		#print("x_tilt:",angle_x,"    y_tilt",angle_y)
		#print("position:",center_x,center_y)

		#send command to coppeliasim to rotate servo fin by simxsetjointtargetposition function try using simxopmodestreaming opmode
		returnCode=sim.simxSetJointTargetPosition(client_id,servohandle_x,angle_x,sim.simx_opmode_oneshot) # for x
		#print(returnCode)
		
		returnCode=sim.simxSetJointTargetPosition(client_id,servohandle_y,angle_y,sim.simx_opmode_oneshot)  # for y
		#print(returnCode)
		

		prev_error[0] = perror[0]
		prev_error[1] = perror[1]
		prev_time = current_time
		
		
		
	
	
	

	##################################################


# NOTE:	YOU ARE NOT ALLOWED TO MAKE ANY CHANGE TO THIS FUNCTION
# 
# Function Name:    change_setpoint
#        Inputs:    list of new setpoint-
#						new_setpoint=[x_pixel,y_pixel]
#       Outputs:    None
#       Purpose:    The function updates the value of global "setpoint" list after every 15 seconds of simulation time.
#					This will be ONLY called by executable file. 
def change_setpoint(new_setpoint):

	global setpoint
	setpoint=new_setpoint[:]


# NOTE:	YOU ARE NOT ALLOWED TO MAKE ANY CHANGE TO THIS FUNCTION
# 
# Function Name:    main
#        Inputs:    None
#       Outputs:    None
#       Purpose:    This part of the code is only for testing your solution. The function does the following:
# 						- imports 'task_1b' file as module
# 						- imports 'task_1a_part1' file as module
#						- imports 'task_2a' file as module
# 						- calls init_remote_api_server() function in 'task_2a' to connect with CoppeliaSim Remote API server
# 						- then calls start_simulation() function in 'task_2a' to start the simulation
#						- then calls init_setup() function to store the required handles in respective global variables and complete initializations if required
# 						- then calls get_vision_sensor_image() function in 'task_2a' to capture an image from the Vision Sensor in CoppeliaSim scene
# 						- If the return code is 'simx_return_ok':
# 									- then calls transform_vision_sensor_image() function in 'task_2a' to transform the captured image
# 						  			  to a format compatible with OpenCV. 
#			 						- then the transformed image is given as input and Perspective Transform is applied
#			 						  by calling applyPerspectiveTransform function	from 'task_1b'
#			 						- then the output of warped_img is given to 'scan_image' function from 'task_1a_part1'
#			 			- then calls control_logic() function to command the servo motors

# NOTE: Write your solution ONLY in the space provided in the above functions. Main function should not be edited.

if __name__ == "__main__":

	# Import 'task_1b.py' file as module
	try:
		import task_1b

	except ImportError:
		print('\n[ERROR] task_1b.py file is not present in the current directory.')
		print('Your current directory is: ', os.getcwd())
		print('Make sure task_1b.py is present in this current directory.\n')
		sys.exit()
		
	except Exception as e:
		print('Your task_1b.py throwed an Exception. Kindly debug your code!\n')
		traceback.print_exc(file=sys.stdout)
		sys.exit()
	
	# Import 'task_1a_part1.py' file as module
	try:
		import task_1a_part1

	except ImportError:
		print('\n[ERROR] task_1a_part1.py file is not present in the current directory.')
		print('Your current directory is: ', os.getcwd())
		print('Make sure task_1a_part1.py is present in this current directory.\n')
		sys.exit()
		
	except Exception as e:
		print('Your task_1a_part1.py throwed an Exception. Kindly debug your code!\n')
		traceback.print_exc(file=sys.stdout)
		sys.exit()
	
	# Import 'task_2a.py' file as module
	try:
		import task_2a

	except ImportError:
		print('\n[ERROR] task_2a.py file is not present in the current directory.')
		print('Your current directory is: ', os.getcwd())
		print('Make sure task_2a.py is present in this current directory.\n')
		sys.exit()
		
	except Exception as e:
		print('Your task_2a.py throwed an Exception. Kindly debug your code!\n')
		traceback.print_exc(file=sys.stdout)
		sys.exit()

	# Initiate the Remote API connection with CoppeliaSim server
	print('\nConnection to CoppeliaSim Remote API Server initiated.')
	print('Trying to connect to Remote API Server...')

	try:
		client_id = task_2a.init_remote_api_server()

		if (client_id != -1):
			print('\nConnected successfully to Remote API Server in CoppeliaSim!')

			# Starting the Simulation
			try:
				return_code = task_2a.start_simulation()

				if (return_code == sim.simx_return_novalue_flag):
					print('\nSimulation started correctly in CoppeliaSim.')
					
					# Storing the required handles in respective global variables.
					try:
						init_setup(client_id)
					except Exception:
						print('\n[ERROR] Your init_setup() function throwed an Exception. Kindly debug your code!')
						print('Stop the CoppeliaSim simulation manually if started.\n')
						traceback.print_exc(file=sys.stdout)
						print()
						sys.exit()

				else:
					print('\n[ERROR] Failed starting the simulation in CoppeliaSim!')
					print('start_simulation function in task_2a.py is not configured correctly, check the code!')
					print()
					sys.exit()

			except Exception:
				print('\n[ERROR] Your start_simulation function in task_2a.py throwed an Exception. Kindly debug your code!')
				print('Stop the CoppeliaSim simulation manually.\n')
				traceback.print_exc(file=sys.stdout)
				print()
				sys.exit()
		
		else:
			print('\n[ERROR] Failed connecting to Remote API server!')
			print('[WARNING] Make sure the CoppeliaSim software is running and')
			print('[WARNING] Make sure the Port number for Remote API Server is set to 19997.')
			print('[ERROR] OR init_remote_api_server function in task_2a.py is not configured correctly, check the code!')
			print()
			sys.exit()

	except Exception:
		print('\n[ERROR] Your init_remote_api_server function in task_2a.py throwed an Exception. Kindly debug your code!')
		print('Stop the CoppeliaSim simulation manually if started.\n')
		traceback.print_exc(file=sys.stdout)
		print()
		sys.exit()
	
	# Initialising the center_x and center_y variable to the current position of the ball
	center_x = 1063
	center_y = 1063
	
	init_simulation_time = 0
	curr_simulation_time = 0

	# Storing time when the simulation started in variable init_simulation_time
	return_code_signal,init_simulation_time_string=sim.simxGetStringSignal(client_id,'time',sim.simx_opmode_streaming)

	if(return_code_signal==0):
		init_simulation_time=float(init_simulation_time_string)

	# Running the coppeliasim simulation for 15 seconds
	while(curr_simulation_time - init_simulation_time <=15):
		
		return_code_signal,curr_simulation_time_string=sim.simxGetStringSignal(client_id,'time',sim.simx_opmode_buffer)
		
		if(return_code_signal == 0):
			curr_simulation_time=float(curr_simulation_time_string)
		
		try:
			vision_sensor_image, image_resolution, return_code = task_2a.get_vision_sensor_image(vision_sensor_handle)

			if ((return_code == sim.simx_return_ok) and (len(image_resolution) == 2) and (len(vision_sensor_image) > 0)):
				# print('\nImage captured from Vision Sensor in CoppeliaSim successfully!')

				# Get the transformed vision sensor image captured in correct format
				try:
					transformed_image = task_2a.transform_vision_sensor_image(vision_sensor_image, image_resolution)

					if (type(transformed_image) is np.ndarray):

						# cv2.imshow('transformed image', transformed_image)
						# cv2.waitKey(0)
						# cv2.destroyAllWindows()

						# Get the resultant warped transformed vision sensor image after applying Perspective Transform
						try:
							warped_img = task_1b.applyPerspectiveTransform(transformed_image)
							
							if (type(warped_img) is np.ndarray):
								
								# Get the 'shapes' dictionary by passing the 'warped_img' to scan_image function
								try:
									shapes = task_1a_part1.scan_image(warped_img)

									if (type(shapes) is dict and shapes!={}):
										print('\nShapes detected by Vision Sensor are: ')
										print(shapes)
										
										# Storing the detected x and y centroid in center_x and center_y variable repectively
										center_x = shapes['Circle'][1]
										center_y = shapes['Circle'][2]

									elif(type(shapes) is not dict):
										print('\n[ERROR] scan_image function returned a ' + str(type(shapes)) + ' instead of a dictionary.')
										print('Stop the CoppeliaSim simulation manually.')
										print()
										sys.exit()
								
								except Exception:
									print('\n[ERROR] Your scan_image function in task_1a_part1.py throwed an Exception. Kindly debug your code!')
									print('Stop the CoppeliaSim simulation manually.\n')
									traceback.print_exc(file=sys.stdout)
									print()
									sys.exit()
							
							else:
								print('\n[ERROR] applyPerspectiveTransform function is not configured correctly, check the code.')
								print('Stop the CoppeliaSim simulation manually.')
								print()
								sys.exit()
						
						except Exception:
							print('\n[ERROR] Your applyPerspectiveTransform function in task_1b.py throwed an Exception. Kindly debug your code!')
							print('Stop the CoppeliaSim simulation manually.\n')
							traceback.print_exc(file=sys.stdout)
							print()
							sys.exit()

					else:
						print('\n[ERROR] transform_vision_sensor_image function in task_2a.py is not configured correctly, check the code.')
						print('Stop the CoppeliaSim simulation manually.')
						print()
						sys.exit()

				except Exception:
					print('\n[ERROR] Your transform_vision_sensor_image function in task_2a.py throwed an Exception. Kindly debug your code!')
					print('Stop the CoppeliaSim simulation manually.\n')
					traceback.print_exc(file=sys.stdout)
					print()
					sys.exit()
			
			try:
				control_logic(center_x,center_y)
			
			except:
				print('\n[ERROR] Your control_logic function throwed an Exception. Kindly debug your code!')
				print('Stop the CoppeliaSim simulation manually.\n')
				traceback.print_exc(file=sys.stdout)
				print()
				sys.exit()

		except Exception:
			print('\n[ERROR] Your get_vision_sensor_image function in task_2a.py throwed an Exception. Kindly debug your code!')
			print('Stop the CoppeliaSim simulation manually.\n')
			traceback.print_exc(file=sys.stdout)
			print()
			sys.exit()

	# Ending the Simulation
	try:
		return_code = task_2a.stop_simulation()
		
		if (return_code == sim.simx_return_novalue_flag):
			print('\nSimulation stopped correctly.')

			# Stop the Remote API connection with CoppeliaSim server
			try:
				task_2a.exit_remote_api_server()

				if (task_2a.start_simulation() == sim.simx_return_initialize_error_flag):
					print('\nDisconnected successfully from Remote API Server in CoppeliaSim!')

				else:
					print('\n[ERROR] Failed disconnecting from Remote API server!')
					print('[ERROR] exit_remote_api_server function in task_2a.py is not configured correctly, check the code!')

			except Exception:
				print('\n[ERROR] Your exit_remote_api_server function in task_2a.py throwed an Exception. Kindly debug your code!')
				print('Stop the CoppeliaSim simulation manually.\n')
				traceback.print_exc(file=sys.stdout)
				print()
				sys.exit()
		
		else:
			print('\n[ERROR] Failed stopping the simulation in CoppeliaSim server!')
			print('[ERROR] stop_simulation function in task_2a.py is not configured correctly, check the code!')
			print('Stop the CoppeliaSim simulation manually.')
		
		print()
		sys.exit()

	except Exception:
		print('\n[ERROR] Your stop_simulation function in task_2a.py throwed an Exception. Kindly debug your code!')
		print('Stop the CoppeliaSim simulation manually.\n')
		traceback.print_exc(file=sys.stdout)
		print()
		sys.exit()
