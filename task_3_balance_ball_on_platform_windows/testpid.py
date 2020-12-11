import sim
import math
import time
import os, sys
import traceback

def control_logic(x,y):

	global setpoint, client_id
	setpoint = [0,0]
	print("1")

	perror = [0,0] #for x and y error values initialization
	derror = [0,0]
	ierror = [0,0]
	prev_error = [0,0]
	prev_time = time.time()
	sample_time = 0.001 #set accordingly
	kp = [1,1]
	kd = [0,0]
	ki = [0,0]

	x_limit = [-90,90] # min limit and maximum limit in degrees
	y_limit = [-90,90]

	trim = [0,0] # if any trimming in angles is required

	start_time = time.time()

	returnCode, servohandle1=sim.simxGetObjectHandle(clientID,"joint_x", sim.simx_opmode_blocking)
	returnCode, servohandle2=sim.simxGetObjectHandle(clientID,"joint_y", sim.simx_opmode_blocking)
	returnCode, ballhandle=sim.simxGetObjectHandle(clientID,"green_ball_1",sim.simx_opmode_blocking)
	returnCode,position=sim.simxGetObjectPosition(clientID,ballhandle,-1,sim.simx_opmode_streaming)

	while(1):
		returnCode,position=sim.simxGetObjectPosition(clientID,ballhandle,-1,sim.simx_opmode_buffer)
		#print("ball position :",position,"    ------->  ",(time.time()-start_time))
		
		center_x = position[0] #positions of the ball
		center_y = position[1]

		current_time = time.time()
		dt = current_time - prev_time

		if (dt >= sample_time): # code is running for a sample time

			perror[0] = setpoint[0]-center_x
			perror[1] = setpoint[1]-center_y

			derror[0] = (perror[0] - prev_error[0])/dt
			derror[1] = (perror[1] - prev_error[1])/dt

			ierror[0] = ierror[0] + perror[0]
			ierror[1] = ierror[1] + perror[1]
			
			angle_x = (kp[0]*perror[0]) + (kd[0]*derror[0]) + (ki[0]*ierror[0]*dt)
			angle_y = (kp[1]*perror[1]) + (kd[1]*derror[1]) + (ki[1]*ierror[1]*dt)

			angle_x = angle_x + trim[0] #if any trim required
			angle_y = angle_y + trim[1]

			#limiting maximum and minimum values of the output angle in degrees
			if (angle_x < x_limit[0]):
				angle_x = x_limit[0]

			if (angle_x > x_limit[1]):
				angle_x = x_limit[1]
			
			if (angle_y < y_limit[0]):
				angle_y = y_limit[0]

			if (angle_y < y_limit[1]):
				angle_y = y_limit[1]

			angle_x = (angle_x*math.pi)/180		#converting into radian  ("we are NOT ALLOWED TO INCLUDE MATH")
			angle_y = (angle_y*math.pi)/180
			#print("x axis",angle_x)
			#send command to coppeliasim to rotate servo fin by simxsetjointtargetposition function try using simxopmodestreaming opmode
			returnCode=sim.simxSetJointTargetPosition(clientID,servohandle1,angle_x,sim.simx_opmode_streaming)
			returnCode=sim.simxSetJointTargetPosition(clientID,servohandle2,angle_y,sim.simx_opmode_streaming)

			prev_error[0] = perror[0]
			prev_error[1] = perror[1]
			prev_time=current_time

		if (current_time - start_time >= 10):
			break

if __name__ == "__main__":
	print("2")
	try:
	    import sim
	except:
	    print ('--------------------------------------------------------------')
	    print ('"sim.py" could not be imported. This means very probably that')
	    print ('either "sim.py" or the remoteApi library could not be found.')
	    print ('Make sure both are in the same folder as this file,')
	    print ('or appropriately adjust the file "sim.py"')
	    print ('--------------------------------------------------------------')
	    print ('')

	import time

	print ('Program started')
	sim.simxFinish(-1) # just in case, close all opened connections
	clientID=sim.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to CoppeliaSim
	if clientID!=-1:
	    print ('Connected to remote API server')

	    control_logic(1,2)
	    returnCode=sim.simxStopSimulation(clientID,sim.simx_opmode_oneshot)
	    sim.simxGetPingTime(clientID)
	    sim.simxFinish(clientID)
	else:
	    print ('Failed connecting to remote API server')
	print ('Program ended')
