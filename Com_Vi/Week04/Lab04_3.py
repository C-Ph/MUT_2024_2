import numpy as np
import cv2
from matplotlib import pyplot as plt

image = np.array([
    [7, 2, 3, 3, 8],
    [4, 5, 3, 8, 4],
    [3, 3, 2, 8, 4],
    [2, 8, 7, 2, 7],
    [5, 4, 4, 5, 4]
])

kernel = np.array([
    [1, 0, -1],
    [1, 0, -1],
    [1, 0, -1]
])

# Convolution function
def convolve2d_no_padding(image, kernel):
    kernel_height, kernel_width = kernel.shape
    image_height, image_width = image.shape
    
    # size calculation (without padding)
    output_height = image_height - kernel_height + 1
    output_width = image_width - kernel_width + 1
    
    # Prepare the output array
    output = np.zeros((output_height, output_width), dtype=int)
    
    # Perform the convolution
    for i in range(output_height):
        for j in range(output_width):
            region = image[i:i + kernel_height, j:j + kernel_width]
            output[i, j] = np.sum(region * kernel)
    
    return output

# Perform convolution
output_image = convolve2d_no_padding(image, kernel)

img = cv2.imread('D:/COD_E/001_Project/CLASS_2024/Comvi/Week04/me.jpg')

# Create a list of kernel sizes for Gaussian Blur
kernel_sizes = [(3, 3), (5, 5), (7, 7)]
blurred_images = []

# Apply Gaussian Blur with different kernel sizes
for kernel_size in kernel_sizes:
    blur = cv2.GaussianBlur(img, kernel_size, 0)
    blurred_images.append(blur)

plt.figure(figsize=(15, 10))

# Plot original image and Gaussian Blurred images
plt.subplot(2, 4, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # Convert 'BGR -> RGB' for matplotlib
plt.title("Original Gaussian Blur Image")
plt.axis('off')

for i, kernel in enumerate(kernel_sizes):
    plt.subplot(2, 4, i + 2)
    plt.imshow(cv2.cvtColor(blurred_images[i], cv2.COLOR_BGR2RGB))  # Convert BGR -> RGB
    plt.title(f'Gaussian {kernel[0]}, {kernel[1]}')
    plt.axis('off')

plt.tight_layout()
plt.show()
