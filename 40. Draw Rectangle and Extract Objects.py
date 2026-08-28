import cv2

img = cv2.imread("image.jpg")

x1, y1 = 100, 100
x2, y2 = 400, 400

cv2.rectangle(
    img,
    (x1, y1),
    (x2, y2),
    (0, 255, 0),
    2
)

object_img = img[y1:y2, x1:x2]

cv2.imshow("Original with Rectangle", img)
cv2.imshow("Extracted Object", object_img)

cv2.waitKey(0)
cv2.destroyAllWindows()