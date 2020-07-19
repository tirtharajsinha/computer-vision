import cv2
import numpy as np

cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,150)

mycolor=[[5,107,0,19,255,255],#orange
         [133,56,0,159,156,255],#purple
         [57,76,0,100,255,255]]#green

mycolorvalues=[[51,153,255],    ##BGR format
               [255,0,255],
               [0,255,0]]

mypoint=[]   #[x,y,colorcode]

def findcolor(img,mycolor,mycolorvalues):
     imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
     count=0
     newpoints=[]
     for color in mycolor:
         lower = np.array(color[:3])
         upper = np.array(color[3:6])
         mask = cv2.inRange(imghsv, lower, upper)
         x,y=getcontours(mask)
         cv2.circle(imgresult,(x,y),10,mycolorvalues[count],cv2.FILLED)
         if x!=0 and y!=0:
             newpoints.append([x,y,count])
         count=count+1
     return newpoints
       #  cv2.imshow(str(color[0]),mask)

def getcontours(img):
    contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h=0,0,0,0
    for cnt in contours:
        area=cv2.contourArea(cnt)

        if area>500:
           #cv2.drawContours(imgresult, cnt, -1, (255, 0, 0), 3)
           peri=cv2.arcLength(cnt,True)

           approx=cv2.approxPolyDP(cnt,0.02*peri,True)

           x,y,w,h=cv2.boundingRect(approx)
    return x+w//2,y

def drawoncanvas(mypoint,mycolorvalues):
    for points in mypoint:
        cv2.circle(imgresult, (points[0], points[1]), 10, mycolorvalues[points[2]], cv2.FILLED)


while True:
    success,img=cap.read()
    imgresult=img.copy()
    newpoints=findcolor(img,mycolor,mycolorvalues)
    if len(newpoints)!=0:
        for newpnt in newpoints:
            mypoint.append(newpnt)
    if len(mypoint)!=0:
        drawoncanvas(mypoint,mycolorvalues)
    cv2.imshow("Video",imgresult)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break



