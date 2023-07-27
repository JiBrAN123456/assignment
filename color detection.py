import cv2
import numpy as np


image_1 = cv2.imread("\\Users\yunis\PycharmProjects\pythonProject1\images\green.png")
image_2 = cv2.imread("\\Users\yunis\PycharmProjects\pythonProject1\images\BLUE.jpg")
image_3 = cv2.imread("\\Users\yunis\PycharmProjects\pythonProject1\images\RED.jpg")


#for green
lower_colorg = np.array([40, 40, 40])
upper_colorg = np.array([80, 255, 255])

hsv_green = cv2.cvtColor(image_1, cv2.COLOR_BGR2HSV)


mask = cv2.inRange(hsv_green, lower_colorg, upper_colorg)


cv2.imshow("hsvgreen",mask)

cv2.imshow("image1", image_1)



#for blue
lower_colorb = np.array([90, 40, 40])
upper_colorb = np.array([150, 255, 255])

hsv_blue = cv2.cvtColor(image_2, cv2.COLOR_BGR2HSV)


maskblue = cv2.inRange(hsv_blue, lower_colorb, upper_colorb)




cv2.imshow("hsvblue",maskblue)
cv2.imshow("image2", image_2)

#for red

lower_colorr = np.array([0, 120, 70])
upper_colorr = np.array([180, 255, 255])

hsv_red = cv2.cvtColor(image_3, cv2.COLOR_BGR2HSV)


maskred = cv2.inRange(hsv_red, lower_colorr, upper_colorr)




cv2.imshow("hsvred",maskred)
cv2.imshow("image3", image_3)



cv2.waitKey(0)
