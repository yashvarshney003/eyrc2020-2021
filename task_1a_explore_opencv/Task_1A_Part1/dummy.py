i=0
for c in contours:
    perimeter = cv2.arcLength(c,True)
    approx = cv2.approxPolyDP(c,0.01*perimeter,True)
    if(len(approx)== 4):
        (x, y, w, h) = cv2.boundingRect(approx)
        ar = w/float(h)
        print(f"aspect ratio{ar}")
        if(ar >=0.95 or ar <=1.05):
            pts = approx.reshape(4, 2)
            print(pts)
            rect = np.zeros((4, 2), dtype = "float32")
    # the top-left point will have the smallest sum, whereas
    # the bottom-right point will have the largest sum
            s = pts.sum(axis = 1)
            rect[0] = pts[np.argmin(s)]
            rect[2] = pts[np.argmax(s)]
    # now, compute the difference between the points, the
    # top-right point will have the smallest difference,
    # whereas the bottom-left will have the largest difference
            diff = np.diff(pts, axis = 1)
            rect[1] = pts[np.argmin(diff)]
            rect[3] = pts[np.argmax(diff)]
    # return the ordered coordinates
            print(rect)
            print("above rect")
            x1= rect[0][0]
            y1= rect[0][1]
            x2= rect[1][0]
            y2= rect[1][1]
            x3= rect[2][0]
            y3= rect[2][1]
            x4= rect[3][0]
            y4= rect[3][1]
            dist1 = math.sqrt((x3 - x1)**2 + (y3 - y1)**2)
            dist2 = math.sqrt((x4 - x2)**2 + (y4 - y2)**2)
            print(dist1)
            print(dist2)
            if(abs(dist1 -dist2)<=2.000):
                    print("square")
            else:
                    print("rhombus")
        			print(perimeter)
        			print("jhvjvjvjvjh")

        			cv2.drawContours(image,contours,i, (234,242,0), 3)
        			i+=1
        			plt.imshow(image,cmap= 'gray')
        			plt.show()
    	else:
            pts = approx.reshape(4, 2)
            print(pts)
            rect = np.zeros((4, 2), dtype = "float32")
    # the top-left point will have the smallest sum, whereas
    # the bottom-right point will have the largest sum
            s = pts.sum(axis = 1)
            rect[0] = pts[np.argmin(s)]
            rect[2] = pts[np.argmax(s)]
    # now, compute the difference between the points, the
    # top-right point will have the smallest difference,
    # whereas the bottom-left will have the largest difference
            diff = np.diff(pts, axis = 1)
            rect[1] = pts[np.argmin(diff)]
            rect[3] = pts[np.argmax(diff)]
    # return the ordered coordinates
            print(rect)
            print("above rect")
            x1= rect[0][0]
            y1= rect[0][1]
            x2= rect[1][0]
            y2= rect[1][1]
            x3= rect[2][0]
            y3= rect[2][1]
            x4= rect[3][0]
            y4= rect[3][1]
            dist1 = math.sqrt((x3 - x1)**2 + (y3 - y1)**2)
            dist2 = math.sqrt((x4 - x2)**2 + (y4 - y2)**2)
            print(dist1)
            print(dist2)
            if(abs(dist1 -dist2)<=2.000):
                    print("square")
            else:
                    print("rhombus")
                    print(perimeter)
                    print("jhvjvjvjvjh")

                    cv2.drawContours(image,contours,i, (234,242,0), 3)
                    i+=1
                    plt.imshow(image,cmap= 'gray')
                    plt.show()'''