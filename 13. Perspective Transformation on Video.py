import cv2
import numpy as np

cap = cv2.VideoCapture("video.mp4")

pts1 = np.float32([
    [100, 100],
    [500, 100],
    [100, 400],
    [500, 400]
])

pts2 = np.float32([
    [0, 0],
    [400, 0],
    [0, 400],
    [400, 400]
])

M = cv2.getPerspectiveTransform(pts1, pts2)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    transformed = cv2.warpPerspective(frame, M, (400, 400))

    cv2.imshow("Original Video", frame)
    cv2.imshow("Perspective Video", transformed)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()