import cv2
import numpy as np

# Step 1: Read the original image
image = cv2.imread('your_image.jpg')

# Step 2: Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 3: Apply Histogram Equalization
equalized = cv2.equalizeHist(gray)

# Step 4: Stack original and equalized side by side for comparison
comparison = np.hstack((gray, equalized))

# Step 5: Save and show the result
cv2.imwrite("histogram_equalization_comparison.jpg", comparison)

cv2.imshow('Original vs Equalized', comparison)
cv2.waitKey(0)
cv2.destroyAllWindows()
