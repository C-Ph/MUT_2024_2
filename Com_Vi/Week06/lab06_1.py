import numpy as np
import matplotlib.pyplot as plt
import cv2

def add_gaussian_noise(image, mean=0, sigma=25):
    row, col, ch = image.shape
    gauss = np.random.normal(mean, sigma, (row, col, ch))
    noisy = np.clip(image + gauss, 0, 255)
    return noisy.astype(np.uint8)

image = cv2.imread('bb.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Define mean and sigma values
mean_values = [0, 10, 50]
sigma_values = [10, 25, 50]

# Set up the figure with subplots
fig, axs = plt.subplots(len(mean_values), len(sigma_values), figsize=(15, 10))

# Display the original image
axs[0, 0].imshow(image)
axs[0, 0].set_title("Original Image")
axs[0, 0].axis('off')

# Apply and display noisy images for each mean and sigma
index = 1
for i, mean in enumerate(mean_values):
    for j, sigma in enumerate(sigma_values):
        noisy_image = add_gaussian_noise(image, mean, sigma)
        axs[i, j].imshow(noisy_image)
        axs[i, j].set_title(f"Mean={mean}, Sigma={sigma}")
        axs[i, j].axis('off')

plt.tight_layout()
plt.show()
