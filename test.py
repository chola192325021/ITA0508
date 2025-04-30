from PIL import Image

# Load the image
image = Image.open("your_image.jpg")

# Convert to grayscale
gray_image = image.convert("L")

# Save the grayscale image
gray_image.save("gray_image.jpg")

# Optional: Show the image
gray_image.show()
