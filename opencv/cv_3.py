import cv2

img = cv2.imread("C:/Users/Admin/Downloads/highway-with-cars.jpg")

width = 600
height = 850
resized_img = cv2.resize(img, (width, height))
print("size: ", img.size)
print("Resized size: ", resized_img.size)
cv2.imshow("Original Image", img)

cv2.imshow("Resized Image", resized_img)

# flipped_img = cv2.flip(resized_img, 1)
# cv2.imshow("Flipped Image", flipped_img)
#
# flipped_ver_img = cv2.flip(resized_img, 0)
# cv2.imshow("Flipped vertical Image", flipped_ver_img)

flipped_ver_hor_img = cv2.flip(resized_img, -1)
cv2.imshow("Flipped Horizontal & vertical Image", flipped_ver_hor_img)

cv2.waitKey(0)
cv2.destroyAllWindows()