import cv2

img=cv2.imread('green.png')
img1=cv2.resize(img,(512,512))
img2=cv2.imread('lena.jpg')
cv2.imshow('img1',img1)

hsv=cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)
mask_green=cv2.inRange(hsv,(40,50,50),(80,255,255))
mask_girin=cv2.bitwise_not(mask_green)
cv2.imshow('mask1',mask_girin)

girin_extacted=cv2.bitwise_and(img1,img1,mask=mask_girin)
cv2.imshow('mask2',girin_extacted)

lena_mask=cv2.bitwise_and(img2,img2,mask=mask_green)
cv2.imshow('mask3',lena_mask)

lena_girin=cv2.add(lena_mask,girin_extacted)
cv2.imshow('result',lena_girin)
cv2.waitKey(0)
cv2.destroyAllWindows()
