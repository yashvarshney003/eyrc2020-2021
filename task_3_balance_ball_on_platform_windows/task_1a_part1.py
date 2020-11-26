'''
*****************************************************************************************
*
*               ===============================================
*                   Nirikshak Bot (NB) Theme (eYRC 2020-21)
*               ===============================================
*
*  This script is to implement Task 1A - Part 1 of Nirikshak Bot (NB) Theme (eYRC 2020-21).
*  
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*  
*  e-Yantra - An MHRD project under National Mission on Education using ICT (NMEICT)
*
*****************************************************************************************
'''

# Team ID:          NB_2139
# Author List:      Aman Tyagi, Yash Varshney
# Filename:         task_1a_part1.py
# Functions:        scan_image, rect, red_mask, blue_mask, green_mask, detect, line_intersect
#                   
# Global variables: shapes


####################### IMPORT MODULES #######################
## You are not allowed to make any changes in this section. ##
## You have to implement this task with the three available ##
## modules for this task (numpy, opencv, os)                ##
##############################################################
import cv2
import numpy as np
import os
##############################################################


# Global variable for details of shapes found in image and will be put in this dictionary, returned from scan_image function
shapes = {}


################# ADD UTILITY FUNCTIONS HERE #################
'''
                Inputs: Coordinates of points of two lines
                Outputs: Intersection point of the two lines
                Purpose: Thispurpose calculates the intersection point of two lines. Intersection
                point is helpful in finding the congruency of the two diagonals which is one of the
                distinct properties of the parallelograms.'''



'''        Name: rect
           Inputs: contours
           Outputs: Properties of parallelograms and quadrilaterals
           Purpose: This function is called when the shape has 4 sides. It calculates several
           different properties of the shape which help distinguish between different parallelograms
           and quadrialteral such as if opposite sides and angles are equal, diagonals are congruent,
           all angles are congruent and if the aspect ratio is one.'''
def rect(c):
    perimeter = cv2.arcLength(c,True)
    approx = cv2.approxPolyDP(c,0.01*perimeter,True)
    print(f"approx{approx}")
    if(len(approx)== 4):
        pts = approx.reshape(4, 2)

        #Vertex co-ordinates
        x1= int(pts[0][0])
        y1= int(pts[0][1])
        x2= int(pts[1][0])
        y2= int(pts[1][1])
        x3= int(pts[2][0])
        y3= int(pts[2][1])
        x4= int(pts[3][0])
        y4= int(pts[3][1])

        #length of each side
        first_side = round(np.sqrt((x1 - x2)**2 + (y1 - y2)**2))
        second_side = round(np.sqrt((x2 - x3)**2 + (y2 - y3)**2))
        third_side = round(np.sqrt((x3 - x4)**2 + (y3 - y4)**2))
        fourth_side = round(np.sqrt((x4 - x1)**2 + (y4 - y1)**2))
        op_side_eq= (-2.0<=round(abs(first_side-third_side),1)<=2.0 and -2.0<=round(abs(second_side-fourth_side),1)<=2.0)
        all_sides_cong=((abs(first_side+third_side)-abs(second_side+fourth_side)) in np.arange(-5,5))

        #If aspect ratio is 1 or not. Useful to distinguish between Square and Rhombus
#         ar= op_side_eq and all_sides_cong
        #To check if diagonals are congruent by checking distance of four vertices from the intersection point
        int_point=line_intersect(x1,y1,x3,y3,x2,y2,x4,y4)
        first_diag_1 = round(np.sqrt((int_point[0] - x1)**2 + (int_point[1] - y1)**2))
        first_diag_2 = round(np.sqrt((int_point[0] - x3)**2 + (int_point[1] - y3)**2))
        second_diag_1 = round(np.sqrt((int_point[0] - x2)**2 + (int_point[1] - y2)**2))
        second_diag_2 = round(np.sqrt((int_point[0] - x4)**2 + (int_point[1] - y4)**2))
#       Keeping an error of +-5 pixels in calculation and detection
        cong_diag=(-5<=abs(first_diag_1-first_diag_2)<=5  and -5<=abs(second_diag_1-second_diag_2)<=5)
        
        #To find if opposite angles are equal
        line_1 = (abs(x2-x1), abs(y2-y1))
        line_2 = (abs(x3-x2), abs(y3-y2))
        line_3 = (abs(x4-x3), abs(y4-y3))
        line_4 = (abs(x4-x1), abs(y4-y1))
        dot_product_1 = np.dot(line_1, line_2) / (np.linalg.norm(line_1) * np.linalg.norm(line_2))
        dot_product_2 = np.dot(line_3, line_2) / (np.linalg.norm(line_2) * np.linalg.norm(line_3))
        dot_product_3 = np.dot(line_4, line_3) / (np.linalg.norm(line_3) * np.linalg.norm(line_4))
        dot_product_4 = np.dot(line_1, line_4) / (np.linalg.norm(line_4) * np.linalg.norm(line_1))
        angle1 = round(180-np.degrees(np.arccos(dot_product_1)))
        angle2 = round(np.degrees(np.arccos(dot_product_2)))
        angle3 = round(180-np.degrees(np.arccos(dot_product_3)))
        angle4 = round(np.degrees(np.arccos(dot_product_4)))
        
        op_angle = -1.0<=(abs(angle3-angle1)-abs(angle4-angle2))<=1.0
        
        #To find if all angles are 90 degree
        angle=(abs(angle1)==abs(angle2)==abs(angle3)==abs(angle4)==90)
        
        #return list containing bool values of required properties
        ret_value =  [angle, op_angle, cong_diag,op_side_eq, all_sides_cong]
        return ret_value
    
