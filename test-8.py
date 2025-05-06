import cv2

# Load the image
image = cv2.imread('your_image.jpg')

# Resize smaller (shrink to half size)
small = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

# Resize larger (enlarge to 2x size)
large = cv2.resize(image, None, fx=2.0, fy=2.0, interpolation=cv2.INTER_CUBIC)

cv2.imwrite("Smaller image.jpg",small)
cv2.imwrite("Larger image.jpg",large)
# Display results
cv2.imshow("Original", image)
cv2.imshow("Smaller Image", small)
cv2.imshow("Larger Image", large)

cv2.waitKey(0)
cv2.destroyAllWindows()
