import numpy as np
import cv2

img=cv2.imread('morphology.jpg',cv2.IMREAD_GRAYSCALE)
kernel = np.ones((5,5), np.uint8)
erosion=cv2.erode(img,kernel,iterations = 1)
dilation=cv2.dilate(img,kernel,iterations = 1)


kernel = np.ones((3, 3), np.uint8)
# 열림 연산으로 자잘한 노이즈 제거
result = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
result=cv2.dilate(result, kernel, iterations = 1)


cv2.imshow('result', result)
cv2.imshow('erosion', erosion)
cv2.imshow('dilation', dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()