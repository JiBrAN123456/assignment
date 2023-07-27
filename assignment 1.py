import cv2
import numpy as np


def function(img_path,save_path):

   image = cv2.imread(img_path)

   grey_image = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)

   blurred_image = cv2.GaussianBlur(grey_image,(3,3),0)

   edges =  cv2.Canny(blurred_image,threshold1= 30,threshold2=60)

   contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

   image_with_contours = image.copy()
   cv2.drawContours(image_with_contours, contours, -1, (0, 255, 0), 2)


   cv2.imwrite(save_path, image_with_contours)
   cv2.imshow("result",image_with_contours)
   cv2.waitKey(0)

inputimage = "\\Users\yunis\PycharmProjects\pythonProject1\images\green.png"

outputimage = "\\Users\yunis\PycharmProjects\pythonProject1\images\greenprocessed.png"

function(inputimage, outputimage)






