import cv2
import numpy as np

img = cv2.imread("C:/Users/Admin/Downloads/highway-with-cars.jpg")

resized_img = cv2.resize(img, (500, 500))

d =7

sigmacolor = 100
sigmaspace = 100

b = cv2.bilateralFilter(resized_img, d, sigmacolor, sigmaspace)

cv2.imshow("Input", resized_img)
cv2.imshow("Output", b)

cv2.waitKey(0)
cv2.destroyAllWindows()

