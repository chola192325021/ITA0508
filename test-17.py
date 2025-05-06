import cv2

def crop_copy_paste_roi(image):
    # Load the image
    image = cv2.imread("your_image.jpg")

    if image is None:
        print("Error: Could not read the image.")
        return

    # Show the original image
    cv2.imshow("Original Image", image)

    # Define the Region of Interest (ROI) - adjust the values as needed
    # Format: image[y1:y2, x1:x2]
    roi = image[50:150, 100:200]  # example ROI (100x100 pixels from specific region)

    # Optional: display the ROI
    cv2.imshow("Cropped ROI", roi)

    # Paste the ROI at a new location in the same image (e.g., top-left corner)
    image[0:100, 0:100] = roi

    # Save the modified image
    cv2.imwrite("ROI Cropped.jpg", image)
  
    # Show the modified image
    cv2.imshow("Modified Image with ROI", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
crop_copy_paste_roi("your_image.jpg")
