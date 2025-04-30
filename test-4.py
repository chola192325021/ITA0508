import cv2
import matplotlib.pyplot as plt

def analyze_color_histogram(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Define color channels
    color_channels = ('b', 'g', 'r')  # OpenCV uses BGR

    plt.figure(figsize=(10, 5))
    plt.title("Color Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")

    # Plot histogram for each channel
    for i, color in enumerate(color_channels):
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])

    plt.legend(['Blue', 'Green', 'Red'])
    plt.grid(True)
    plt.tight_layout()
    plt.show()
