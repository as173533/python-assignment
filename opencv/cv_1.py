from email.mime import image

import cv2

img = cv2.imread("C:/Users/Admin/Downloads/highway-with-cars.jpg",0)

print("Dimension of the image: ",img.shape)

# width = img.shape[1]
width = 1000
height = 400
# height = img.shape[0]
dim = (width, height)
resized = cv2.resize(img, dim,)

cv2.imshow("img", resized)
# cv2.imwrite("C:/Users/Admin/Downloads/cars.jpg", img)
cv2.waitKey(0)    
cv2.destroyAllWindows()

