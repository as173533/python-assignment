import cv2
import numpy as np

img = cv2.imread("C:/Users/Admin/Downloads/highway-with-cars.jpg")

column = img.shape[1]
row = img.shape[0]

center = (column//2,row//2)
angle = 307

r = cv2.getRotationMatrix2D(center,angle,1)

rotated = cv2.warpAffine(img,r,(column,row))

cv2.imshow("Rotated",rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()