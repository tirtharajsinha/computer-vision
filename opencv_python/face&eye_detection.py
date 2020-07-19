import cv2
import numpy as np
facecascade=cv2.CascadeClassifier("stock/haarcascade_frontalface_default.xml")
eyecascade=cv2.CascadeClassifier("stock/haarcascade_eye.xml")

img=cv2.imread("stock/messi.jpg")
imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


faces=facecascade.detectMultiScale(imggray,1.1,4)
#eyes=eyecascade.detectMultiScale(imggray,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    roi_gray = imggray[y:y + h, x:x + w]
    roi_color = img[y:y + h, x:x + w]
    eyes = eyecascade.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0,0,255), 2)

cv2.imshow("original",img)
cv2.waitKey(0)