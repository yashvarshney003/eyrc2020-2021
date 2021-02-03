import numpy as np
import cv2
import os, sys
import traceback
import time
import math
import json
import multiprocessing
import sim
import task_2a
client_id = task_2a.init_remote_api_server()
return_code = sim.simxStartSimulation(client_id,sim.simx_opmode_oneshot)
print(sim.simxGetPingTime(client_id))
i =1;
while(i< 20):
    i+=1
    rt_code, prev_time = sim.simxGetStringSignal(client_id,'time',sim.simx_opmode_streaming)
    print(prev_time)
    rt_code,current_time =sim.simxGetStringSignal(client_id,'time',sim.simx_opmode_buffer)
    print(current_time)

