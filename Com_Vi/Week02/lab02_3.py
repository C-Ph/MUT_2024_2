import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Read the image
img = cv.imread("Ph.jpg")
if img is None:
    print("Could not open or find the image")
    exit(0)

# Resize image
scale_percent = 100  # percent of original size
width = int(img.shape[1] * scale_percent / 400)
height = int(img.shape[0] * scale_percent / 400)
dim = (width, height)
src = cv.resize(img, dim, interpolation=cv.INTER_AREA)

# Convert to grayscale
src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

# Apply Histogram Equalization
equalized_img = cv.equalizeHist(src_gray)

# Function to plot histograms
def plot_histogram(image, title, color):
    hist = cv.calcHist([image], [0], None, [256], [0, 256])
    plt.plot(hist, color=color)
    plt.title(title)
    plt.xlabel("Pixel Value")
    plt.ylabel("Frequency")
    plt.grid()

# Plot images and histograms
plt.figure(figsize=(10, 6))

# Original Grayscale Image
plt.subplot(2, 2, 1)
plt.imshow(src_gray, cmap='gray')
plt.title("Original Grayscale Image")
plt.axis("off")

plt.subplot(2, 2, 2)
plot_histogram(src_gray, "Histogram: Original", color='gray')

# Equalized Image
plt.subplot(2, 2, 3)
plt.imshow(equalized_img, cmap='gray')
plt.title("Equalized Image")
plt.axis("off")

plt.subplot(2, 2, 4)
plot_histogram(equalized_img, "Histogram: Equalized", color='blue')

plt.tight_layout()
plt.show()

# Show images using OpenCV (optional)
cv.imshow("Original Grayscale Image", src_gray)
cv.imshow("Equalized Image", equalized_img)
cv.waitKey(0)
cv.destroyAllWindows()