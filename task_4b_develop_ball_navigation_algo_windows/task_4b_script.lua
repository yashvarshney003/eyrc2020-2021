--[[
*****************************************************************************************
*
*        		===============================================
*           		Nirikshak Bot (NB) Theme (eYRC 2020-21)
*        		===============================================
*
*  This Lua script is to implement Task 4B of Nirikshak Bot (NB) Theme (eYRC 2020-21).
*  
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*  
*  e-Yantra - An MHRD project under National Mission on Education using ICT (NMEICT)
*
*****************************************************************************************
]]--


--[[
# Team ID:			[ Team-ID ]
# Author List:		[ Names of team members worked on this file separated by Comma: Name1, Name2, ... ]
# Filename:			task_4b_lua
# Functions:        [ Comma separated list of functions in this file ]
# Global variables:	
# 					[ List of global variables defined in this file ]
]]--

--[[
##################### GLOBAL VARIABLES #######################
## You can add global variables in this section according   ##
## to your requirement.                                     ##
## DO NOT TAMPER WITH THE ALREADY DEFINED GLOBAL VARIABLES. ##
##############################################################
]]--

base_children_list={} --Do not change or delete this variable
baseHandle = -1       --Do not change or delete this variable
--############################################################

--[[
##################### HELPER FUNCTIONS #######################
## You can add helper functions in this section according   ##
## to your requirement.                                     ##
## DO NOT MODIFY OR CHANGE THE ALREADY DEFINED HELPER       ##
## FUNCTIONS                                                ##
##############################################################
]]--

--[[
**************************************************************
  YOU ARE NOT ALLOWED TO MODIFY THIS FUNCTION
**************************************************************
	Function Name : createWall()
	Purpose:
	---
	Creates a black-colored wall of dimensions 90cm x 10cm x 10cm

	Input Arguments:
	---
	None
	
	Returns:
	---
	wallObjectHandle : number
	
	returns the object handle of the wall created
	
	Example call:
	---
	wallObjectHandle = createWall()
**************************************************************	
]]--
function createWall()
	wallObjectHandle = sim.createPureShape(0, 8, {0.09, 0.01, 0.1}, 0.0001, nil)
	--Refer https://www.coppeliarobotics.com/helpFiles/en/regularApi/simCreatePureShape.htm to understand the parameters passed to this function
	sim.setShapeColor(wallObjectHandle, nil, sim.colorcomponent_ambient_diffuse, {0, 0, 0})
	sim.setObjectInt32Parameter(wallObjectHandle,sim.shapeintparam_respondable_mask,65280)
	--Refer https://www.coppeliarobotics.com/helpFiles/en/apiFunctions.htm#sim.setObjectInt32Parameter to understand the various parameters passed. 	
	--The walls should only be collidable with the ball and not with each other.
	--Hence we are enabling only the local respondable masks of the walls created.
	sim.setObjectSpecialProperty(wallObjectHandle, sim.objectspecialproperty_collidable)
	--Walls may have to be set as renderable........................... 
	--This is required to make the wall as collidable
	return wallObjectHandle
end

--############################################################

--[[
**************************************************************
	Function Name : receiveData()
	Purpose:
	---
	Receives data via Remote API. This function is called by 
	simx.callScriptFunction() in the python code (task_2b.py)

	Input Arguments:
	---
	inInts : Table of Ints
	inFloats : Table of Floats
	inStrings : Table of Strings
	inBuffer : string
	
	Returns:
	---
	inInts : Table of Ints
	inFloats : Table of Floats
	inStrings : Table of Strings
	inBuffer : string
	
	These 4 variables represent the data being passed from remote
	API client(python) to the CoppeliaSim scene
	
	Example call:
	---
	Shall be called from the python script
**************************************************************	
]]--
function receiveData(inInts,inFloats,inStrings,inBuffer)

	--*******************************************************
	--               ADD YOUR CODE HERE
    x = 1
    for i=0,9 do
        maze_array[i] = {}
        for j=0,9 do
            maze_array[i][j] = inInts[x]    -- storing data as 2D array indexing start from 00
            x = x+1
        end
    end
	--*******************************************************
	return inInts, inFloats, inStrings, inBuffer
