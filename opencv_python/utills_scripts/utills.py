import cv2
import numpy as np


def get_filtered_image(image, action):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    action=action.upper()
    if action == 'NO_FILTER':
        filtered = img
    elif action == 'COLORIZED':
        filtered = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    elif action == 'GRAYSCALE':
        filtered = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    elif action == 'BLURRED':
        width, height = img.shape[:2]
        if width > 500:
            k = (50, 50)
        elif width > 200:
            k = (25, 25)
        else:
            k = (10, 10)
        blur = cv2.blur(img, k)
        filtered = cv2.cvtColor(blur, cv2.COLOR_BGR2RGB)
    elif action == "BINARY":
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, filtered = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
    elif action == 'INVERT':
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, img = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
        filtered = cv2.bitwise_not(img)
    elif action == 'FACE_DETECTION':
        img = image
        facecascade = cv2.CascadeClassifier("stock/haarcascade_frontalface_default.xml")
        eyecascade = cv2.CascadeClassifier("stock/haarcascade_eye.xml")
        imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = facecascade.detectMultiScale(imggray, 1.6, 4)
        for (x, y, w, h) in faces:

            cv2.circle(img, (x + w // 2, y + h // 2), h // 2 + 20, (0, 185, 0), 5)
            roi_gray = imggray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]
            eyes = eyecascade.detectMultiScale(roi_gray, 1.1, 4)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 2)

        filtered = img

    elif action == 'CLASSIFICATION':
        img = image
        classFile = 'stock/classifier/coco.names'
        with open(classFile, 'rt') as f:
            classNames = f.read().rstrip('\n').split('\n')

        configpath = 'stock/classifier/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
        weightspath = 'stock/classifier/frozen_inference_graph.pb'

        net = cv2.dnn_DetectionModel(weightspath, configpath)
        net.setInputSize(320, 320)
        net.setInputScale(1.0 / 127.5)
        net.setInputMean((127.5, 127.5, 127.5))
        net.setInputSwapRB(True)

        classids, confs, bbox = net.detect(img, confThreshold=0.52)

        if len(classids) != 0:

            for classid, confidence, box in zip(classids.flatten(), confs.flatten(), bbox):
                cv2.rectangle(img, box, color=(0, 255, 0), thickness=3)
                cv2.putText(img, classNames[classid - 1].upper(), (box[0] + 10, box[1] + 30), cv2.FONT_HERSHEY_TRIPLEX,
                            1,
                            (255, 255, 0), 2)
        filtered = img
    elif action == 'SKETCHED':
        img = image
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_invert = cv2.bitwise_not(img_gray)
        img_smoothing = cv2.GaussianBlur(img_invert, (21, 21), sigmaX=0, sigmaY=0)

        def dodgeV2(x, y):
            return cv2.divide(x, 255 - y, scale=256)

        final_img = dodgeV2(img_gray, img_smoothing)
        filtered = final_img
    elif action == "SHAPE":

        def getcontours(img):
            contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
            for cnt in contours:
                area = cv2.contourArea(cnt)

                if area > 500:
                    cv2.drawContours(imgcontour, cnt, -1, (255, 0, 0), 3)
                    peri = cv2.arcLength(cnt, True)
                    approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)

                    objcolor = len(approx)
                    x, y, w, h = cv2.boundingRect(approx)
                    if objcolor == 3:
                        objectType = "Tri"
                    elif objcolor == 4:
                        aspratio = w / float(h)
                        if aspratio > 0.95 and aspratio < 1.05:
                            objectType = "squre"
                        else:
                            objectType = "rectangle"
                    elif objcolor == 5:
                        objectType = "pentagon"
                    elif objcolor == 6:
                        objectType = "hexagon"
                    elif objcolor == 7:
                        objectType = "heptagon"
                    elif objcolor == 8:
                        objectType = "octagon"
                    elif objcolor > 10:
                        objectType = "circle"
                    else:
                        objectType = "polygon"
                    cv2.rectangle(imgcontour, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    cv2.putText(imgcontour, objectType, (x + (w // 2) - 5, y + (h // 2) - 10), cv2.FONT_HERSHEY_COMPLEX,
                                0.5, (0, 0, 0), 2)

        img = image
        imgcontour = img.copy()
        imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        imgblur = cv2.GaussianBlur(imggray, (7, 7), 1)
        imgcanny = cv2.Canny(imgblur, 50, 50)
        getcontours(imgcanny)
        filtered = imgcontour
        getcontours(imgcanny)
        filtered = imgcontour
    elif action=="DOCUMENT":
        filtered = np.zeros((512, 512, 3), np.uint8)
        cv2.putText(filtered, "NO feature", (100, 200), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 100), 10)
    else:
        filtered = np.zeros((512, 512, 3), np.uint8)
        cv2.putText(filtered, "No Action", (100, 200), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 100), 10)
    return filtered


img = cv2.imread("stock/messi.jpg")
processed = get_filtered_image(img, "FACE_DETECTION")
cv2.imshow("processed", processed)
cv2.waitKey(0)
