import cv2

img =cv2.imread(r"C:\Users\kumar\Downloads\shinkansen.jpg")
cv2.imshow("img1.jpg", img)
cv2.imwrite("img2.png", img)
cv2.imwrite("img3.tiff", img)
cv2.imshow("img2.png", img)
cv2.imshow("img3.tiff", img)
cv2.waitKey(0)