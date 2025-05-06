import cv2
# Load the image
img = cv2.imread("your_image.jpg")
# Rotate 90 degrees clockwise
flip270_img=cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imwrite("Flipped 270 image.jpg",flip270_img)
# Display the rotated image
cv2.imshow("Flipped Image", flip270_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
