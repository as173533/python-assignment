import cv2

video = cv2.VideoCapture("C:/Users/Admin/Downloads/demo.mp4")

fourcc = cv2.VideoWriter_fourcc(*'mp4v')

output = cv2.VideoWriter('output.mp4', fourcc, 30, (480, 270))

while video.isOpened():
    ret, frame = video.read()
    if ret:
        output.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cv2.destroyAllWindows()

