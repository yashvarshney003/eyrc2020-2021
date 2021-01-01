#this script increment/decrement in the value of the variables according to key pressed on the keyboard
# 			kp 		ki 		kd
# increment	q		w 		e
# decrement	a 		s 		d

import keyboard
import time

was_pressed = False
kp=0
ki=0
kd=0

while(1):
	print("Kp = ",kp,"    kd = ",kd,"    ki = ",ki)
	if keyboard.is_pressed('q'):
		if not was_pressed:
			kp = kp+1
			was_pressed = True
	elif keyboard.is_pressed('a'):
		if not was_pressed:
			kp = kp-1
			was_pressed = True

	elif keyboard.is_pressed('w'):
		if not was_pressed:
			kd = kd+1
			was_pressed = True
	elif keyboard.is_pressed('s'):
		if not was_pressed:
			kd = kd-1
			was_pressed = True

	elif keyboard.is_pressed('e'):
		if not was_pressed:
			ki = ki+1
			was_pressed = True
	elif keyboard.is_pressed('d'):
		if not was_pressed:
			ki = ki-1
			was_pressed = True

	else:
		was_pressed = False

