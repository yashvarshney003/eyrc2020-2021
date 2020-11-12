import numpy as np
import cv2 as cv
import csv
if __name__ == "__main__":
    import task_1b
    image = cv.imread("shot2.png",1)
    wraped_image = task_1b.applyPerspectiveTransform(image)
    cv.imshow("warpedimage",wraped_image)
    cv.waitKey(0)
    cv.destroyAllWindows()