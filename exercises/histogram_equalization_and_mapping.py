#HISTOGRAM EQUALIZATION &MAPPING
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('th.jpg', 0)
equ = cv2.equalizeHist(img)
h=cv2.calcHist((img), [0], None, [256], [0,256])
h1=cv2.calcHist((equ), [0], None, [256], [0,256])
res = np.hstack((img, equ))
cv2.imshow('image.jpg', res)
plt.plot(h)
plt.plot(h1)
plt.title("Histogram Mapping & Equalization")
plt.xlabel("Intensity")
plt.ylabel("Frequency")
plt.grid()
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
