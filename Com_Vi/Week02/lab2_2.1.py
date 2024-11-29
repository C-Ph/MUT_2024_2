from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def create_histogram(image_path):
    # Load the image
    image = Image.open(image_path)
    data = np.array(image)

    # Check for grayscale or RGB image
    if len(data.shape) == 3:  # RGB Image
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

        # Normalize the histograms
        total_pixels = data.shape[0] * data.shape[1]
        histogramRed /= total_pixels
        histogramGreen /= total_pixels
        histogramBlue /= total_pixels

        return histogramRed, histogramGreen, histogramBlue

    elif len(data.shape) == 2:  # Grayscale Image
        histogramGray = np.zeros(256)

        # Update histogram
        for row in data:
            for pixel in row:
                histogramGray[pixel] += 1

        # Normalize the histogram
        total_pixels = data.shape[0] * data.shape[1]
        histogramGray /= total_pixels

        return histogramGray

    else:
        print("Unsupported image format")
        return None

def compare_histograms_chi_squared(histogram1, histogram2):
    chi_squared_value = 0.0  # Initialize chi-squared value
    
    # Iterate through bins in both histograms
    for bin1, bin2 in zip(histogram1, histogram2):
        expected_value = (bin1 + bin2) / 2  # Calculate the expected value

        if expected_value > 0:  # Avoid division by zero
            squared_difference = (bin1 - bin2) ** 2  # Squared difference
            contribution = squared_difference / expected_value  # Contribution to chi-squared
            chi_squared_value += contribution  # Add contribution to the total

    return chi_squared_value

def plot_histograms(histogram1, histogram2, title1="Image1", title2="Image2"):
    # Plot histograms for comparison
    plt.figure(figsize=(10, 5))

    # Plot for Image 1
    plt.subplot(1, 2, 1)
    plt.plot(histogram1, color='blue', label='Histogram')
    plt.title(title1)
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Normalized Frequency")
    plt.legend()

    # Plot for Image 2
    plt.subplot(1, 2, 2)
    plt.plot(histogram2, color='red', label='Histogram')
    plt.title(title2)
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Normalized Frequency")
    plt.legend()

    plt.tight_layout()
    plt.show()

def main(image_path1, image_path2):
    # Step 1: Load images and calculate histograms
    hist1 = create_histogram(image_path1)
    hist2 = create_histogram(image_path2)

    if isinstance(hist1, tuple) and isinstance(hist2, tuple):  # RGB images
        hist1R, hist1G, hist1B = hist1
        hist2R, hist2G, hist2B = hist2

        # Calculate Chi-Squared for RGB channels
        chi_squared_R = compare_histograms_chi_squared(hist1R, hist2R)
        chi_squared_G = compare_histograms_chi_squared(hist1G, hist2G)
        chi_squared_B = compare_histograms_chi_squared(hist1B, hist2B)
        
        print(f"Chi-Squared (Red): {chi_squared_R}")
        print(f"Chi-Squared (Green): {chi_squared_G}")
        print(f"Chi-Squared (Blue): {chi_squared_B}")

        # Plot histograms for each channel
        plot_histograms(hist1R, hist2R, title1="Image1 - Red Channel", title2="Image2 - Red Channel")
        plot_histograms(hist1G, hist2G, title1="Image1 - Green Channel", title2="Image2 - Green Channel")
        plot_histograms(hist1B, hist2B, title1="Image1 - Blue Channel", title2="Image2 - Blue Channel")

    elif isinstance(hist1, np.ndarray) and isinstance(hist2, np.ndarray):  # Grayscale images
        chi_squared = compare_histograms_chi_squared(hist1, hist2)
        
        print(f"Chi-Squared (Grayscale): {chi_squared}")

        # Plot grayscale histograms
        plot_histograms(hist1, hist2, title1="Image1 - Grayscale", title2="Image2 - Grayscale")

# Example usage (ensure to replace with actual image paths)
image_file1 = 'cat.jpg'  # Replace with actual image path
image_file2 = 'catG.jpg'  # Replace with actual image path
main(image_file1, image_file2)