end

--[[
**************************************************************
	Function Name : generateHorizontalWalls()
	Purpose:
	---
	Generates all the Horizontal Walls in the scene.

	Input Arguments:
	---
	None
	
	Returns:
	---
	None
	
	Example call:
	---
	generateHorizontalWalls()
**************************************************************	
]]--
function generateHorizontalWalls()

	--*******************************************************
	--               ADD YOUR CODE HERE
    x = -0.45
    y = 0.5
    z = 0.37087 --0.065
    for i=1,11 do
        for j=1,10 do
            position = {x,y,z}
            orientation = {0,0,0}
            wallObjectHandle = createWall()
            wall_name = "H_WallSegment_" .. (i-1) .. "x" .. (j-1)   -- wall name indexing starting from 00
            sim.setObjectName(wallObjectHandle,wall_name)
            sim.setObjectPosition(wallObjectHandle,sim.handle_parent,position)  -- setting wall at desired position
            sim.setObjectOrientation(wallObjectHandle,sim.handle_parent,orientation)    --setting wall desired orientation
            x = x + 0.1
        end
        y = y - 0.1
        x = -0.45
    end
	--*******************************************************
end

--[[
**************************************************************
	Function Name : generateVerticalWalls()
	Purpose:
	---
	Generates all the Vertical Walls in the scene.

	Input Arguments:
	---
	None
	
	Returns:
	---
	None
	
	Example call:
	---
	generateVerticalWalls()
**************************************************************	
]]--
function generateVerticalWalls()

	--*******************************************************
	--               ADD YOUR CODE HERE
    x = -0.5
    y = 0.45
    z = 0.37087 -- 0.065
    for i=1,11 do
        for j=1,10 do
            position = {x,y,z}
            orientation = {0,0,math.pi/2}
            wallObjectHandle = createWall()
            wall_name = "V_WallSegment_" .. (j-1) .. "x" .. (i-1)
            sim.setObjectName(wallObjectHandle,wall_name)
            sim.setObjectPosition(wallObjectHandle,sim.handle_parent,position)
            sim.setObjectOrientation(wallObjectHandle,sim.handle_parent,orientation)
            y = y - 0.1
        end
        x = x + 0.1
        y = 0.45
    end

	--*******************************************************
end

--[[
**************************************************************
	Function Name : deleteWalls()
	Purpose:
	---
	Deletes all the grouped walls in the given scene

	Input Arguments:
	---
	None
	
	Returns:
	---
	None
	
	Example call:
	---
	deleteWalls()
**************************************************************	
]]--
function deleteWalls()

	--*******************************************************
	--               ADD YOUR CODE HERE

    local savedState=sim.getInt32Parameter(sim.intparam_error_report_mode)  
    sim.setInt32Parameter(sim.intparam_error_report_mode,0)                 --desabling error report mode (considering the case of empty maze)
    sim.removeObject(wallsGroupHandle)      								--deleting horizontal wall
    sim.setInt32Parameter(sim.intparam_error_report_mode,savedState)        -- enabling error report mode
	--*******************************************************
end


