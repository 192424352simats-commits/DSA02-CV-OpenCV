import cv2

img = cv2.imread("watch.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = cv2.GaussianBlur(gray, (5, 5), 0)

circles = cv2.HoughCircles(
    gray,
    cv2.HOUGH_GRADIENT,
    dp=1.2,
    minDist=50,
    param1=100,
    param2=50,
    minRadius=20,
    maxRadius=300
)

if circles is not None:
    circles = circles[0]

    for x, y, r in circles:
        cv2.circle(img, (int(x), int(y)), int(r), (0, 255, 0), 3)
        cv2.putText(img, "WATCH",
                    (int(x) - 50, int(y)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 255, 0), 2)

cv2.imshow("Watch Recognition", img)

cv2.waitKey(0)
cv2.destroyAllWindows()