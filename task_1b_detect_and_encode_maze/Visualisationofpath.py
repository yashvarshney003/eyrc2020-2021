import cv2 
import numpy as np
import time


def find_path(maze_data,initial_pos, final_pos):
	k=0
	walls=[]
	children_list=[]

	
	prev_parent=(-1,-1) #iniitial parent so that console did not move to its parent.
	alternative=[] #to save the parent index and alternative path or alternative children

	all_paths=[]

	path=[]

	

	neighbours = {}
	for i in range (0,10):
		for j in range (0,10):
			digit = bin(maze_data[i][j]).replace("0b","")
			for z in range(4-len(digit)):
				digit = "0"+digit
			#print(f"binary is {i} and {j} {digit}")
			list_of_neighbours = []
			if(digit[0]=='0'):
				#print("here")
				
				list_of_neighbours.append((i+1,j))
				#print(list_of_neighbours)
			if(digit[1]=='0'):

				
				list_of_neighbours.append((i,j+1))
				#print(list_of_neighbours)
			if(digit[2]== '0' ):
				
				list_of_neighbours.append((i-1,j))
				#print(list_of_neighbours)
			if(digit[3]=='0'):
				
				list_of_neighbours.append((i,j-1))
				#print(list_of_neighbours)
			tup = (i,j) 
			
			neighbours[tup] = list_of_neighbours
	print(neighbours)

	path = [(initial_pos[0],initial_pos[1])]
	shortest_path = None
	parent = (-1,-1)
	while(path):
		print(f"path is {path}")

		parent = path[-1]
		#print(f"parent is {parent}")
		if(parent[0]==final_pos[0] and parent[1]==final_pos[1]):
			print("find the path")
			if(shortest_path is None):
				shortest_path = []

				
				path1 = path.copy()
				shortest_path.append(path1)
			else:
							
					path1 = path.copy()
					shortest_path.append(path1)
				
			element = path.pop()
			print(f"element popped off{element}")

		else:
			print(f"parent is  {parent}")
			print(f"number is {maze_data[parent[0]][parent[1]]}")
			print(neighbours)
			print(neighbours[parent])
			if(len(neighbours[parent]) >0 ):

				while(len(neighbours[parent]) > 0):
					print(f"list are of{parent} are  {neighbours[parent]}")
				
					if(neighbours[parent][0] not in path):
						print(f"element inserted{neighbours[parent][0]}")
						
						
						path.append(neighbours[parent][0])
						neighbours[parent].pop(0)
						print(f"element inserted after insertion{neighbours[parent]}")
						break
					else:
						neighbours[parent].pop(0)
				else:
					path.pop()
			else:
				path.pop()
				print(f"list is now {neighbours[parent]}")
		print("----------------------")
	print(shortest_path)
	last_path = None
	if(shortest_path):
		for i in shortest_path:
			print(f"path iss-----------------{i}")
			if(last_path is None):
				last_path = i
			else:
				if(len(last_path) > len(i)):
					last_path = i
		
	print("9999999999999999999999999999999900000000000000000000000000000---------------------")	
	return last_path	
def convert_path_to_pixels(path):
	
	resolution_x = 1240
	
	resolution_y = 1240
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
	return pixel_path

def show_path(img,pixel_list):
	img = cv.resize(img,(1240,1240))
	pixel_path=[]
	for i in range(0,len(pixel_list)):
		tup=(0,0)
		temp=pixel_list[i]
		tup=(temp[1],temp[0])
		pixel_path.append(tup)
	for i in range(0,(len(pixel_path)-1)):
	#print("drawing line")
		img = cv.line(img, pixel_path[i], pixel_path[i+1], (0,255,0), 9) 

	for i in range(0,len(pixel_path)):
		center=pixel_path[i]
		img = cv.circle(img, center, 3, (255,0,0), -1)
	return img
def draw_starting_end_point(img,start_coord,end_coord):
	img = cv.circle(img, start_coord, 5, (0,0,255), -1)
	img = cv.circle(img,end_coord, 5, (0,255,255), -1)
	return img

if __name__ == "__main__":
	import task_1b
	start_coord = (0,0)
	end_coord = (9,9)
	input_img = cv.imread("test_cases/maze01.jpg",1)
	input_shape = input_img.shape
	
	warped_img = task_1b.applyPerspectiveTransform(input_img)
	print(warped_img.size)
	
	encoded_maze = task_1b.detectMaze(warped_img)
	print(f"encoded maze {encoded_maze}")
	path = find_path(encoded_maze,start_coord,end_coord)
	print(path)
	pixel_path = convert_path_to_pixels(path)
	draw_path_image = show_path(warped_img,pixel_path)
	draw_path_image = draw_starting_end_point(draw_path_image,start_coord,end_coord)
	draw_path_image = cv.resize(draw_path_image,(400,400))
	cv.imshow("output_image",draw_path_image)
	cv.waitKey(5000)
	cv.destroyAllWindows()

		
