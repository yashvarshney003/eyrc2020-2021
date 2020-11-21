--[[
*****************************************************************************************
*
*               ===============================================
*                   Nirikshak Bot (NB) Theme (eYRC 2020-21)
*               ===============================================
*
*  This Lua script is to implement Task 2B of Nirikshak Bot (NB) Theme (eYRC 2020-21).
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
# Team ID:          NB_2139
# Author List:      Anurag Saxena, Yash Varshney
# Filename:         task_2b
# Functions:        createWall, saveTexture, retrieveTexture, reapplyTexture, receiveData, generateHorizontalWalls, 
#                   generateVerticalWalls, deleteWalls, createMaze, sysCall_init, sysCall_beforeSimulation
#                   sysCall_afterSimulation, sysCall_cleanup
#                   [ Comma separated list of functions in this file ]
# Global variables: 
#                   [ List of global variables defined in this file ]
]]--

--[[
##################### GLOBAL VARIABLES #######################
## You can add global variables in this section according   ##
## to your requirement.                                     ##
## DO NOT TAMPER WITH THE ALREADY DEFINED GLOBAL VARIABLES. ##
##############################################################
]]--

maze_array = {}
baseHandle = -1       --Do not change or delete this variable
textureID = -1        --Do not change or delete this variable
textureData = -1       --Do not change or delete this variable
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
    
    returns the object handle of the created wall
    
    Example call:
    ---
    wallObjectHandle = createWall()
**************************************************************  
]]--
function createWall()
    wallObjectHandle = sim.createPureShape(0, 26, {0.09, 0.01, 0.1}, 0, nil)
    sim.setShapeColor(wallObjectHandle, nil, sim.colorcomponent_ambient_diffuse, {0, 0, 0})
    sim.setObjectSpecialProperty(wallObjectHandle, sim.objectspecialproperty_collidable)
    sim.setObjectSpecialProperty(wallObjectHandle, sim.objectspecialproperty_measurable)
    sim.setObjectSpecialProperty(wallObjectHandle, sim.objectspecialproperty_detectable_all)
    sim.setObjectSpecialProperty(wallObjectHandle, sim.objectspecialproperty_renderable)
    return wallObjectHandle
end

--[[
**************************************************************
  YOU ARE NOT ALLOWED TO MODIFY OR CALL THIS HELPER FUNCTION
**************************************************************
    Function Name : saveTexture()
    Purpose:
    ---
    Reads and initializes the applied texture to Base object
    and saves it to a file.
    Input Arguments:
    ---
    None
    
    Returns:
    ---
    None
    
    Example call:
    ---
    saveTexture()
**************************************************************  
]]--
function saveTexture()
    baseHandle = sim.getObjectHandle("Base")
    textureID = sim.getShapeTextureId(baseHandle)
    textureData=sim.readTexture(textureID ,0,0,0,0,0)
    sim.saveImage(textureData, {512,512}, 0, "models/other/base_template.png", -1)
end
--[[
**************************************************************
  YOU ARE NOT ALLOWED TO MODIFY OR CALL THIS HELPER FUNCTION
**************************************************************
    Function Name : retrieveTexture()
    Purpose:
    ---
    Loads texture from file.
    Input Arguments:
    ---
    None
    
    Returns:
    ---
    None
    
    Example call:
    ---
    retrieveTexture()
**************************************************************  
]]--
function retrieveTexture()
    textureData, resolution = sim.loadImage(0, "models/other/base_template.png") 
end

--[[
**************************************************************
  YOU ARE NOT ALLOWED TO MODIFY OR CALL THIS HELPER FUNCTION
**************************************************************
    Function Name : reapplyTexture()
    Purpose:
    ---
    Re-applies texture to Base object
    Input Arguments:
    ---
    None
    
    Returns:
    ---
    None
    
    Example call:
    ---
    reapplyTexture()
**************************************************************  
]]--
function reapplyTexture()
    plane, textureID = sim.createTexture("", 0, nil, {1.01, 1.01}, nil, 0, {512, 512})
    sim.writeTexture(textureID, 0, textureData, 0, 0, 0, 0, 0)
    sim.setShapeTexture(baseHandle, textureID, sim.texturemap_plane, 0, {1.01, 1.01},nil,nil)
    sim.removeObject(plane)
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
    N/A
    
    Hint:
    ---
    You might want to study this link to understand simx.callScriptFunction()
    better 
    https://www.coppeliarobotics.com/helpFiles/en/remoteApiExtension.htm
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
    z = 0.065
    for i=1,11 do
        for j=1,10 do
            position = {x,y,z}
            orientation = {0,0,0}
            wallObjectHandle = createWall()
            sim.setObjectParent(wallObjectHandle,baseHandle,true)   -- making generated wall child of Base
            wall_name = "H_WallSegment_" .. (i-1) .. "x" .. (j-1)   -- wall name indexing starting from 00
            sim.setObjectName(wallObjectHandle,wall_name)
            sim.setObjectPosition(wallObjectHandle,sim_handle_parent,position)  -- setting wall at desired position
            sim.setObjectOrientation(wallObjectHandle,sim_handle_parent,orientation)    --setting wall desired orientation
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
    z = 0.065
    for i=1,11 do
        for j=1,10 do
            position = {x,y,z}
            orientation = {0,0,math.pi/2}
            wallObjectHandle = createWall()
            sim.setObjectParent(wallObjectHandle,baseHandle,true)
            wall_name = "V_WallSegment_" .. (j-1) .. "x" .. (i-1)
            sim.setObjectName(wallObjectHandle,wall_name)
            sim.setObjectPosition(wallObjectHandle,sim_handle_parent,position)
            sim.setObjectOrientation(wallObjectHandle,sim_handle_parent,orientation)
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
    Deletes all the walls in the given scene
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
            sim.setInt32Parameter(sim.intparam_error_report_mode,savedState)        -- enabling error report mode
            if objectHandle_horizontal > 0 then
                sim.removeObject(objectHandle_horizontal)      --deleting horizontal wall
            end
            if objectHandle_vertical > 0 then
                sim.removeObject(objectHandle_vertical)         --deleting vertical wall
            end
        end
    end
       
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
        
    --*******************************************************
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

    if pcall(saveTexture) then -- Do not delete or modify this section
        print("Successfully saved texture")
    else
        print("Texture does not exist. Importing texture from file..")
        retrieveTexture()
        reapplyTexture()
    end     
end

--[[
**************************************************************
        YOU ARE NOT ALLOWED TO MODIFY THIS FUNCTION. 
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
    
    sim.setShapeTexture(baseHandle, -1, sim.texturemap_plane, 0, {1.01, 1.01},nil,nil) -- Do not delete or modify this line
    
    generateHorizontalWalls()
    generateVerticalWalls()
    createMaze()
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
    reapplyTexture() -- Do not delete or modify this line
end

function sysCall_cleanup()
    -- do some clean-up here
end

-- See the user manual or the available code snippets for additional callback functions and details

