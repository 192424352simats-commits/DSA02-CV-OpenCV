import cv2
import numpy as np

img = cv2.imread("image.jpg")

kernel = np.array([
    [1,  1, 1],
    [1, -8, 1],
    [1,  1, 1]
], dtype=np.float32)

laplacian = cv2.filter2D(img, -1, kernel)
sharpened = cv2.subtract(img, laplacian)

cv2.imshow("Original", img)
cv2.imshow("Sharpened", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()