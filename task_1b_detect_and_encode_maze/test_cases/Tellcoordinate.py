import cv2 as cv
   
# function to display the coordinates of 
# of the points clicked on the image  
def click_event(event, x, y, flags, params): 
  
    # checking for left mouse clicks 
    if event == cv.EVENT_LBUTTONDOWN: 
  
        # displaying the coordinates 
        # on the Shell 
        print(x, ' ', y) 
  
        # displaying the coordinates 
        # on the image window 
        font = cv.FONT_HERSHEY_SIMPLEX 
        cv.putText(img, str(x) + ',' +
                    str(y), (x-50,y), font, 
                    1, (255, 0, 0), 2) 
        cv.imshow('image', img) 
  
    # checking for right mouse clicks      
    
  
# driver function  
if __name__=="__main__": 
  
    # reading the image 
    img = cv.imread('Shape01.png', 1) 
  
    # displaying the image 
    cv.imshow('image', img) 

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    
    ret2,thresh2 = cv.threshold(gray,109,255,cv.THRESH_BINARY)
    #cv.imwrite("getPerspectiveTransformbinary.jpg",thresh2)
    
  
    # setting mouse hadler for the image 
    # and calling the click_event() function 
    cv.setMouseCallback('image', click_event) 
  
    # wait for a key to be pressed to exit 
    cv.waitKey(0) 
  
    # close the window 
    cv.destroyAllWindows() 