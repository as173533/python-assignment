import cv2

video = cv2.VideoCapture(0)

while video.isOpened():
    _, frame = video.read()
    cv2.imshow("Live", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()