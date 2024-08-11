import cv2 as cv
import numpy as np
im = cv.imread('OIP.jpg')
img = cv.resize(im,(480,360))

cv.imshow('Real Image',img)
cv.waitKey()

def erosion(img):
    ker = np.ones((5,5),np.uint8)
    er = cv.erode(img,ker,iterations = 1)
    cv.imshow('Erosion',er)
    cv.waitKey()
   
def dilation(img):
    ker = np.ones((5,5),np.uint8)
    dil = cv.dilate(img,ker,iterations = 1)
    cv.imshow('Dilution',dil)
    cv.waitKey()

def opening(img):
    ker = np.ones((5,5),np.uint8)
    op = cv.morphologyEx(img, cv.MORPH_OPEN, ker)
    cv.imshow('Opening',op)
    cv.waitKey()

def closing(img):
    ker = np.ones((5,5),np.uint8)
    cl = cv.morphologyEx(img, cv.MORPH_CLOSE, ker)
    cv.imshow('Closing',cl)
    cv.waitKey()
   
erosion(img)
dilation(img)
opening(img)
closing(img)

cv.destroyAllWindows()
