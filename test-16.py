import cv2

def add_watermark( image,watermark_text):
    # Load the original image
    image = cv2.imread("your_image.jpg")

    if image is None:
        print("Error: Could not read the image.")
        return

    # Get image dimensions
    height, width = image.shape[:2]

    # Choose font, scale, color, and thickness
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_color = (255, 255, 255)  # white
    thickness = 2

    # Get the size of the text box
    text_size, _ = cv2.getTextSize(watermark_text, font, font_scale, thickness)
    text_width, text_height = text_size

    # Set text position (bottom-right corner with padding)
    x = width - text_width - 10
    y = height - 10

    # Create a copy of the image to overlay text with transparency
    overlay = image.copy()

    # Add text to the overlay
    cv2.putText(overlay, watermark_text, (x, y), font, font_scale, font_color, thickness, cv2.LINE_AA)

    # Blend original image and overlay using transparency
    alpha = 0.5  # Transparency factor
    watermarked = cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0)

    # Save the output
    cv2.imwrite("Watermarked Image.jpg", watermarked)


    # Display the result
    cv2.imshow("Watermarked Image", watermarked)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
add_watermark("your_image.jpg", "@ Naruto Uzumaki!")
