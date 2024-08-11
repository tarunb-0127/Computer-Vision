import numpy as np
import cv2 as cv

# Function to tilt the image into slanting
def tilt(img):
    rows, cols, ch = img.shape[:3]
    pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
    pts2 = np.float32([[10, 100], [200, 50], [100, 200]])
    M = cv.getAffineTransform(pts1, pts2)
    res = cv.warpAffine(img, M, (cols, rows))
    return res

# Function to magnify the image and focus
def zoom(img):
    rows, cols, ch = img.shape[:3]
    # Adjust these points based on the image size
    pts1 = np.float32([[46, 65], [300, 65], [46, 300], [300, 300]])
    pts2 = np.float32([[10, 10], [350, 10], [10, 350], [350, 350]])
    M = cv.getPerspectiveTransform(pts1, pts2)
    res = cv.warpPerspective(img, M, (cols, rows))
    return res

# Load image
img = cv.imread('OIP (1).jpg', 1)

# Check if the image is loaded successfully
if img is None:
    print("Error: Unable to load image")
else:
    # Apply tilt transformation and display
    tilted_img = tilt(img)
    cv.imshow('Original Image',img)
    cv.imshow('Tilted Image', tilted_img)
    cv.waitKey()

    # Apply zoom transformation and display
    zoomed_img = zoom(img)
    cv.imshow('Focused Image', zoomed_img)
    cv.waitKey()

    # Close all OpenCV windows
    cv.destroyAllWindows()
