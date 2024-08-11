#CANNY EDGE DETECTION
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('tesla.jpg',0)
edges = cv.Canny(img,100,200)
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()


#SOBAL EDGE DETECTION
import cv2
import matplotlib.pyplot as plt
#imgpath = "test.tiff"
img = cv2.imread("tesla.jpg", 1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
edgesx = cv2.Sobel(img, -1, dx=1, dy=0, ksize=1)
edgesy = cv2.Sobel(img, -1, dx=0, dy=1, ksize=1)
edges = edgesx + edgesy
output = [img, edgesx, edgesy, edges]
titles = ['Original', 'x', 'y', 'Edges']

for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.imshow(output[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()
