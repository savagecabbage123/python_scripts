import cv2
print("Version")
print(cv2.__version__)
image = cv2.imread("butterfly.jpg")
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("cool butterfly", image)
cv2.imshow("gray butterfly", gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()