'''         Name: detect
            Inputs: contours of the shape
            Outputs: Image shape, area, centroid co-ordinates
            Purpose: This functions takes contours, calculates area and outputs the
            image shape.'''
def detect(color,c):
        
        # initialize the shape name and approximate the contour
        
        M = cv2.moments(c)
        cX = int((M["m10"] / M["m00"])) #X co-ordinate of the centroid of the shape
        cY = int((M["m01"] / M["m00"])) #Y co-ordinate of the centroid of the shape
       
        return [color,cX, cY]
    
'''     Name: Process
        Inputs: Input image
        Outputs: None
        Purpose: This function masks the RGB colours and calls detect fucntion to
        detect shapes in the image and writes the required output in the shapes dictionary'''

def process(imageFrame):
    #initialize a list for keeping records of detected shapes and co-ordinates
    colo= []
    
    #Convert BGR image to HSV
    imageFrame = cv2.GaussianBlur(imageFrame,(5,5),cv2.BORDER_TRANSPARENT)
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
    
    #find contours on blue mask
    cnts= cv2.findContours(gray_blur_blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    ret1 =None
    
    #If blue contours found
    if type(cnts[-1]) !=type(None) :
        if len(cnts) == 2:
            cnts = cnts[0]
        elif len(cnts) == 3:
            cnts = cnts[1]
        for i in cnts:
             ret1 = detect('blue',i)
    if(ret1):

        colo.append(ret1)
           
    #Find red contours in the image
    cnts= cv2.findContours(gray_blur_red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
    
    #If red contours found
    if type(cnts[-1]) !=type(None) :
            
        if len(cnts) == 2:
            cnts = cnts[0]

        elif len(cnts) == 3:
            cnts = cnts[1]
        for i in cnts:
            ret = detect('red',i)
    colo.append(ret)
    
    #return the list containing all detected values
    return(colo)        


##############################################################


def scan_image(img_file_path):
    global shapes
    shapes={}

    #Read the image

    if type(img_file_path) == type(str()):
        img_file_path = cv2.imread(img_file_path)
    else:
        img_file_path= img_file_path
        
        #Call the process function to detect shapes and other required outputs
    outputs = process(img_file_path)
    #if only one circle is detected, add its details to the list in the dictionary
    if(len(outputs)==1):
        shapes['Circle'] = outputs[0]

    else:
        #First, empty the list
        shapes['Circle'] = []
        #append all the detected values in the list
        for  i in outputs:
            shapes['Circle'].append(i)
 
  #return the updated dictionary
    
    return shapes


# NOTE: YOU ARE NOT ALLOWED TO MAKE ANY CHANGE TO THIS FUNCTION
# 
# Function Name:    main
#        Inputs:    None
#       Outputs:    None
#       Purpose:    the function first takes 'Sample1.png' as input and runs scan_image function to find details
#                   of colored (non-white) shapes present in 'Sample1.png', it then asks the user whether
#                   to repeat the same on all images present in 'Samples' folder or not

if __name__ == '__main__':

    curr_dir_path = os.getcwd()
    print('Currently working in '+ curr_dir_path)

    # path directory of images in 'Samples' folder
    img_dir_path = curr_dir_path+'\\'
    
    # path to 'Sample1.png' image file
    file_num = 1
    img_file_path = img_dir_path + 'red_blue.png' #+ str(file_num) + '.png'
    print(img_file_path)
    print(type(img_file_path))
    print(type(str()))
    # print('\n============================================')
    # print('\nLooking for Sample' + str(file_num) + '.png')

    # if os.path.exists('Samples/Sample' + str(file_num) + '.png'):
    #     print('\nFound Sample' + str(file_num) + '.png')
    
    # else:
    #     print('\n[ERROR] Sample' + str(file_num) + '.png not found. Make sure "Samples" folder has the selected file.')
    #     exit()
    
    print('\n============================================')
    
    scan_image(img_file_path)

    try:
        print('\nRunning scan_image function with ' + img_file_path + ' as an argument')
        shapes = scan_image(img_file_path)

        if type(shapes) is dict:
            print(shapes)
            print('\nOutput generated. Please verify.')
        
        else:
            print('\n[ERROR] scan_image function returned a ' + str(type(shapes)) + ' instead of a dictionary.\n')
            exit()

    except Exception:
        print('\n[ERROR] scan_image function is throwing an error. Please debug scan_image function')
        exit()

    print('\n============================================')

    choice = input('\nWant to run your script on all the images in Samples folder ? ==>> "y" or "n": ')

    if choice == 'y':

        file_count = 2
        
        for file_num in range(file_count):

            # path to image file
            img_file_path = img_dir_path + 'Sample' + str(file_num + 1) + '.png'

            print('\n============================================')
            print('\nLooking for Sample' + str(file_num + 1) + '.png')

            if os.path.exists('Samples/Sample' + str(file_num + 1) + '.png'):
                print('\nFound Sample' + str(file_num + 1) + '.png')
            
            else:
                print('\n[ERROR] Sample' + str(file_num + 1) + '.png not found. Make sure "Samples" folder has the selected file.')
                exit()
            
            print('\n============================================')

            try:
                print('\nRunning scan_image function with ' + img_file_path + ' as an argument')
                shapes = scan_image(img_file_path)

                if type(shapes) is dict:
                    print(shapes)
                    print('\nOutput generated. Please verify.')
                
                else:
                    print('\n[ERROR] scan_image function returned a ' + str(type(shapes)) + ' instead of a dictionary.\n')
                    exit()

            except Exception:
                print('\n[ERROR] scan_image function is throwing an error. Please debug scan_image function')
                exit()

            print('\n============================================')

    else:
        print('')
