# From: http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_drawing_functions/py_drawing_functions.html#drawing-functions
# Description: Program adds shapes and text to a back rectangle

import numpy as np
import cv2

# Create a black image
img = np.zeros((512,512,3), np.uint8)
cv2.imshow('image', img)
cv2.waitKey()

# Draw a diagonal blue line with thickness of 5 px
cv2.line(img,(0,0),(511,511),(255,0,0),5)
cv2.imshow('image', img)
cv2.waitKey()

# Draw rectangle
cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
cv2.imshow('image', img)
cv2.waitKey()

# Draw circle
cv2.circle(img,(447,63), 63, (0,0,255), -1)
cv2.imshow('image', img)
cv2.waitKey()

# Draw ellipse
cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
cv2.imshow('image', img)
cv2.waitKey()

# Draw a polygon
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255))
cv2.imshow('image', img)
cv2.waitKey()

# Add text
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)
cv2.imshow('image', img)
cv2.waitKey()