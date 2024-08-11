import cv2
import numpy as np
# Reading the image
image = cv2.imread('sunflower.jpg')
# Applying the filter
averageBlur = cv2.blur(image, (5, 5))
gaussian = cv2.GaussianBlur(image, (3, 3), 0)
medianBlur = cv2.medianBlur(image, 9)
bilateral = cv2.bilateralFilter(image, 9, 75, 75)

# Showing the image
cv2.imshow('Original', image)
cv2.imshow('Average blur', averageBlur)
cv2.imshow('Gaussian blur', gaussian)
cv2.imshow('Median blur', medianBlur)
cv2.imshow('Bilateral blur', bilateral)

cv2.waitKey()
cv2.destroyAllWindows()




