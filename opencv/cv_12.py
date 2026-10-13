#canny EDGE Detection
#1 Noise reduction
#2 Intensity of gradient
#3 Non-Maximum suppression
#4 Thresholding

import cv2
import numpy as np

img = cv2.imread("C:/Users/Admin/Downloads/highway-with-cars.jpg")
resized_img = cv2.resize(img, (500, 500))

min_thresh = 100
max_thresh = 200
edges = cv2.Canny(resized_img, min_thresh, max_thresh)

cv2.imshow("Original", resized_img)
cv2.imshow("Edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()


