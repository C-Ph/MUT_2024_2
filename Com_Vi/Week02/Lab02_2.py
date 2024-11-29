from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

def create_histogram(image_path):
    # Load the image
    image = Image.open(image_path)
    data = np.array(image)

    if len(data.shape) == 3:  # For RGB images
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

    elif len(data.shape) == 2:  # For grayscale images
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

def normalize_chi_squared_value(chi_squared_value, max_possible_value):
    # Normalize the chi-squared value to range 0-1
    return 1 - (chi_squared_value / max_possible_value)

def compare_histograms_chi_squared(histogram1, histogram2, normalize=True):
    chi_squared_value = 0.0  # Initialize chi-squared value

    # Iterate through bins in both histograms
    for bin1, bin2 in zip(histogram1, histogram2):
        expected_value = (bin1 + bin2) / 2  # Calculate the expected value

        if expected_value != 0:  # Avoid division by zero
            squared_difference = (bin1 - bin2) ** 2  # Squared difference
            contribution = squared_difference / expected_value  # Contribution to chi-squared
            chi_squared_value += contribution  # Add contribution to the total

    # Normalize if needed
    if normalize:
        max_possible_value = len(histogram1) * np.max(histogram1)
        chi_squared_value = normalize_chi_squared_value(chi_squared_value, max_possible_value)

    return chi_squared_value

def plot_histograms_and_compare(image_path1, image_path2):
    hist1 = create_histogram(image_path1)
    hist2 = create_histogram(image_path2)

    image1 = Image.open(image_path1)
    image2 = Image.open(image_path2)

    plt.figure(figsize=(16, 10))

    if isinstance(hist1, tuple) and isinstance(hist2, tuple):  # RGB images
        chi_squared_red = compare_histograms_chi_squared(hist1[0], hist2[0])
        chi_squared_green = compare_histograms_chi_squared(hist1[1], hist2[1])
        chi_squared_blue = compare_histograms_chi_squared(hist1[2], hist2[2])

        # Display images
        plt.subplot(3, 3, 1)
        plt.imshow(image1)
        plt.title("Image 1 (RGB)")
        plt.axis("off")

        plt.subplot(3, 3, 2)
        plt.imshow(image2)
        plt.title("Image 2 (RGB)")
        plt.axis("off")

        # Plot histograms with similarity scores
        colors = ['Red', 'Green', 'Blue']
        similarities = [chi_squared_red, chi_squared_green, chi_squared_blue]
        for i, (hist1_channel, hist2_channel, color, similarity) in enumerate(zip(hist1, hist2, colors, similarities)):
            plt.subplot(3, 3, 4 + i)
            plt.plot(hist1_channel, label=f'{color} - Image 1', color=color.lower())
            plt.plot(hist2_channel, label=f'{color} - Image 2', linestyle='dashed', color=color.lower())
            plt.title(f'{color} Histogram Comparison\nSimilarity: {similarity:.2f}')
            plt.xlabel("Pixel Value")
            plt.ylabel("Frequency")
            plt.legend()

    elif isinstance(hist1, np.ndarray) and isinstance(hist2, np.ndarray):  # Grayscale images
        chi_squared_gray = compare_histograms_chi_squared(hist1, hist2)

        print(f"Chi-Squared Test Result (Normalized - Grayscale): {chi_squared_gray:.2f}")

        # Display images
        plt.subplot(2, 2, 1)
        plt.imshow(image1, cmap='gray')
        plt.title("Image 1 (Grayscale)")
        plt.axis("off")

        plt.subplot(2, 2, 2)
        plt.imshow(image2, cmap='gray')
        plt.title("Image 2 (Grayscale)")
        plt.axis("off")

        # Plot histogram with similarity score
        plt.subplot(2, 1, 2)
        plt.plot(hist1, label='Image 1', color='black')
        plt.plot(hist2, label='Image 2', linestyle='dashed', color='gray')
        plt.title(f'Grayscale Histogram Comparison\nSimilarity: {chi_squared_gray:.2f}')
        plt.xlabel("Pixel Value")
        plt.ylabel("Frequency")
        plt.legend()

    else:
        print("Cannot compare histograms. Unsupported format.")
        return

    # Show the plots
    plt.tight_layout()
    plt.show()

# Example usage
plot_histograms_and_compare('cat.jpg', 'catG.jpg')  # Compare two images



