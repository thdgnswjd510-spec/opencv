import numpy as np
import cv2

img=np.full((512,512,3),255,np.uint8)

drawing=False
ix,iy=-1,-1

def Drag (event,x,y,flags,param):
    global ix,iy,drawing

    if event==cv2.EVENT_LBUTTONDOWN:
        drawing=True
        ix,iy=x,y

    elif event==cv2.EVENT_MOUSEMOVE:
        if drawing==True:
            cv2.line(img,(ix,iy),(x,y),(0,0,0),3)
            ix,iy=x,y

    elif event==cv2.EVENT_LBUTTONUP:
        drawing=False
        cv2.line(img,(ix,iy),(x,y),(255,0,0),2)

cv2.namedWindow('img')
cv2.setMouseCallback("img",Drag)

while True:
    cv2.imshow("img",img)
    key=cv2.waitKey(1)

    if cv2.getWindowProperty("img",cv2.WND_PROP_VISIBLE)<1:
        break

    if key== ord('c'):
        img[:]=255

    elif key== ord('q') or key==27:
        break

cv2.destroyAllWindows()

