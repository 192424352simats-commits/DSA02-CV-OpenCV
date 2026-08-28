import cv2
import numpy as np

img = cv2.imread("image.jpg")

pts1 = np.float32([
    [50, 50],
    [400, 50],
    [50, 400],
    [400, 400]
])

pts2 = np.float32([
    [0, 0],
    [400, 0],
    [0, 400],
    [400, 400]
])

M = cv2.getPerspectiveTransform(pts1, pts2)

perspective = cv2.warpPerspective(img, M, (400, 400))

cv2.imshow("Original", img)
cv2.imshow("Perspective", perspective)

cv2.waitKey(0)
cv2.destroyAllWindows()