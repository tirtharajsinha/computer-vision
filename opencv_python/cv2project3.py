#python opencv project
#number plate ditector
#devoloper Tirtharaj Sinha
#opencv project
####################################

import cv2
import numpy as np



cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)
platecascade = cv2.CascadeClassifier("stock/haarcascade_russian_plate_number.xml")
minarea=500
color=(255,255,0)
count=0
while True:
    success,img=cap.read()


    imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    numberplate = platecascade.detectMultiScale(imggray, 1.1, 4)

    for (x, y, w, h) in numberplate:
        area=w*h
        if area>minarea:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
            cv2.putText(img,"Number Plate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
            imgroi=img[y:y+h,x:x+w]
            cv2.imshow("roi",imgroi)



    cv2.imshow("Video",img)

    if cv2.waitKey(1) & 0xFF==ord("s"):
        cv2.imwrite("stock/scanned/Noplate_"+str(count)+".jpg",imgroi)
        cv2.rectangle(img,(0,200),(640,300),(0,255,255),cv2.FILLED)
        cv2.putText(img,"scan saved",(150,265),cv2.FONT_HERSHEY_DUPLEX,2,(0,255,0),2)
        cv2.imshow("Video",img)
        cv2.waitKey(500)
        count += 1

