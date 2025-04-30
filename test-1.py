from PIL import Image, ImageFilter

# Open the image
image = Image.open("your_image.jpg")

# Apply Gaussian Blur
blurred_image = image.filter(ImageFilter.GaussianBlur(radius=15))  # You can increase radius for more blur

# Save the blurred image
blurred_image.save("blurred_image.jpg")

# Optional: Show the blurred image
blurred_image.show()