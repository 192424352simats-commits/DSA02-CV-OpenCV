import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Web Camera", frame)

    key = cv2.waitKey(50) & 0xFF

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()