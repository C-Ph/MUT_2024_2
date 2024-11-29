from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def create_histogram(image_path):
    # Load the image
    image = Image.open(image_path)
    data = np.array(image)

    if len(data.shape) == 3:  # RGB Image
        # Initialize histograms
        histogramRed = np.zeros(256)
        histogramGreen = np.zeros(256)
        histogramBlue = np.zeros(256)

        # Update histograms
        for row in data:
            for pixel in row:
                r, g, b = pixel[:3]
                histogramRed[r] += 1
                histogramGreen[g] += 1
                histogramBlue[b] += 1

        return histogramRed, histogramGreen, histogramBlue

    elif len(data.shape) == 2:  # Grayscale Image
        # Initialize histogram
        histogramGray = np.zeros(256)

        # Update histogram
        for row in data:
            for pixel in row:
                histogramGray[pixel] += 1

        return histogramGray

    else:
        print("Unsupported image format")
        return None

def plot_comparison(image_paths, titles):
    # Create a figure with two subplots per image (1 for image and 1 for histogram)
    fig, axes = plt.subplots(len(image_paths), 2, figsize=(12, 8))
    for i, (image_path, title) in enumerate(zip(image_paths, titles)):
        # Load and display the image
        image = Image.open(image_path)
        axes[i, 0].imshow(image)
        axes[i, 0].set_title(title)
        axes[i, 0].axis('off')

        # Generate the histogram
        histograms = create_histogram(image_path)
        if isinstance(histograms, tuple):  # RGB Image
            histogramRed, histogramGreen, histogramBlue = histograms
            axes[i, 1].plot(histogramRed, color='red', label='Red')
            axes[i, 1].plot(histogramGreen, color='green', label='Green')
            axes[i, 1].plot(histogramBlue, color='blue', label='Blue')
        elif isinstance(histograms, np.ndarray):  # Grayscale Image
            axes[i, 1].plot(histograms, color='gray', label='Gray')

        # Customize the histogram plot
        axes[i, 1].set_xlabel("Pixel Level")
        axes[i, 1].set_ylabel("Frequency")
        axes[i, 1].legend()
        axes[i, 1].grid()

    plt.tight_layout()
    plt.show()

# Example usage:
image_files = ['cat.jpg', 'catG.jpg']  # Replace with your images
titles = ['RGB', 'Grayscale']  # Example titles
plot_comparison(image_files, titles)

