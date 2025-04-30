import cv2
import numpy as np

def save_color_histogram():
    # Ask user for the image file name
    image_path = input("Enter the image file name (e.g., 'your_image.jpg'): ")

    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Could not read the image. Please check the file name and path.")
        return

    # Split the image into its Blue, Green, and Red channels
    (b, g, r) = cv2.split(image)

    # Calculate histograms for each channel
    hist_b = cv2.calcHist([b], [0], None, [256], [0, 256])
    hist_g = cv2.calcHist([g], [0], None, [256], [0, 256])
    hist_r = cv2.calcHist([r], [0], None, [256], [0, 256])

    # Normalize histograms for better visualization
    cv2.normalize(hist_b, hist_b, 0, 400, cv2.NORM_MINMAX)
    cv2.normalize(hist_g, hist_g, 0, 400, cv2.NORM_MINMAX)
    cv2.normalize(hist_r, hist_r, 0, 400, cv2.NORM_MINMAX)

    # Create a blank image to draw the histograms
    hist_image = np.zeros((400, 256, 3), dtype=np.uint8)

    # Draw histograms for each channel (Blue, Green, Red)
    for i in range(1, 256):
        cv2.line(hist_image, (i-1, 400-int(hist_b[i-1])), (i, 400-int(hist_b[i])), (255, 0, 0), 1)
        cv2.line(hist_image, (i-1, 400-int(hist_g[i-1])), (i, 400-int(hist_g[i])), (0, 255, 0), 1)
        cv2.line(hist_image, (i-1, 400-int(hist_r[i-1])), (i, 400-int(hist_r[i])), (0, 0, 255), 1)

    # Save the histogram image as 'color_histogram_output.jpg'
    cv2.imwrite("color_histogram_output.jpg", hist_image)
    print("Histogram saved as 'color_histogram_output.jpg'.")

    # Show the original image and the histogram
    cv2.imshow("Original Image", image)
    cv2.imshow("Color Histogram", hist_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Usage
save_color_histogram()
