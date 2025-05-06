import cv2
# Load the image
img = cv2.imread("your_image.jpg")
# Rotate 90 degrees clockwise
rotated_img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
flipped_img=cv2.rotate(rotated_img,cv2.ROTATE_90_CLOCKWISE)
cv2.imwrite("Flipped image.jpg",flipped_img)
# Display the rotated image
cv2.imshow("Flipped Image", flipped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()