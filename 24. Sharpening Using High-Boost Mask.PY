import cv2

img = cv2.imread("image.jpg")

blur = cv2.GaussianBlur(img, (5, 5), 0)

A = 2.0

high_boost = cv2.addWeighted(img, A, blur, -(A - 1), 0)

cv2.imshow("Original", img)
cv2.imshow("High Boost", high_boost)

cv2.waitKey(0)
cv2.destroyAllWindows()