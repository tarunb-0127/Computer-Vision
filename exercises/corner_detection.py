# Importing the libraries
import cv2
import numpy as np

# Harris Corner Detection
# Reading the image and converting the image to B/W
img = cv2.imread('l.jpg')
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_image = np.float32(gray_image)
# Applying the function
dst = cv2.cornerHarris(gray_image, blockSize=2, ksize=3, k=0.04)
# dilate to mark the corners
dst = cv2.dilate(dst, None)
img[dst > 0.01 * dst.max()] = [0, 0, 255]
cv2.imshow('Harris Corner Detection', img)
cv2.waitKey(0)

# SIFT Detection
# Reading the image and converting into B/W
image = cv2.imread('l.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Create SIFT object
sift = cv2.SIFT_create()
# Detect keypoints and compute descriptors
kp, des = sift.detectAndCompute(gray_image, None)
# Draw keypoints
kp_image = cv2.drawKeypoints(image, kp, None, color=(0, 0, 255), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('SIFT Detection', kp_image)
cv2.waitKey(0)

# FAST Corner Detection
# Reading the image and converting into B/W
image = cv2.imread('l.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Create FAST object
fast = cv2.FastFeatureDetector_create()
# Detect keypoints
kp = fast.detect(gray_image, None)
# Draw keypoints
kp_image = cv2.drawKeypoints(image, kp, None, color=(0, 0, 255))
cv2.imshow('FAST Corner Detection', kp_image)
cv2.waitKey(0)

cv2.destroyAllWindows()
