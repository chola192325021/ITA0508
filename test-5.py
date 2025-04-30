import cv2
import numpy as np

# Step 1: Read the image
image = cv2.imread("your_image.jpg")

# Optional: Convert to grayscale (if needed)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 2: Create a kernel (structuring element)
kernel = np.ones((5, 5), np.uint8)  # You can change the size

# Step 3: Apply erosion
eroded = cv2.erode(gray, kernel, iterations=1)

# Step 4: Save and display results
cv2.imwrite("eroded_image.jpg", eroded)

cv2.imshow("Original", gray)
cv2.imshow("Eroded Image", eroded)
cv2.waitKey(0)
cv2.destroyAllWindows()
