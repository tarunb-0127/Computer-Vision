#24 Bit to 8 Bit

import cv2

#Input image

input = cv2.imread("C:/Coding/OpenCV/exercises/original_image.jpg")

#Get input size

height, width = 400,600

w, h = (256, 256)

temp = cv2.resize(input, (w, h), cv2.INTER_LINEAR)

output = cv2.resize(temp, (width, height), cv2.INTER_NEAREST)

cv2.imshow("8bit.jpg",output)

cv2.imshow("24bit.jpg",input)

#24 Bit to 4 Bit

import cv2

#Input image
height, width = 400,600

input_img = cv2.imread("C:/Coding/OpenCV/exercises/original_image.jpg")


#Get input size

a, b = (16, 16)

temp1 = cv2.resize(input_img, (a, b), cv2.INTER_LINEAR)

output1 = cv2.resize(temp1, (width, height), cv2.INTER_NEAREST)

cv2.imshow("4bit.jpg",output1)

cv2.imshow("24bit.jpg",input_img)

#24 Bit to 1 Bit

import cv2

input = cv2.imread("C:/Coding/OpenCV/exercises/original_image.jpg")

#Get input size

height, width = 400,600

c, d = (2, 2)

temp2 = cv2.resize(input, (c, d), cv2.INTER_LINEAR)

output2 = cv2.resize(temp2, (width, height), cv2.INTER_NEAREST)

cv2.imshow("1bit.jpg",output2)

cv2.imshow("24bit.jpg",input)
