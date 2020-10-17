import cv2 
   
# function to display the coordinates of 
# of the points clicked on the image  
def click_event(event, x, y, flags, params): 
  
    # checking for left mouse clicks 
    if event == cv2.EVENT_LBUTTONDOWN: 
  
        # displaying the coordinates 
        # on the Shell 
        print(x, ' ', y) 
  
        # displaying the coordinates 
        # on the image window 
        font = cv2.FONT_HERSHEY_SIMPLEX 
        cv2.putText(img, str(x) + ',' +
                    str(y), (x-50,y), font, 
                    1, (255, 0, 0), 2) 
        cv2.imshow('image', img) 
  
    # checking for right mouse clicks      
    
  
# driver function 
if __name__=="__main__": 
  
    # reading the image 
    img = cv2.imread('maze02.jpg', 1) 
  
    # displaying the image 
    cv2.imshow('image', img) 
    img9 = cv2.imread('maze09.jpg', 1) 
  
    # displaying the image 
    cv2.imshow('image2', img9)
    img1 = cv2.imread('maze01.jpg', 1) 
  
    # displaying the image 
    cv2.imshow('image2', img1)
    img3 = cv2.imread('maze03.jpg', 1) 
  
    # displaying the image 
    cv2.imshow('image3', img3)
    img4 = cv2.imread('maze04.jpg', 1) 
  
    # displaying the image 
    cv2.imshow('image2', img4)
    img5 = cv2.imread('maze05.jpg', 1) 
  
    # displaying the image 
    cv2.imshow('image5', img5) 

  
    # setting mouse hadler for the image 
    # and calling the click_event() function 
    cv2.setMouseCallback('image', click_event) 
  
    # wait for a key to be pressed to exit 
    cv2.waitKey(0) 
  
    # close the window 
    cv2.destroyAllWindows() 