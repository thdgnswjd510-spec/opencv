import cv2
import numpy as np

img=cv2.imread("passport.jpg")
img=cv2.resize(img,(400,600))
rows,cols=img.shape[:2]

def Click(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
      print(x,y)


cv2.circle(img,(47,322),10,(255,0,0),-1)
cv2.circle(img,(281,493),10,(0,255,0),-1)
cv2.circle(img,(129,75),10,(0,0,255),-1)
cv2.circle(img,(334,203),10,(0,0,255),-1)

pts1=np.float32([[47,322],[281,493],[129,75],[334,203]])
pts2=np.float32([[0,0],[0,600],[400,0],[400,600]])
M=cv2.getPerspectiveTransform(pts1,pts2)

dst=cv2.warpPerspective(img,M,(400,600))

cv2.imshow("img",img)
cv2.setMouseCallback("img",Click)
cv2.imshow("img2",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
