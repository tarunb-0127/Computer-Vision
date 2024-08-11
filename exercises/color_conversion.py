import cv2

image = cv2.imread("istockphoto-184276818-612x612.jpg")
w, h = (256, 256)
image = cv2.resize(image, (w,h), cv2.INTER_LINEAR)


# converting BGR to RGB
image_rgbb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_rgbg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_rgbh = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
image_rgby = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)

cv2.imshow('BGR to RGB', image_rgbb)
cv2.imshow('BGR to Grayscale', image_rgbg)
cv2.imshow('BGR to HSV', image_rgbh)
cv2.imshow('BGR to YUV', image_rgby)

cv2.waitKey(0)
cv2.destroyAllWindows()
