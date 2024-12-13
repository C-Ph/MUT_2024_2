import numpy as np

# Define the input image and kernel
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
    # Output size calculation (without padding)
    output_height = image_height - kernel_height + 1
    output_width = image_width - kernel_width + 1
    # Prepare the output array
    output = np.zeros((output_height, output_width), dtype=int)
    # Perform the convolution
    for i in range(output_height):
        for j in range(output_width):
            region = image[i:i+kernel_height, j:j+kernel_width]
            output[i, j] = np.sum(region * kernel)
    return output

# Perform convolution
output_image = convolve2d_no_padding(image, kernel)

# Display results
print("Original Image:")
print(image)
print("\nKernel:")
print(kernel)
print("\nOutput Image:")
print(output_image)