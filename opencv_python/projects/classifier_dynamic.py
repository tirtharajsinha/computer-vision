import cv2
import numpy as np

#files[coco.namrs,ssd_mobilenet_v3,inference_graph] are avelaible at stock/classifier folder


#img=cv2.imread('stock/cvimg3.jpg')
cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)


classFile='stock/classifier/coco.names'
with open(classFile,'rt') as f:
    classNames=f.read().rstrip('\n').split('\n')


configpath='stock/classifier/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightspath='stock/classifier/frozen_inference_graph.pb'


net=cv2.dnn_DetectionModel(weightspath,configpath)
net.setInputSize(320,320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5,127.5,127.5))
net.setInputSwapRB(True)

while True:
    success,img=cap.read()
    classids, confs, bbox = net.detect(img, confThreshold=0.5)
    if len(classids)!=0:
        for classid, confidence, box in zip(classids.flatten(), confs.flatten(), bbox):
            cv2.rectangle(img, box, color=(0, 255, 0), thickness=3)
            cv2.putText(img, classNames[classid - 1].upper(), (box[0] + 10, box[1] + 30), cv2.FONT_HERSHEY_COMPLEX, 1,
                        (0, 255, 255), 2)


    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break




