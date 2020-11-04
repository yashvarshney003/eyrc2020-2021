import cv2, numpy as np




cap = cv2.VideoCapture('Videos/ballmotionwhite.m4v')

# print(cap.get(cv2.CAP_PROP_FRAME_COUNT))
frame_list=[69,138,207]

for i in frame_list:
    cap.set(cv2.CAP_PROP_POS_FRAMES, i-1)
# while cap.isOpened() :
    ret, imageFrame = cap.read()
    if ret== True:
        hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV) 
      
        # Set range for red color and  
        # define mask 
        red_lower = np.array([0, 50, 50]) 
        red_upper = np.array([10, 255, 255]) 
        red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)
        kernal = np.ones((5, 5), "uint8") 
        
    #     red_mask = cv2.dilate(red_mask, kernal) 
        res_red = cv2.bitwise_and(imageFrame, imageFrame,  mask = red_mask)
    #     cv2.imshow('res_red', res_red)
        cnts= cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
          
#         print('length of red contours',len(cnts))
    #     print(cnts)
        if type(cnts[-1]) !=type(None) :
#             print('in if')
            if len(cnts) == 2:
                cnts = cnts[0]

            # if the length of the contours tuple is '3' then we are using
            # either OpenCV v3, v4-pre, or v4-alpha
            elif len(cnts) == 3:
                cnts = cnts[1]
        for c in cnts:
            M = cv2.moments(c)
            cX = int((M["m10"] / M["m00"]))
            cY = int((M["m01"] / M["m00"]))
            print('cX',cX,'cY', cY)
#             area = cv2.contourArea(c)
#             print('area',area)
    #     cv2.imshow('frame', red_mask)
        if cv2.waitKey(25) & 0xFF == ord('q'):
        
        
            cap.release()
            cv2.destroyAllWindows()
                

        