--[[
**************************************************************
  YOU CAN DEFINE YOUR OWN INPUT AND OUTPUT PARAMETERS FOR THIS
						  FUNCTION
**************************************************************
	Function Name : createMaze()
	Purpose:
	---
	Creates the maze in the given scene by deleting specific 
	horizontal and vertical walls

	Input Arguments:
	---
	None
	
	Returns:
	---
	None
	
	Example call:
	---
	createMaze()
**************************************************************	
]]--
function createMaze()
	
	--*******************************************************
	--               ADD YOUR CODE HERE
    for x=0,9 do
        for y=0,9 do
            n = maze_array[x][y]        --generating binary number corresponding to the cell xy data
            binary=""
            if (n==0) then
                binary="0000"
            else
                if (n==1) then
                    binary="0001"
                else
                    for i=1,4 do
                        if (n==1) then
                            binary=binary .. 1
                            n=n-1
                        elseif (n==0) then
                            binary=binary .. 0
                        else
                            if (n%2==1) then
                                binary=binary .. (n%2)
                                n=n-1
                                n=n/2
                            elseif (n%2==0) then
                                binary=binary .. (n%2)
                                n=n/2
                            else
                                print("*** Unexpected ERROR in binary generation ***")
                            end
                        end
                    end
                    binary=string.reverse(binary)       -- binary data generated
                end
            end
            
            for i=1,4 do
              num=binary:sub(i,i)   -- reading binary string letter by letter
              num=tonumber(num)
              --SENW
              --cell number(x,y)
              wall_Handle = -1
              
              local savedState=sim.getInt32Parameter(sim.intparam_error_report_mode)
              sim.setInt32Parameter(sim.intparam_error_report_mode,0)
              if (i==1 and num ==0) then
                --South wall
                wall_Name = "H_WallSegment_" .. (x+1) .. "x" .. y
                wall_Handle=sim.getObjectHandle(wall_Name)
              elseif (i==2 and num ==0) then
                --East wall
                wall_Name = "V_WallSegment_" .. x .. "x" .. (y+1)
                wall_Handle=sim.getObjectHandle(wall_Name)
              elseif (i==3 and num ==0) then
                --North wall
                wall_Name = "H_WallSegment_" .. x .. "x" .. y
                wall_Handle=sim.getObjectHandle(wall_Name)
              elseif (i==4 and num ==0) then
                --West wall
                wall_Name = "V_WallSegment_" .. x .. "x" .. y
                wall_Handle=sim.getObjectHandle(wall_Name)
              else
                    --no wall delete case
              end
              sim.setInt32Parameter(sim.intparam_error_report_mode,savedState)
              if (wall_Handle > 0) then
                objectName=sim.getObjectName(wall_Handle)
                sim.removeObject(wall_Handle)
              end
            end
        end
    end
    print("Maze successfully created")
    print("Maze creating function bypassed.")
	--*******************************************************
end
--[[
	Function Name : groupWalls()
	Purpose:
	---
	Groups the various walls in the scene to one object.
	The name of the new grouped object should be set as 'walls_1'.

	Input Arguments:
	---
	None
	
	Returns:
	---
	None
	
	Example call:
	---
	groupWalls()
**************************************************************	
]]--

function groupWalls()
	--*******************************************************
	--               ADD YOUR CODE HERE
    
    wall_handles={}
    for i=1,11 do
        for j=1,10 do
            objectName_horizontal = "H_WallSegment_" .. (i-1) .. "x" .. (j-1)
            objectHandle_horizontal = 1
            objectName_vertical = "V_WallSegment_" .. (j-1) .. "x" .. (i-1)
            objectHandle_vertical = 1
            local savedState=sim.getInt32Parameter(sim.intparam_error_report_mode)  
            sim.setInt32Parameter(sim.intparam_error_report_mode,0)                 --desabling error report mode    
            objectHandle_horizontal = sim.getObjectHandle(objectName_horizontal)
            objectHandle_vertical = sim.getObjectHandle(objectName_vertical)
            if objectHandle_horizontal > 0 then
                wall_handles[table.maxn(wall_handles)+1] = objectHandle_horizontal    -- storing horizontal wall handle in the end
            end
            if objectHandle_vertical > 0 then
               wall_handles[table.maxn(wall_handles)+1] = objectHandle_vertical         --deleting vertical wall
            end
        end
    end
    force_sensor_pw_1_handle =sim.getObjectHandle("force_sensor_pw_1")

    wallsGroupHandle = sim.groupShapes(wall_handles,false) 
    sim.setObjectName(wallsGroupHandle,"walls_1")
    sim.setObjectParent(wallsGroupHandle,force_sensor_pw_1_handle,true)
   	sim.setInt32Parameter(sim.intparam_error_report_mode,savedState)        -- enabling error report mode (enabling in the end considering blank maze case)
    print("walls grouped successfully")
	--*******************************************************
end

