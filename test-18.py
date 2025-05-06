import cv2
import numpy as np

def apply_erosion(image):
    # Load the image
    image = cv2.imread("your_image.jpg")

    if image is None:
        print("Error: Could not read the image.")
        return

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply binary threshold
    ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Check if binary is valid
    if binary is None or not isinstance(binary, np.ndarray):
        print("Error: Binary image creation failed.")
        return

    # Create kernel
    kernel = np.ones((5, 5), np.uint8)

    # Apply erosion
    eroded = cv2.erode(binary, kernel, iterations=1)

    # Save the result
    cv2.imwrite("Morphological Erosion.jpg", eroded)
    cv2.imwrite("Morphological Erosion-Binary.jpg", binary)
    # Show the images
    cv2.imshow("Original", image)
    cv2.imshow("Binary", binary)
    cv2.imshow("Eroded", eroded)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
apply_erosion("your_image.jpg")  # Replace with your actual file name
