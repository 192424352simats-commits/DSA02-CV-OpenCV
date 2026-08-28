import cv2

img1 = cv2.imread("image.jpg")
img2 = cv2.imread("image2.jpg")

crop = img1[100:300, 100:300]

img2[50:250, 50:250] = crop

cv2.imshow("Cropped Image", crop)
cv2.imshow("Pasted Image", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()