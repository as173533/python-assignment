import cv2
import numpy as np

img = cv2.imread("C:/Users/Admin/Downloads/highway-with-cars.jpg")

resized_img = cv2.resize(img,(500,500))

ksize = 3


blur = cv2.medianBlur(resized_img,ksize)

cv2.imshow("Input",resized_img)
cv2.imshow("Output",blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
