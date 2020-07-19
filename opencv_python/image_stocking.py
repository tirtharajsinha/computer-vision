import cv2
import numpy as np
# img=cv2.imread("stock/cvimg3.jpg")
#img1=cv2.imread("stock/cvimg2.jpg")

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver
img=cv2.imread("stock/cvimg2.jpg")
img1=cv2.imread("stock/cvimg3.jpg")
img2=cv2.imread("stock/cvimg4.jpg")
img3=cv2.imread("stock/cvimg5.jpg")
img4=cv2.imread("stock/cvtest.jpg")
img5=cv2.imread("stock/cvimg.jpg")

imgstack=stackImages(0.5,([img,img1,img2],[img3,img4,img5]))

# hor=np.hstack((img,img))
# ver=np.vstack((img,img))
#
#
# cv2.imshow("horizontal",hor)
# cv2.imshow("vertical",ver)
cv2.imshow("stacked",imgstack)

cv2.waitKey(0)