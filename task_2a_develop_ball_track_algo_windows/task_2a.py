'''
*****************************************************************************************
*
*        		===============================================
*           		Nirikshak Bot (NB) Theme (eYRC 2020-21)
*        		===============================================
*
*  This script is to implement Task 2A of Nirikshak Bot (NB) Theme (eYRC 2020-21).
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

# Team ID:          [2139]
# Author List:      [ Yash Varshney,Aman Tyagi]
# Filename:         task_2a.py
# Functions:        init_remote_api_server, start_simulation, get_vision_sensor_image, transform_vision_sensor_image,
# 					stop_simulation, exit_remote_api_server
#                   [ Comma separated list of functions in this file ]
# Global variables: client_id
# 					[ List of global variables defined in this file ]


####################### IMPORT MODULES #######################
## You are not allowed to make any changes in this section. ##
## You have to implement this task with the three available ##
## modules for this task (numpy,opencv,os,sys,traceback)    ##
##############################################################
import numpy as np
import cv2
import os, sys
import traceback
import time
#Remove this

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
iteration = 1


################# ADD UTILITY FUNCTIONS HERE #################
## You can define any utility functions for your code.      ##
## Please add proper comments to ensure that your code is   ##
## readable and easy to understand.                         ##
##############################################################






##############################################################


def init_remote_api_server():

	"""
	Purpose:
	---
	This function should first close any open connections and then start
	communication thread with server i.e. CoppeliaSim.

	NOTE: In this Task, do not call the exit_remote_api_server function in case of failed connection to the server.
	The test_task_2a executable script will handle that condition.
	
	Input Arguments:
	---
	None
	
	Returns:
	---
	`client_id` 	:  [ integer ]
		the client_id generated from start connection remote API, it should be stored in a global variable
	
	Example call:
	---
	client_id = init_remote_api_server()
	
	NOTE: This function will be automatically called by test_task_2a executable before starting the simulation.
	"""

	global client_id

	##############	ADD YOUR CODE HERE	##############
	sim.simxFinish(-1) # just in case, close all opened connections
	client_id = sim.simxStart('127.0.0.1',19997,True,True,5000,5) 
	
	
	##################################################

	return client_id


def start_simulation():

	"""
	Purpose:
	---
	This function should first start the simulation if the connection to server
	i.e. CoppeliaSim was successful and then wait for last command sent to arrive
	at CoppeliaSim server end.

	NOTE: In this Task, do not call the exit_remote_api_server function in case of failed connection to the server.
	The test_task_2a executable script will handle that condition.
	
	Input Arguments:
	---
	None
	
	Returns:
	---
	`return_code` 	:  [ integer ]
		the return code generated from the start running simulation remote API
	
	Example call:
	---
	return_code = start_simulation()
	
	NOTE: This function will be automatically called by test_task_2a executable at the start of simulation.
	"""

	global client_id

	return_code = 0

	##############	ADD YOUR CODE HERE	##############
	
	return_code = sim.simxStartSimulation(client_id,sim.simx_opmode_oneshot)
	'''return_code,pingtime = sim.simxGetPingTime(client_id)
	print(return_code,pingtime)'''
	

	#print(f"cmd time {return_code}")
	print(return_code)
	
	

	##################################################

	return return_code


def get_vision_sensor_image():
	
	"""
	Purpose:
	---
	This function should first get the handle of the Vision Sensor object from the scene.
	After that it should get the Vision Sensor's image array from the CoppeliaSim scene.

	Input Arguments:
	---
	None
	
	Returns:
	---
	`vision_sensor_image` 	:  [ list ]
		the image array returned from the get vision sensor image remote API
	`image_resolution` 		:  [ list ]
		the image resolution returned from the get vision sensor image remote API
	`return_code` 			:  [ integer ]
		the return code generated from the remote API
	
	Example call:
	---
	vision_sensor_image, image_resolution, return_code = get_vision_sensor_image()

	NOTE: This function will be automatically called by test_task_2a executable at regular intervals.
	"""

	global client_id
	global iteration

	vision_sensor_image = []
	image_resolution = []
	return_code = 0
	print("called")
	print(f"iteration{iteration}")
	iteration+=1

	##############	ADD YOUR CODE HERE	##############
	
	return_code,handel = sim.simxGetObjectHandle(client_id,"vision_sensor_1",sim.simx_opmode_blocking)
	time.sleep(2)
	
	
	# Now retrieve streaming data (i.e. in a non-blocking fashion):
	startTime = time.time()
	return_code ,image_resolution,vision_sensor_image =sim.simxGetVisionSensorImage(client_id,handel,0,sim.simx_opmode_streaming)# Initialize streaming
	while time.time()-startTime < 5:
		return_code ,image_resolution,vision_sensor_image =sim.simxGetVisionSensorImage(client_id,handel,0,sim.simx_opmode_streaming) # Try to retrieve the streamed data
		if return_code == sim.simx_return_ok : # After initialization of streaming, it will take a few ms before the first value arrives, so check the return code
			print ('resolution: ',image_resolution)
			#print(vision_sensor_image)
			break 
		time.sleep(0.005)
		
	
	
	
	
	
	

	##################################################

	return vision_sensor_image, image_resolution, return_code


def transform_vision_sensor_image(vision_sensor_image, image_resolution):
	

	"""
	Purpose:
	---
	This function should:
	1. First convert the vision_sensor_image list to a NumPy array with data-type as uint8.
	2. Since the image returned from Vision Sensor is in the form of a 1-D (one dimensional) array,
	the new NumPy array should then be resized to a 3-D (three dimensional) NumPy array.
	3. Change the color of the new image array from BGR to RGB.
	4. Flip the resultant image array about the X-axis.
	The resultant image NumPy array should be returned.
	
	Input Arguments:
	---
	`vision_sensor_image` 	:  [ list ]
		the image array returned from the get vision sensor image remote API
	`image_resolution` 		:  [ list ]
		the image resolution returned from the get vision sensor image remote API
	
	Returns:
	---
	`transformed_image` 	:  [ numpy array ]
		the resultant transformed image array after performing above 4 steps
	
	Example call:
	---
	transformed_image = transform_vision_sensor_image(vision_sensor_image, image_resolution)
	
	NOTE: This function will be automatically called by test_task_2a executable at regular intervals.
	"""

	transformed_image = None
	#print(vision_sensor_image)

	##############	ADD YOUR CODE HERE	##############
	# print(type(vision_sensor_image))
	vision_sensor_image  = np.array(vision_sensor_image,dtype= np.uint8)

	# print(type(vision_sensor_image))
	vision_sensor_image = np.reshape(vision_sensor_image,(1024,1024,3))
	# print(vision_sensor_image.shape)
	transformed_image= cv2.cvtColor(vision_sensor_image, cv2.COLOR_BGR2RGB)
	transformed_image = cv2.flip(transformed_image, 0)
	'''cv2.imshow('transformed image', transformed_image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
'''
	#task_1a_part1.show("name",transformed_image)

	

	
	

	##################################################
	
	return transformed_image


def stop_simulation():

	"""
	Purpose:
	---
	This function should stop the running simulation in CoppeliaSim server.

	NOTE: In this Task, do not call the exit_remote_api_server function in case of failed connection to the server.
	The test_task_2a executable script will handle that condition.
	
	Input Arguments:
	---
	None
	
	Returns:
	---
	`return_code` 	:  [ integer ]
		the return code generated from the stop running simulation remote API
	
	Example call:
	---
	return_code = stop_simulation()
	
	NOTE: This function will be automatically called by test_task_2a executable at the end of simulation.
	"""

	global client_id

	return_code = 0

	##############	ADD YOUR CODE HERE	##############
	
	return_code = sim.simxStopSimulation(client_id,sim.simx_opmode_oneshot)

	##################################################

	return return_code


def exit_remote_api_server():
	
	"""
	Purpose:
	---
	This function should wait for the last command sent to arrive at the Coppeliasim server
	before closing the connection and then end the communication thread with server
	i.e. CoppeliaSim using simxFinish Remote API.

	Input Arguments:
	---
	None
	
	Returns:
	---
	None
	
	Example call:
	---
	exit_remote_api_server()
	
	NOTE: This function will be automatically called by test_task_2a executable after ending the simulation.
	"""

	global client_id

	##############	ADD YOUR CODE HERE	##############
	sim.simxFinish(client_id)
	

	##################################################


# NOTE:	YOU ARE NOT ALLOWED TO MAKE ANY CHANGE TO THIS FUNCTION
# 
# Function Name:    main
#        Inputs:    None
#       Outputs:    None
#       Purpose:    This part of the code is only for testing your solution. The function does the following:
# 						- imports 'task_1b.py' file as module
# 						- imports 'task_1a_part1.py' file as module
# 						- calls init_remote_api_server() function to connect with CoppeliaSim Remote API server
# 						- then calls start_simulation() function to start the simulation
# 						- then calls get_vision_sensor_image() function to capture an image from the Vision Sensor in CoppeliaSim scene
# 						- then calls transform_vision_sensor_image() function to transform the captured image
# 						  to a format compatible with OpenCV
# 						- then the transformed image is given as input and Perspective Transform is applied
# 						  by calling applyPerspectiveTransform function	from 'task_1b'
# 						- lastly the output of warped_img is given to 'scan_image' function from 'task_1a_part1'
# 						- it then asks the user whether to quit the program or not, if 'q' or 'Q' is given as input,
# 						  then it will call stop_simulation to stop the simulation
# 						  and calls exit_remote_api_server function to disconnect from CoppeliaSim Remote API server.
# 
# NOTE: Write your solution ONLY in the space provided in the above functions.

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
		print('Your task_1b.py throwed an Exception, kindly debug your code!\n')
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
		print('Your task_1a_part1.py throwed an Exception, kindly debug your code!\n')
		traceback.print_exc(file=sys.stdout)
		sys.exit()

	# Initiate the Remote API connection with CoppeliaSim server
	print('\nConnection to CoppeliaSim Remote API Server initiated.')
	print('Trying to connect to Remote API Server...')

	i = 0 

	try:
		client_id = init_remote_api_server()

		if (client_id != -1):
			print('\nConnected successfully to Remote API Server in CoppeliaSim!')

			# Starting the Simulation
			try:
				return_code = start_simulation()

				if (return_code == sim.simx_return_novalue_flag):
					print('\nSimulation started correctly in CoppeliaSim.')

				else:
					print('\n[ERROR] Failed starting the simulation in CoppeliaSim!')
					print('start_simulation function is not configured correctly, check the code!')
					print()
					sys.exit()

			except Exception:
				print('\n[ERROR] Your start_simulation function throwed an Exception, kindly debug your code!')
				print('Stop the CoppeliaSim simulation manually.\n')
				traceback.print_exc(file=sys.stdout)
				print()
				sys.exit()
		
		else:
			print('\n[ERROR] Failed connecting to Remote API server!')
			print('[WARNING] Make sure the CoppeliaSim software is running and')
			print('[WARNING] Make sure the Port number for Remote API Server is set to 19997.')
			print('[ERROR] OR init_remote_api_server function is not configured correctly, check the code!')
			print()
			sys.exit()

	except Exception:
		print('\n[ERROR] Your init_remote_api_server function throwed an Exception, kindly debug your code!')
		print('Stop the CoppeliaSim simulation manually if started.\n')
		traceback.print_exc(file=sys.stdout)
		print()
		sys.exit()
	
	# Get image array and its resolution from Vision Sensor in ComppeliaSim scene
	try:
		vision_sensor_image, image_resolution, return_code = get_vision_sensor_image()

		if ((return_code == sim.simx_return_ok) and (len(image_resolution) == 2) and (len(vision_sensor_image) > 0)):
			print('\nImage captured from Vision Sensor in CoppeliaSim successfully!')

			# Get the transformed vision sensor image captured in correct format
			try:
				transformed_image = transform_vision_sensor_image(vision_sensor_image, image_resolution)

				if (type(transformed_image) is np.ndarray):

					cv2.imshow('transformed image', transformed_image)
					cv2.waitKey(0)
					cv2.destroyAllWindows()

					# Get the resultant warped transformed vision sensor image after applying Perspective Transform
					try:

						warped_img = task_1b.applyPerspectiveTransform(transformed_image)
						
						cv2.imshow('warped_img',warped_img)
						cv2.waitKey(0)
						cv2.destroyAllWindows()
						#cv.imwrite("Result\f"{i}",)
						
						if (type(warped_img) is np.ndarray):

							# Get the 'shapes' dictionary by passing the 'warped_img' to scan_image function
							try:
								shapes = task_1a_part1.scan_image(warped_img)

								if (type(shapes) is dict):
									print('\nShapes detected by Vision Sensor are: ')
									print(shapes)

									inp_char = input('\nEnter \'q\' or \'Q\' to quit the program: ')

									if (len(inp_char) == 1) and ((inp_char == 'q') or (inp_char == 'Q')):
										print('\nQuitting the program and stopping the simulation by calling stop_simulation and exit_remote_api_server functions.')

										# Ending the Simulation
										try:
											return_code = stop_simulation()
											
											if (return_code == sim.simx_return_novalue_flag):
												print('\nSimulation stopped correctly.')

												# Stop the Remote API connection with CoppeliaSim server
												try:
													exit_remote_api_server()

													if (start_simulation() == sim.simx_return_initialize_error_flag):
														print('\nDisconnected successfully from Remote API Server in CoppeliaSim!')

													else:
														print('\n[ERROR] Failed disconnecting from Remote API server!')
														print('[ERROR] exit_remote_api_server function is not configured correctly, check the code!')

												except Exception:
													print('\n[ERROR] Your exit_remote_api_server function throwed an Exception, kindly debug your code!')
													print('Stop the CoppeliaSim simulation manually.\n')
													traceback.print_exc(file=sys.stdout)
													print()
													sys.exit()
											
											else:
												print('\n[ERROR] Failed stopping the simulation in CoppeliaSim server!')
												print('[ERROR] stop_simulation function is not configured correctly, check the code!')
												print('Stop the CoppeliaSim simulation manually.')
											
											print()
											sys.exit()

										except Exception:
											print('\n[ERROR] Your stop_simulation function throwed an Exception, kindly debug your code!')
											print('Stop the CoppeliaSim simulation manually.\n')
											traceback.print_exc(file=sys.stdout)
											print()
											sys.exit()
									
									else:
										print('\n[WARNING] Kindly provide input of "q" or "Q" only!')
										print('Stop the CoppeliaSim simulation manually.')
										print()
										sys.exit()
								
								else:
									print('\n[ERROR] scan_image function returned a ' + str(type(shapes)) + ' instead of a dictionary.')
									print('Stop the CoppeliaSim simulation manually.')
									print()
									sys.exit()
							
							except Exception:
								print('\n[ERROR] Your scan_image function in task_1a_part1.py throwed an Exception, kindly debug your code!')
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
						print('\n[ERROR] Your applyPerspectiveTransform function in task_1b.py throwed an Exception, kindly debug your code!')
						print('Stop the CoppeliaSim simulation manually.\n')
						traceback.print_exc(file=sys.stdout)
						print()
						sys.exit()

				else:
					print('\n[ERROR] transform_vision_sensor_image function is not configured correctly, check the code.')
					print('Stop the CoppeliaSim simulation manually.')
					print()
					sys.exit()

			except Exception:
				print('\n[ERROR] Your transform_vision_sensor_image function throwed an Exception, kindly debug your code!')
				print('Stop the CoppeliaSim simulation manually.\n')
				traceback.print_exc(file=sys.stdout)
				print()
				sys.exit()

		else:
			print('\n[ERROR] get_vision_sensor function is not configured correctly, check the code.')
			print('Stop the CoppeliaSim simulation manually.')
			print()
			sys.exit()

	except Exception:
		print('\n[ERROR] Your get_vision_sensor_image function throwed an Exception, kindly debug your code!')
		print('Stop the CoppeliaSim simulation manually.\n')
		traceback.print_exc(file=sys.stdout)
		print()
		sys.exit()

