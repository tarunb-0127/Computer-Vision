import cv2 
import sys 
import numpy as np 
#read input image 
image = cv2.imread("blurred.jpg") 
#check is input image exists 
if image is None: 
    print("can not find image") 
    sys.exit() 
#define sharpening kernel 
sharpeningKernel = np.array(([0, -1, 0],[-1, 5, -1],[0, -1, 0]), dtype="int") 
#filter2D is used to perform the convolution. 
# The third parameter (depth) is set to -1 which means the bit-depth of the output image is the  
# same as the input image. So if the input image is of type CV_8UC3, the output image will also be of the same type 
output = cv2.filter2D(image, -1, sharpeningKernel) 
#create windows to display images 
cv2.namedWindow("image", cv2.WINDOW_AUTOSIZE) 
cv2.namedWindow("output", cv2.WINDOW_AUTOSIZE) 
#display images 
cv2.imshow("image", image) 
cv2.imshow("output", output) 
#press esc to exit the program 
cv2.waitKey(0) 
#close all the opened windows 
cv2.destroyAllWindows() 
