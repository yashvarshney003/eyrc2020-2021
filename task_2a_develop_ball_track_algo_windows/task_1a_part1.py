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

def show(name, image):
    cv2.imshow(name, image)
    cv2.waitKey(0)
    if cv2.waitKey(0) & 0xFF==ord(' '):
        cv2.destroyAllWindows()
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

def line_intersect(Ax1, Ay1, Ax2, Ay2, Bx1, By1, Bx2, By2):
    """ returns a (x, y) tuple or None if there is no intersection """
    d = (By2 - By1) * (Ax2 - Ax1) - (Bx2 - Bx1) * (Ay2 - Ay1)
    if d:
        uA = ((Bx2 - Bx1) * (Ay1 - By1) - (By2 - By1) * (Ax1 - Bx1)) / d
        uB = ((Ax2 - Ax1) * (Ay1 - By1) - (Ay2 - Ay1) * (Ax1 - Bx1)) / d
    else:
        return
    if not(0 <= uA <= 1 and 0 <= uB <= 1):
        return
    x = Ax1 + uA * (Ax2 - Ax1)
    y = Ay1 + uA * (Ay2 - Ay1)
 
    return int(x), int(y)

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
def detect(c):
        
        # initialize the shape name and approximate the contour
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.001 * peri, True)
        M = cv2.moments(c)
        cX = int((M["m10"] / M["m00"])) #X co-ordinate of the centroid of the shape
        cY = int((M["m01"] / M["m00"])) #Y co-ordinate of the centroid of the shape
        shape = "unidentified" #Initialize a variable of string type
    
        area = cv2.contourArea(approx)
        #print(f" length of approx {approx}")
        
        
        #Triangle if it shape has three sides
        if len(approx) == 3:
            shape = "Triangle"
        
        elif len(approx) == 4:
            #Call rect() to detect the shape
            angle,op_angle,cong_diag,op_side_eq,all_sides_cong = rect(c)

            #If opposite angles and sides are equal and diagonals are congruent, it must be a parallelogram
            if op_angle and op_side_eq and cong_diag:
                #If all angles and sides are equal, aspect ratio is 1 and diagonals are congruent, it must be a square
                if angle and cong_diag and all_sides_cong:
                    shape='Square'
                elif not(angle) or not(cong_diag) and all_sides_cong:
                    #If aspect ratio is not 1 and angles are not 90, it must be a rhombus
                    shape = 'Rhombus'
                #Otherwise, its a parallelogram
                else:
                    shape = 'Parallelogram'
            #If diagonals are not congruent, aspect ratio is not 1, opposite angles are not equal and
            #all angles are not 90 degrees, it is a trapezium
            elif not(cong_diag) and not(angle) or not(op_angle):
                shape='Trapezium'
            #Otherwise, it is a quadrilateral
            else: shape='Quadrilateral'
        #Pentagon if shape has 5 sides
        elif len(approx) == 5:
            shape = "Pentagon"
        #Hexagon if shape has 6 sides
        elif len(approx) == 6:
            shape = "Hexagon"
        # otherwise, we assume the shape is a circle
        else:
            shape = "Circle"
        #return area rounded off to 1 decimal place
        return shape, float(round(int(area),1)), cX, cY
    
'''     Name: Process
        Inputs: Input image
        Outputs: None
        Purpose: This function masks the RGB colours and calls detect fucntion to
        detect shapes in the image and writes the required output in the shapes dictionary'''

def process(imageFrame):
    #Convert BGR image to HSV
    imageFrame = cv2.GaussianBlur(imageFrame,(5,5),cv2.BORDER_TRANSPARENT)
    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV) 
    
    #To create a mask for red colour
    red_lower = np.array([0, 50, 50]) 
    red_upper = np.array([10, 255, 255]) 
    red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)
    kernal = np.ones((5, 5))
#     red_mask = cv2.dilate(red_mask, kernal)
#     show('red mask',red_mask)
#     print(red_mask.ndim, 'ndim')
#     print('len', len(red_mask))
    red_gray=cv2.threshold(red_mask, 245,225, cv2.THRESH_BINARY)[1]

    
    gray_blur= cv2.Canny(red_gray,100,255)
