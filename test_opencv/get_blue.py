import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)

while(1):
    t0 = time.time()
    # Take each frame
    _, inframe = cap.read()
    frame = cv2.resize(inframe,None,fx=0.2, fy=0.2, interpolation = cv2.INTER_CUBIC)
    
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    #cv2.imshow('frame',inframe)
    #cv2.waitKey(5)
    #cv2.imshow('mask',mask)
    #cv2.imshow('res',res)
    #cv2.waitKey(5)
    t1 = time.time()
    print t1-t0
    # k = cv2.waitKey(5) & 0xFF
    # if k == 27:
        # break

cv2.destroyAllWindows()