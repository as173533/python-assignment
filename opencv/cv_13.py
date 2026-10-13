import cv2

video = cv2.VideoCapture("C:/Users/Admin/Downloads/demo.mp4")
while video.isOpened():
    _, frame = video.read()
    frame = cv2.resize(frame, (500, 500))

    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()