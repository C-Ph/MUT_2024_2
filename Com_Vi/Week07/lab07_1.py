# import cv2
# import numpy as np
# import time
# import matplotlib.pyplot as plt
# from matplotlib.image import imread

# # Start the timer
# start_time = time.time()

# # Image file path (using raw string to avoid escape sequence issues)
# image_file = r'file\img (2).jpg'
# input_image = imread(image_file)

# # Extract RGB channels
# r_img, g_img, b_img = input_image[:, :, 0], input_image[:, :, 1], input_image[:, :, 2]

# # Gamma correction parameters
# gamma = 1.400
# r_const, g_const, b_const = 0.2126, 0.7152, 0.0722

# # Apply gamma correction for grayscale conversion
# grayscale_image = r_const * (r_img ** gamma) + g_const * (g_img ** gamma) + b_const * (b_img ** gamma)

# # Plot original image and grayscale image
# fig1 = plt.figure(1)
# ax1, ax2 = fig1.add_subplot(121), fig1.add_subplot(122)
# ax1.imshow(input_image)
# ax2.imshow(grayscale_image, cmap='gray')
# plt.show()

# # Using OpenCV's Sobel filter
# sobelx = cv2.Sobel(grayscale_image, cv2.CV_64F, 1, 0, ksize=3)
# sobely = cv2.Sobel(grayscale_image, cv2.CV_64F, 0, 1, ksize=3)
# sobel_filtered_image_cv = np.sqrt(sobelx**2 + sobely**2)

# # Sobel kernel for manual convolution
# Gx = np.array([[1.0, 0.0, -1.0], [2.0, 0.0, -2.0], [1.0, 0.0, -1.0]])
# Gy = np.array([[1.0, 2.0, 1.0], [0.0, 0.0, 0.0], [-1.0, -2.0, -1.0]])

# # Manually applying Sobel filter (convolution)
# [rows, columns] = np.shape(grayscale_image)
# sobel_filtered_image = np.zeros(shape=(rows, columns))

# # Loop through image and apply convolution (can be slow for large images)
# for i in range(rows - 2):
#     for j in range(columns - 2):
#         gx = np.sum(np.multiply(Gx, grayscale_image[i:i + 3, j:j + 3]))
#         gy = np.sum(np.multiply(Gy, grayscale_image[i:i + 3, j:j + 3]))
#         sobel_filtered_image[i + 1, j + 1] = np.sqrt(gx ** 2 + gy ** 2)

# # Plot the results for Sobel filter comparison
# fig2 = plt.figure(2)
# ax1, ax2 = fig2.add_subplot(121), fig2.add_subplot(122)
# ax1.imshow(input_image)
# ax2.imshow(sobel_filtered_image, cmap='gray')
# plt.show()

# # Plot original, manual Sobel, and OpenCV Sobel results side by side
# fig3 = plt.figure(3)
# ax1, ax2, ax3 = fig3.add_subplot(131), fig3.add_subplot(132), fig3.add_subplot(133)
# ax1.imshow(input_image)
# ax2.imshow(sobel_filtered_image, cmap='gray')
# ax3.imshow(sobel_filtered_image_cv, cmap='gray')
# plt.show()

# # End the timer and calculate the elapsed time
# end_time = time.time()
# elapsed_time = end_time - start_time
# print(f"Runtime: {elapsed_time:.2f} seconds")



import cv2
import matplotlib.pyplot as plt
import numpy as np
import time
from matplotlib.image import imread

start_time_manual = time.time()

image_file = 'file/img (2).jpg'
input_image = imread(image_file)
[nx, ny, nz] = np.shape(input_image) 
r_img, g_img, b_img = input_image[:, :, 0], input_image[:, :, 1], input_image[:, :, 2]

gamma = 1.400 
r_const, g_const, b_const = 0.2126, 0.7152, 0.0722  
grayscale_image = r_const * r_img ** gamma + g_const * g_img ** gamma + b_const * b_img ** gamma

Gx = np.array([[1.0, 0.0, -1.0], [2.0, 0.0, -2.0], [1.0, 0.0, -1.0]])
Gy = np.array([[1.0, 2.0, 1.0], [0.0, 0.0, 0.0], [-1.0, -2.0, -1.0]])
[rows, columns] = np.shape(grayscale_image)  
sobel_manual = np.zeros(shape=(rows, columns))

for i in range(rows - 2):
    for j in range(columns - 2):
        gx = np.sum(np.multiply(Gx, grayscale_image[i:i + 3, j:j + 3]))  
        gy = np.sum(np.multiply(Gy, grayscale_image[i:i + 3, j:j + 3])) 
        sobel_manual[i + 1, j + 1] = np.sqrt(gx ** 2 + gy ** 2)

manual_time = time.time() - start_time_manual

# OpenCV implementation
start_time_opencv = time.time()

# Convert image to grayscale using OpenCV
gray_image = cv2.cvtColor(input_image, cv2.COLOR_RGB2GRAY)

# Apply Sobel operator
sobelx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
sobel_opencv = np.sqrt(sobelx**2 + sobely**2)

opencv_time = time.time() - start_time_opencv

# Plot results
plt.figure(figsize=(12, 4))
plt.subplot(131)
plt.imshow(input_image)
plt.title('Original Image')
plt.axis('off')

plt.subplot(132)
plt.imshow(sobel_manual, cmap='gray')
plt.title(f'Manual Sobel\nTime: {manual_time:.3f}s')
plt.axis('off')

plt.subplot(133)
plt.imshow(sobel_opencv, cmap='gray')
plt.title(f'OpenCV Sobel\nTime: {opencv_time:.3f}s')
plt.axis('off')

plt.tight_layout()
plt.show()
