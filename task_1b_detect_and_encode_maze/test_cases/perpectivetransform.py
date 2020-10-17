import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt 
img = cv.imread('maze07.jpg',1)
rows,cols,ch = img.shape
pts1 = np.float32([[49,60],[450,55],[56,456],[456,456]])
pts2 = np.float32([[0,0],[509,0],[0,509],[509,509]])
M = cv.getPerspectiveTransform(pts1,pts2)
dst = cv.warpPerspective(img,M,(510,510))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()