import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mg

# Reading image
img = cv2.imread('g1.jpg')
img=cv2.resize(img, (0, 0), fx = 0.1, fy = 0.1)

# variable and converting to gray scale.
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Converting image to a binary image
# ( black and white only image).
ret, threshold = cv2.threshold(imgray, 127, 255, 0)

# Detecting contours in image.
contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
print("Number of contours="+str(len(contours)))
print(contours[0])
cv2.drawContours(img,contours,-1,(0,255,0),3)

cv2.imshow('Image',img)
cv2.imshow('IMage GRAY',imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()
