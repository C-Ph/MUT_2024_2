import numpy as np
import cv2
from scipy.ndimage import convolve
import matplotlib.pyplot as plt

# Gaussian Filter
def gaussian_filter(image, kernel_size=5, sigma=1.0):
    ax = np.linspace(-(kernel_size // 2), kernel_size // 2, kernel_size)
    gauss = np.exp(-0.5 * np.square(ax) / np.square(sigma))
    kernel = np.outer(gauss, gauss)
    kernel /= np.sum(kernel)
    return convolve(image, kernel)

# Sobel Filter
def sobel_filters(image):
    Kx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])  # Horizontal
    Ky = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])  # Vertical
    Gx = convolve(image, Kx)
    Gy = convolve(image, Ky)
    magnitude = np.sqrt(Gx**2 + Gy**2)
    direction = np.arctan2(Gy, Gx)  # Gradient direction
    return magnitude, direction

# Non-Maximum Suppression
def non_maximum_suppression(magnitude, direction):
    rows, cols = magnitude.shape
    suppressed = np.zeros((rows, cols), dtype=np.float32)
    direction = np.rad2deg(direction)
    direction[direction < 0] += 180

    for i in range(1, rows-1):
        for j in range(1, cols-1):
            # Direction quantization
            if (0 <= direction[i, j] < 22.5) or (157.5 <= direction[i, j] <= 180):
                neighbors = (magnitude[i, j+1], magnitude[i, j-1])
            elif 22.5 <= direction[i, j] < 67.5:
                neighbors = (magnitude[i-1, j+1], magnitude[i+1, j-1])
            elif 67.5 <= direction[i, j] < 112.5:
                neighbors = (magnitude[i+1, j], magnitude[i-1, j])
            else:  # 112.5 <= direction < 157.5
                neighbors = (magnitude[i-1, j-1], magnitude[i+1, j+1])

            # Suppress non-maximum values
            if magnitude[i, j] >= neighbors[0] and magnitude[i, j] >= neighbors[1]:
                suppressed[i, j] = magnitude[i, j]
            else:
                suppressed[i, j] = 0

    return suppressed

# Double Threshold
def double_threshold(suppressed, low_threshold, high_threshold):
    strong = 255
    weak = 75

    strong_i, strong_j = np.where(suppressed >= high_threshold)
    weak_i, weak_j = np.where((suppressed <= high_threshold) & (suppressed >= low_threshold))

    result = np.zeros_like(suppressed, dtype=np.uint8)
    result[strong_i, strong_j] = strong
    result[weak_i, weak_j] = weak
    return result, weak, strong

# Edge Tracking by Hysteresis
def edge_tracking_by_hysteresis(image, weak, strong):
    rows, cols = image.shape
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            if image[i, j] == weak:
                if (strong in [image[i+1, j-1], image[i+1, j], image[i+1, j+1],
                               image[i, j-1], image[i, j+1],
                               image[i-1, j-1], image[i-1, j], image[i-1, j+1]]):
                    image[i, j] = strong
                else:
                    image[i, j] = 0
    return image

# Main Function for Canny Edge Detection
def canny_edge_detection(image, low_threshold, high_threshold):
    # 1. Step 1: Gaussian Blur
    smoothed = gaussian_filter(image)

    # 2. Step 2: Sobel Filters
    magnitude, direction = sobel_filters(smoothed)

    # 3. Step 3: Non-Maximum Suppression
    suppressed = non_maximum_suppression(magnitude, direction)

    # 4. Step 4: Double Thresholding
    thresholded, weak, strong = double_threshold(suppressed, low_threshold, high_threshold)

    # 5. Step 5: Edge Tracking by Hysteresis
    final_edges = edge_tracking_by_hysteresis(thresholded, weak, strong)

    return final_edges

image = cv2.imread('file\imgg.jpg', cv2.IMREAD_GRAYSCALE)
image = np.float32(image)

edges = canny_edge_detection(image, low_threshold=50, high_threshold=150)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')

plt.subplot(1, 2, 2)
plt.title('Canny Edge Detection')
plt.imshow(edges, cmap='gray')
plt.show()