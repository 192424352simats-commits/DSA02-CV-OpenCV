import cv2

img = cv2.imread("image.jpg")

blur = cv2.GaussianBlur(img, (5, 5), 0)

unsharp = cv2.addWeighted(img, 1.5, blur, -0.5, 0)

cv2.imshow("Original", img)
cv2.imshow("Unsharp Masking", unsharp)

cv2.waitKey(0)
cv2.destroyAllWindows()