#     show('redgray', red_gray)
#     show('gray_blur', gray_blur)
    #Create a mask for green colour
    green_lower = np.array([25, 52, 72], np.uint8) 
    green_upper = np.array([102, 255, 255], np.uint8) 
    green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)
    kernal = np.ones((5, 5))
    green_mask = cv2.dilate(green_mask, kernal)
    green_gray=cv2.threshold(green_mask, 250,255, cv2.THRESH_BINARY)[1]
    gray_blur_green = cv2.Canny(green_gray,100,255)
    
#     show('greengray', green_gray)
#     show('gray_blur_green', gray_blur_green)
    
    #Create a mask for blue colour
    blue_lower = np.array([94, 20, 0], np.uint8) 
    blue_upper = np.array([140,255 ,255], np.uint8) 
    blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper) 
    kernal = np.ones((5, 5))  
    blue_mask = cv2.dilate(blue_mask, kernal)
    blue_gray=cv2.threshold(blue_mask, 245,225, cv2.THRESH_TRUNC)[1]
    gray_blur_blue= cv2.Canny(blue_gray,100,255)
    
#     show('bluegray', blue_gray)
#     show('gray_blur_blue', gray_blur_blue)
    
    #Find red contours in the image
    cnts= cv2.findContours(gray_blur , cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
      
    #If red contours found
    if type(cnts[-1]) !=type(None) :
            
        if len(cnts) == 2:
            cnts = cnts[0]

        elif len(cnts) == 3:
            cnts = cnts[1]
        for i in cnts:
            ret_values=detect(i)
            #Add detected shape and corresponding outputs to the dictionary
            shapes[ret_values[0]]=['red', ret_values[1], ret_values[2], ret_values[3]]
    
    #Find green contours n the image
    cnts = cv2.findContours(gray_blur_green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    #If green contours found
    if type(cnts[-1]) !=type(None) :
        if len(cnts) == 2:
            cnts = cnts[0]
        elif len(cnts) == 3:
            cnts = cnts[1]
        
        for i in cnts:
            ret_values=detect(i)
            #Add detected shape and corresponding outputs in the dictionary
            shapes[ret_values[0]]=['green',ret_values[1], ret_values[2], ret_values[3]]


    #Find blue contours in the image
    cnts= cv2.findContours(gray_blur_blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    #If blue contours found
    if type(cnts[-1]) !=type(None) :
        if len(cnts) == 2:
            cnts = cnts[0]
        elif len(cnts) == 3:
            cnts = cnts[1]
        for i in cnts:
            ret_values=detect(i)
            #Add detected shape and corresponding outputs in the dictionary
            shapes[ret_values[0]]=['blue',ret_values[1], ret_values[2], ret_values[3]]


##############################################################


def scan_image(img_file_path):
    global shapes
    shapes={}

    #Read the image
    image = cv2.imread(img_file_path)
    
    #Call the process function to detect shapes and other required outputs
    process(image)
#     cv2.imshow("Image", resized)
#     cv2.waitKey(0)
#     if cv2.waitKey(0) & 0xFF == ord('q'):
#         cv2.destroyAllWindows()
    #Sort the dictionary in descending order of area of the shape
    shapes=dict(sorted(shapes.items(), key=lambda x:x[1][1],reverse=True))
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
    img_dir_path = curr_dir_path + '/Samples/'
    
    # path to 'Sample1.png' image file
    file_num = 1
    img_file_path = img_dir_path + 'Sample' + str(file_num) + '.png'

    print('\n============================================')
    print('\nLooking for Sample' + str(file_num) + '.png')

    if os.path.exists('Samples/Sample' + str(file_num) + '.png'):
        print('\nFound Sample' + str(file_num) + '.png')
    
    else:
        print('\n[ERROR] Sample' + str(file_num) + '.png not found. Make sure "Samples" folder has the selected file.')
        exit()
    
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