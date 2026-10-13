import cv2
import numpy as np

img = cv2.imread("C:/Users/Admin/Downloads/highway-with-cars.jpg")

width = 600
height = 850
resized_img = cv2.resize(img, (width, height))

kernel = np.ones((5, 5), dtype='uint8')

# erosion = cv2.erode(resized_img, kernel, iterations=1)
# dilation = cv2.dilate(resized_img, kernel, iterations=1)

# opening = cv2.morphologyEx(resized_img, cv2.MORPH_OPEN, kernel)
# closing = cv2.morphologyEx(resized_img, cv2.MORPH_CLOSE, kernel)

# gradient = cv2.morphologyEx(resized_img, cv2.MORPH_GRADIENT, kernel)

tophat = cv2.morphologyEx(resized_img, cv2.MORPH_TOPHAT, kernel)
tophat = cv2.morphologyEx(resized_img, cv2.MORPH_BLACKHAT, kernel)

cv2.imshow("Original", resized_img)
# cv2.imshow("Eroded", erosion)
# cv2.imshow("Dilated", dilation)
# cv2.imshow("Opening", opening)
# cv2.imshow("Closing", closing)
# cv2.imshow("Gradient", gradient)
cv2.imshow("Tophat", tophat)
cv2.imshow("Blackhat", tophat)

cv2.waitKey(0)
cv2.destroyAllWindows()