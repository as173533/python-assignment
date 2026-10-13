import cv2
import numpy as np

img = cv2.imread("C:/Users/Admin/Downloads/highway-with-cars.jpg")

resized_img = cv2.resize(img,(500,500))

ksize = (7,7)

sigmax = 0
sigmay = 0

blur = cv2.GaussianBlur(resized_img,ksize,sigmax)

cv2.imshow("Input",resized_img)
cv2.imshow("Output",blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
