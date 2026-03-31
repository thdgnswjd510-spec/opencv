import numpy as np
import cv2

img = cv2.imread('shape.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 100,
                           param1=250, param2=10, minRadius=30, maxRadius=100)

if circles is not None:
    circles = np.uint16(np.around(circles))

    for i in circles[0, :]:
        cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
        cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()