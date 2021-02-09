import cv2 
from matplotlib import pyplot as plt
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
                    str(y), (x,y), font, 
                    1, (255, 0, 0), 2) 
        cv2.imshow('image', img) 
  
    # checking for right mouse clicks      
    if event==cv2.EVENT_RBUTTONDOWN: 
  
        # displaying the coordinates 
        # on the Shell 
        print(x, ' ', y) 
  
        # displaying the coordinates 
        # on the image window 
        font = cv2.FONT_HERSHEY_SIMPLEX 
        b = img[y, x, 0] 
        g = img[y, x, 1] 
        r = img[y, x, 2] 
        cv2.putText(img, str(b) + ',' +
                    str(g) + ',' + str(r), 
                    (x,y), font, 1, 
                    (255, 255, 0), 2) 
        cv2.imshow('image', img) 
img  = cv2.imread("table_4__26k123.png")
img2  = cv2.imread("table_4__26k123.png")
for i in range(64,1280,128):
    for j in range(64,1280,128):
        #print(i,j)
        ip = i + round((5 - ((i+64)//640)*10)* 3)
        jp = j + round((5 - ((j +64)//640)*10)* 3)
        img =  cv2.line(img,(ip+10,jp),(ip+10,jp+128),(122,234,2),4)
        img = cv2.circle(img,(ip,jp),10,(255,0,255),2)
plt.imshow(img)
plt.show()
cv2.imshow('image', img2) 
  
    # setting mouse hadler for the image 
    # and calling the click_event() function 
cv2.setMouseCallback('image', click_event) 
  
    # wait for a key to be pressed to exit 
cv2.waitKey(0) 
  
    # close the window 
cv2.destroyAllWindows() 