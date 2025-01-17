# -*- coding: utf-8 -*-
import cv2
#Import OpenCV
#import cv2.cv as cv
#Import Numpy
import numpy as np

camera_feed = cv2.VideoCapture(0)

def nothing(x):
    pass


cv2.namedWindow('image')
cv2.createTrackbar('h_max','image',179,179,nothing)
cv2.createTrackbar('h_min','image',0,179,nothing)
cv2.createTrackbar('s_max','image',255,255,nothing)
cv2.createTrackbar('s_min','image',0,255,nothing)
cv2.createTrackbar('v_max','image',255,255,nothing)
cv2.createTrackbar('v_min','image',0,255,nothing)


while(1):

    _,frame = camera_feed.read()
    #Convert the current frame to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 设定蓝色的阈值
    h_max=cv2.getTrackbarPos('h_max','image')
    h_min=cv2.getTrackbarPos('h_min','image')
    s_max=cv2.getTrackbarPos('s_max','image')
    s_min=cv2.getTrackbarPos('s_min','image')
    v_max=cv2.getTrackbarPos('v_max','image')
    v_min=cv2.getTrackbarPos('v_min','image')
    
    # -----------------pink------------------
    #lower_blue=np.array([110,50,50])
    lower_blue=np.array([h_min,s_min,v_min])
    #upper_blue=np.array([130,255,255])
    upper_blue=np.array([h_max,s_max,v_max])
    
    
    '''
    #Define the threshold for finding a blue object with hsv
    lower_blue = np.array([120,69,0])
    upper_blue = np.array([179,224,255])
    '''
    #Create a binary image, where anything blue appears white and everything else is black
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    #Get rid of background noise using erosion and fill in the holes using dilation and erode the final image on last time
    element = cv2.getStructuringElement(cv2.MORPH_RECT,(9,9))
    mask = cv2.erode(mask,element, iterations=2)
    mask = cv2.dilate(mask,element,iterations=2)

    mask = cv2.erode(mask,element)
    
    #Create Contours for all blue objects
    image1,contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #image1,contours, hierarchy = cv2.findContours(mask, 1, 2)
    maximumArea = 0
    bestContour = None

    # for all object
    for contour in contours:
        '''
        #Straight Bounding Rectangle
        x,y,w,h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y),(x+w,y+h), (0,0,255), 3)
        '''

        #Rotated Rectangle
        rect = cv2.minAreaRect(contour)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        cv2.drawContours(frame,[box],0,(0,0,255),2)


    # #only for the biggest object
    # for contour in contours:
        # currentArea = cv2.contourArea(contour)
        # if currentArea > maximumArea:
            # bestContour = contour
            # maximumArea = currentArea
     # #Create a bounding box around the biggest blue object
    # if bestContour is not None:
        # x,y,w,h = cv2.boundingRect(bestContour)
        # cv2.rectangle(frame, (x,y),(x+w,y+h), (0,0,255), 3)
    

    #Show the original camera feed with a bounding box overlayed 
    cv2.imshow('frame',frame)

    #cv2.imshow('hsv', hsv)

    #Show the contours in a seperate window
    #cv2.imshow('mask',mask)

    cv2.imshow('res',res)
    #Use this command to prevent freezes in the feed
    k = cv2.waitKey(5) & 0xFF
    #If escape is pressed close all windows
    if k == 27:
        break


cv2.destroyAllWindows() 