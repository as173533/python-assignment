import cv2

img = cv2.imread("C:/Users/Admin/Downloads/highway-with-cars.jpg")

print("Dimension of original image", img.shape)

scale = 150

width = int(img.shape[1] * scale / 100)
height = int(img.shape[0] * scale / 100)

dim = (width, height)
resized_img = cv2.resize(img, dim, interpolation = cv2.INTER_LINEAR)

print("Dimension of resized image", resized_img.shape)

cv2.imshow("Original Image", img)
cv2.imshow("Resized Image", resized_img)

cv2.waitKey(0)
cv2.destroyAllWindows()