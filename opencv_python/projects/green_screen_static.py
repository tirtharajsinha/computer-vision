import cv2
import numpy as np
import stackimages
import os

stock_path = os.path.dirname(os.getcwd()) + "\\"
# to import it get stockimages.py file

###############################
# static input image
bg = cv2.imread(stock_path + "stock/bg.jpg")
frame = cv2.imread(stock_path + "stock/greenscreen.jpg")
#################################

bg_image = cv2.resize(bg, (640, 480))
frame = cv2.resize(frame, (640, 480))


def empty(a):
    pass


cv2.namedWindow("trackbars")
cv2.resizeWindow("trackbars", 640, 240)
cv2.createTrackbar("hue min", "trackbars", 49, 179, empty)
cv2.createTrackbar("hue max", "trackbars", 62, 179, empty)
cv2.createTrackbar("sat min", "trackbars", 49, 255, empty)
cv2.createTrackbar("sat max", "trackbars", 255, 255, empty)
cv2.createTrackbar("val min", "trackbars", 87, 255, empty)
cv2.createTrackbar("val max", "trackbars", 255, 255, empty)
path = 'stock/mclaren-720s_0.jpg'

while True:
    img = frame.copy()

    imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("hue min", "trackbars")
    h_max = cv2.getTrackbarPos("hue max", "trackbars")
    s_min = cv2.getTrackbarPos("sat min", "trackbars")
    s_max = cv2.getTrackbarPos("sat max", "trackbars")
    v_min = cv2.getTrackbarPos("val min", "trackbars")
    v_max = cv2.getTrackbarPos("val max", "trackbars")
    print(h_min, h_max, s_min, s_max, v_min, v_max)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imghsv, lower, upper)
    overlapped = cv2.bitwise_and(img, img, mask=mask)

    final = img - overlapped
    final = np.where(final == 0, bg_image, final)
    imgstack = stackimages.stackImages(0.6, [[img, overlapped], [mask, final]])
    cv2.imshow("stacked image", imgstack)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
