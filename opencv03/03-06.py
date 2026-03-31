import cv2
import numpy as np
import matplotlib.pyplot as plt
#아핀 변환
img=cv2.imread("/python_opencv/lena.jpg")
rows,cols,channels=img.shape

pts1=np.float32([[50,50],[200,50],[50,200]])
pts2=np.float32([[10,100],[200,50],[100,250]])

cv2.circle(img,(200,100),10,(255,0,0),-1)
cv2.circle(img,(400,100),10,(0,255,0),-1)
cv2.circle(img,(200,200),10,(0,0,255),-1)


M=cv2.getAffineTransform(pts1,pts2)

dst=cv2.warpAffine(img,M,(cols,rows))

plt.subplot(121),plt.imshow(img),plt.title('image')
plt.subplot(122),plt.imshow(dst),plt.title('Affine')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()