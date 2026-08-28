import cv2

img = cv2.imread("image.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
gy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

gradient = cv2.magnitude(gx, gy)
gradient = cv2.convertScaleAbs(gradient)

gradient = cv2.GaussianBlur(gradient, (5, 5), 0)

sharpened = cv2.addWeighted(gray, 1.0, gradient, 1.0, 0)

cv2.imshow("Original", gray)
cv2.imshow("Gradient Masking", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()