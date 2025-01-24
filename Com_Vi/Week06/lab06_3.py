import numpy as np
import cv2
import matplotlib.pyplot as plt

def add_salt_and_pepper_noise(image, salt_probability, pepper_probability):
    noisy_image = np.copy(image)
    rows, cols = image.shape[:2]

    for i in range(rows):
        for j in range(cols):
            r = np.random.random()

            if r < salt_probability:
                noisy_image[i, j] = 255
            elif r < salt_probability + pepper_probability:
                noisy_image[i, j] = 0

    return noisy_image

image = cv2.imread('bb.jpg', cv2.IMREAD_GRAYSCALE)
salt_probability = 0.02
pepper_probability = 0.02
noisy_image = add_salt_and_pepper_noise(image, salt_probability, pepper_probability)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(noisy_image, cmap='gray')
plt.title('Image with Salt-and-Pepper Noise')
plt.axis('off')

plt.tight_layout()
plt.show()
