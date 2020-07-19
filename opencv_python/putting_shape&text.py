import cv2
import numpy as np


# img=cv2.imread("stock/mclaren-720s_0.jpg")
# print(img.shape)
img=np.zeros((512,512,3),np.uint8)
# img[200:300,100:300]=255,0,0
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(255,255,0),3)
cv2.line(img,(0,512),(512,0),(0,255,255),3)
cv2.rectangle(img,(0,0),(250,350),(255,0,255),3)
cv2.circle(img,(256,256),30,(255,0,0),5)
cv2.putText(img,"tsidealONEidentity",(100,100),cv2.FONT_HERSHEY_DUPLEX,1,(0,150,0),3)

# imgresize=cv2.resize(img,(600,300))
# print(imgresize.shape)
#
# imgcrop=img[0:200,300:500]

cv2.imshow("image",img)
# cv2.imshow("resized image",imgresize)
# cv2.imshow("cropped image",imgcrop)


cv2.waitKey(0)

