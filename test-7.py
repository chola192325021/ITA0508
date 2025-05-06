import cv2
import numpy as np

# Step 1: Read the image
image = cv2.imread('your_image.jpg', cv2.IMREAD_GRAYSCALE)

# Step 2: Define a kernel (structuring element)
kernel = np.ones((5, 5), np.uint8)

# Step 3: Dilate the image
dilated_image = cv2.dilate(image, kernel, iterations=1)

cv2.imwrite('Dilated image.jpg',dilated_image)
# Step 4: Show the original and dilated images
cv2.imshow('Original Image', image)
cv2.imshow('Dilated Image', dilated_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
