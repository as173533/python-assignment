#CHANNEL --> 0 to 255
import cv2
import numpy as np

img = cv2.imread("C:/Users/Admin/Downloads/highway-with-cars.jpg",0)

threshlod_value = 100

_,binary_threshold = cv2.threshold(img, threshlod_value, 255, cv2.THRESH_BINARY)

cv2.imshow("Original ",img)
cv2.imshow("Binary Threshold", binary_threshold)

cv2.waitKey(0)
cv2.destroyAllWindows()