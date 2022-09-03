import cv2
import numpy as np
from matplotlib import pyplot as plt



path = ".a-"

cap = cv2.VideoCapture(path+"%01d.jpg", cv2.CAP_IMAGES)

test = 0
while True:
    ret, frame = cap.read()
    test +=1

    # gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    # Threshold the image
    ret, thresh = cv2.threshold(frame, 255, 255, 255)

    # Find contours 
    contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        
    # Sort Contors by area and then remove the largest frame contour
    n = len(contours) - 1
    contours = sorted(contours, key=cv2.contourArea, reverse=False)[:n]


    # Iterate through contours and draw the convex hull
    for c in contours:
        hull = cv2.convexHull(c)
        cv2.drawContours(frame, [hull],-2, (0, 0, 255), thickness=-1)
        cv2.fillPoly(frame, [hull], color=(255,0,0))
    plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    cv2.imshow("roi",cv2.cvtColor(frame, cv2.COLOR_BGR2HSV_FULL))
    # plt.show()
    # cv2.imwrite(str(test)+'.png',cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    key = cv2.waitKey(30)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
