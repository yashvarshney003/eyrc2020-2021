import time
start_time=time.time()
#data input
#for snapshot image given in documentation (0,0) to (6,9)
#input_data=[11,2,6,3,2,10,10,6,3,6,3,4,13,5,5,11,10,8,12,5,5,5,3,12,5,3,10,10,6,5,5,13,5,3,12,9,6,3,12,13,5,3,12,9,10,10,12,9,10,6,5,9,10,10,6,3,6,3,6,5,1,6,3,10,12,5,9,12,5,13,5,5,5,11,10,4,3,6,5,7,5,5,9,10,6,5,5,9,12,5,13,9,10,10,8,12,9,10,10,12] #it is nothing but the encoded maze data.
#for maze00 in task_1b (0,0) to (8,4)
input_data=[7, 3, 10, 10, 6, 3, 10, 6, 3, 6, 1, 12, 3, 10, 12, 5, 7, 9, 12, 5, 1, 14, 9, 6, 7, 5, 9, 10, 6, 5, 5, 3, 6, 5, 5, 9, 6, 3, 12, 5, 5, 5, 9, 12, 1, 14, 9, 4, 3, 4, 5, 9, 6, 7, 1, 10, 10, 12, 5, 13,9, 6, 5, 1, 8,10, 10, 14, 9, 6, 7, 5, 5, 9, 6, 3, 6, 3, 6, 5, 5, 5, 9, 14, 13, 5, 9, 12, 5, 5, 9, 8, 10, 10, 10, 12, 11, 10, 8, 12]
maze_data=[[0 for i in range(10)]for j in range(10)] #encoded maze data in 2D
k=0
walls=[]
children_list=[]

initial_pos=[8,4]
final_pos=[0,0]#[6,9]
prev_parent=(-1,-1) #iniitial parent so that console did not move to its parent.
alternative=[] #to save the parent index and alternative path or alternative children

path=[]

for i in range (0,10):
	for j in range (0,10):
		maze_data[i][j] = input_data[k]
		k=k+1

for i in range(0,10): #to check wether generated 2d maze is correct or not
	print("maze_data =",maze_data[i])

time.sleep(2)

#start with data of the initial point let this block as parent
i=initial_pos[0] #number of rows
j=initial_pos[1] #number of columns

while(1):
	if ((i==final_pos[0]) and j==final_pos[1]):
		path.append((i,j))
		print("Maze solved successfully")
		print("PATH :")
		print(path)
		break

	n = maze_data[i][j]	
	number = n	
	#convert celll data to binary, since data is not greater then 16 so we need only such algo which generates only 4 digit binary number
	# for converting number to binary we can use this method or the previous method done in task0 in which aman made script to convert binary using recursive algorithem
	binary = []#this stores the binary form of the cell data
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
			binary.reverse()
	print(number,"-->",binary)
	#binary = int(binary) #i think no need to change in integer if conditions can easily be compared with the string format

	for l in range(0,4):
		bit = binary[l]
		#south east north west


		# i don't think we need this logic it was written to check another logic
		# if bit == '1': 
		# 	walls[l]=False #False means wall is present and path is blocked
		# else:
		# 	walls[l]=True # True means wall is not present and path is open



		if (bit==0): #means there is no wall
			if i<9: #for south boyndary condition
				if l==0: #south block
					distance=((final_pos[0]-(i+1))**2)+((final_pos[1]-(i))**2) #distance of the block to the target in this step for priority by assuming i,j indexing as x,y co-ordinates
					children=(distance,i+1,j,i,j)	#(distance between the child block and target block(i+1,j),index of child block,index of parent block(i,j))
			if j<9: #for east boundary condition
				if l==1: #east block
					distance=((final_pos[0]-(i+1))**2)+((final_pos[1]-(i))**2)
					children=(distance,i,j+1,i,j)
			if i>0: #for north boundary condition
				if l==2: #north block
					distance=((final_pos[0]-(i+1))**2)+((final_pos[1]-(i))**2)
					children=(distance,i-1,j,i,j)
			if j>0: #for south boundary condition
				if l==3: #south block
					distance=((final_pos[0]-(i+1))**2)+((final_pos[1]-(i))**2)
					children=(distance,i,j-1,i,j)
			#************************************************************************
			if ((children[1]!=prev_parent[0]) or (children[2]!=prev_parent[1])): #if children is not the previous parent then append the children
				children_list.append(children)
			#************************************************************************
	


	children_list.sort(reverse=True) #sorting the list on the basis of distance in descending order
	prev_parent=(i,j)
	##############################################
	path.append(prev_parent)
	##############################################
	if(len(children_list)>0):
		next_parent=children_list.pop()
		i=next_parent[1]
		j=next_parent[2]
		if(len(children_list)>0): #then strore them in alternative
			for a in range(0,len(children_list)):
				alternative.append(children_list[a])
				children_list=[]
	else:
		#pop from the alternative
		next_parent=alternative.pop()
		i=next_parent[1]
		j=next_parent[2]
		prev_parent=(next_parent[3],next_parent[4])
		#i need to delete some elements of path here to delete all the wrong cells untill the we get the altenative parent.
		while ((path[len(path)-1][0]!= prev_parent[0]) or (path[len(path)-1][1]!= prev_parent[1])):
			popped_element=path.pop()
			print("popped_element =",popped_element)
	#now here we have to find the child or successor of the parent



###############################################################################################
print("time taken by the code including delay = ",time.time()-start_time)
print("time taken only by the code logic =",time.time()-start_time-2)

show_path=[['#' for i in range(10)]for j in range(10)]

#storing path in 2d format
prev_temp=(-1,-1)
for k in range(0,len(path)):
	temp=path[k]
	if ((temp[0]==prev_temp[0]+1) or (temp[0]==prev_temp[0]-1)):
		show_path[temp[0]][temp[1]]='l'
	if ((temp[1]==prev_temp[1]+1) or (temp[1]==prev_temp[1]-1)):
		show_path[temp[0]][temp[1]]='-'
	prev_temp=temp
	k=k+1
#displaying path in 2d format
print("")
print("Generated Path in maze :")
for i in range(0,10):
	print(show_path[i])
