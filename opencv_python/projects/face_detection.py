#python opencv project
#number plate ditector
#devoloper Tirtharaj Sinha
#opencv project
####################################

import cv2
import numpy as np



cap=cv2.VideoCapture(0)
cap.set(3,800)
cap.set(4,600)
cap.set(10,100)



while True:
    success,img=cap.read()

    facecascade = cv2.CascadeClassifier("stock/haarcascade_frontalface_default.xml")
    eyecascade = cv2.CascadeClassifier("stock/haarcascade_eye.xml")

    imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = facecascade.detectMultiScale(imggray, 1.6, 2)

    for (x, y, w, h) in faces:
        cv2.circle(img, (x + w // 2, y + h // 2), h // 2 + 20, (0, 185, 0), 5)
        roi_gray = imggray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        eyes = eyecascade.detectMultiScale(roi_gray,1.1, 4)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 1)



    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break