--[[
	Function Name : addToCollection()
	Purpose:
	---
	Adds the 'walls_1' grouped object to the collection 'colliding_objects'.  

	Input Arguments:
	---
	None
	
	Returns:
	---
	None
	
	Example call:
	---
	addToCollection()
**************************************************************	
]]--

function addToCollection()
	--*******************************************************
	--               ADD YOUR CODE HERE
	collectionHandle=sim.getCollectionHandle("colliding_objects")
	sim.addObjectToCollection(collectionHandle,wallsGroupHandle,sim_handle_single,0)
	print("walls_1 added to the collection")
	--*******************************************************
end

--[[
	******************************************************************************
			YOU ARE ALLOWED TO MODIFY THIS FUNCTION DEPENDING ON YOUR PATH. 
	******************************************************************************
	Function Name : drawPath(inInts,path,inStrings,inBuffer)
	Purpose:
	---
	Builds blue coloured lines in the scene according to the
	path generated from the python file. 

	Input Arguments:
	---
	inInts : Table of Ints
	inFloats : Table of Floats (containing the path generated)
	inStrings : Table of Strings
	inBuffer : string
	
	Returns:
	---
	inInts : Table of Ints
	inFloats : Table of Floats
	inStrings : Table of Strings
	inBuffer : string
	
	Example call:
	---
	Shall be called from the python script
**************************************************************	
]]--
function drawPath(inInts,path,inStrings,inBuffer)
	posTable=sim.getObjectPosition(wallsGroupHandle,-1)
	print('=========================================')
	print('Path received is as follows: ')
	print(path)
	if not lineContainer then
		_lineContainer=sim.addDrawingObject(sim.drawing_lines,1,0,wallsGroupHandle,99999,{0.2,0.2,1})
		sim.addDrawingObjectItem(_lineContainer,nil)
		if path then
			local pc=#path/2
			for i=1,pc-1,1 do
				lineDat={path[(i-1)*2+1],path[(i-1)*2+2],posTable[3]-0.03,path[(i)*2+1],path[(i)*2+2],posTable[3]-0.03}
				sim.addDrawingObjectItem(_lineContainer,lineDat)
			end
		end
	end
	return inInts, path, inStrings, inBuffer
end

--[[
**************************************************************
	Function Name : sysCall_init()
	Purpose:
	---
	Can be used for initialization of parameters
	
	Input Arguments:
	---
	None
	
	Returns:
	---
	None
	
	Example call:
	---
	N/A
**************************************************************	
]]--
function sysCall_init()
	--*******************************************************
	--               ADD YOUR CODE HERE
 
	--*******************************************************
end

--[[
**************************************************************
		YOU ARE NOT ALLOWED TO MODIFY THIS FUNCTION.
		YOU CAN DEFINE YOUR OWN INPUT AND OUTPUT 
		PARAMETERS ONLY FOR CREATEMAZE() FUNCTION
**************************************************************
	Function Name : sysCall_beforeSimulation()
	Purpose:
	---
	This is executed before simulation starts
	
	Input Arguments:
	---
	None
	
	Returns:
	---
	None
	
	Example call:
	---
	N/A
**************************************************************	
]]--
function sysCall_beforeSimulation()
	
	generateHorizontalWalls()
	generateVerticalWalls()
	createMaze()--You can define your own input and output parameters only for this function
	groupWalls()
	addToCollection()
end

--[[
**************************************************************
		YOU ARE NOT ALLOWED TO MODIFY THIS FUNCTION. 
**************************************************************
	Function Name : sysCall_afterSimulation()
	Purpose:
	---
	This is executed after simulation ends
	
	Input Arguments:
	---
	None
	
	Returns:
	---
	None
	
	Example call:
	---
	N/A
**************************************************************	
]]--
function sysCall_afterSimulation()
	-- is executed after a simulation ends
	deleteWalls()
    evaluation_screen_respondable=sim.getObjectHandle('evaluation_screen_respondable@silentError')
    if(evaluation_screen_respondable~=-1) then
        sim.removeModel(evaluation_screen_respondable)
    end
end

function sysCall_cleanup()
	-- do some clean-up here
end

-- See the user manual or the available code snippets for additional callback functions and details