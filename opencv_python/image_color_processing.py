import cv2
import numpy as np

img=cv2.imread("stock/cvimg2.jpg")
kernel=np.ones((5,5),np.uint8)

imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgblur=cv2.GaussianBlur(img,(7,7),0)
imgcanny=cv2.Canny(imgGray,100,100)
imgdialation=cv2.dilate(imgcanny,kernel,iterations=1)
imgeroded=cv2.erode(imgdialation,kernel,iterations=1)

cv2.imshow("image",img)
cv2.imshow("Gray Image",imgGray)
# cv2.imshow("blur Image",imgblur)
cv2.imshow("canny Image",imgcanny)
# cv2.imshow("dialation Image",imgdialation)
# cv2.imshow("eroded Image",imgeroded)
cv2.waitKey(0)