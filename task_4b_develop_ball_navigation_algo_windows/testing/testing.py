import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
data = cv.imread("result_maze00.jpg")
data = cv.resize(data, (1280, 1280)) 
x_increment = 64
y_increment = 64
for i in range(0,10):
    for j in range(1,10):
        data = cv.circle(data,(64+(j-1)*128,64+(i*128)),5,(255,0, 0),2)
        data = cv.line(data,(64+(j-1)*128, 64+(i*128)),( 64+ j*128, 64+(i*128)),(0, 255, 0), 5) 

plt.imshow(data)
plt.show()