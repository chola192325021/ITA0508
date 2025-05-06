import cv2
import numpy as np

def apply_dilation(image):
    # Load the image
    image = cv2.imread("your_image.jpg")

    if image is None:
        print("Error: Could not read the image.")
        return

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply binary threshold
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Create a kernel
    kernel = np.ones((5, 5), np.uint8)

    # Apply dilation
    dilated = cv2.dilate(binary, kernel, iterations=1)

    # Save the result
    cv2.imwrite("MOrphological Dilated.jpg", dilated)

    # Display the results
    cv2.imshow("Original Image", image)
    cv2.imshow("Binary Image", binary)
    cv2.imshow("Dilated Image", dilated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
apply_dilation("your_image.jpg")  # Replace with your image file name
