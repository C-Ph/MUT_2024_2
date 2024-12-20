'''จงหาตัวอย่างภาพที่นำมาทดสอบกับการทำ Unsharp masking 
และ Highboost Filteringของโค้ดตัวอย่างเพื่อให้เห็นผลลัพธ์ที่ชัดเจน 
และแคปภาพผลลัพธ์มาใส่ในคำตอบด้านล่าง [แก้ไขโค้ดให้แสดงภาพจากภายนอกด้วย เช่น eye.jpg]'''

import numpy as np
import cv2
import matplotlib.pyplot as plt

def apply_filter(image, kernel):
    height, width = image.shape
    kernel_size = kernel.shape[0]
    pad = kernel_size // 2
    padded_image = np.pad(image, pad, mode='constant', constant_values=0)
    output = np.zeros_like(image, dtype=np.float32)
    
    for i in range(height):
        for j in range(width):
            region = padded_image[i:i + kernel_size, j:j + kernel_size]
            output[i, j] = np.sum(region * kernel)
    
    return output

def unsharp_masking(image, kernel_size=3, alpha=1.5):
    kernel = np.ones((kernel_size, kernel_size)) / (kernel_size ** 2)
    blurred_image = apply_filter(image, kernel)
    mask = image - blurred_image
    sharpened_image = image + alpha * mask
    return np.clip(sharpened_image, 0, 255)

def highboost_filtering(image, kernel_size=3, k=1.5):
    kernel = np.ones((kernel_size, kernel_size)) / (kernel_size ** 2)
    blurred_image = apply_filter(image, kernel)
    mask = image - blurred_image
    highboost_image = image + k * mask
    return np.clip(highboost_image, 0, 255)

# Read and process image
image = cv2.imread("eye.jpg", cv2.IMREAD_GRAYSCALE)
image = cv2.resize(image, (400, 300))

# Apply filters
sharpened = unsharp_masking(image, kernel_size=3, alpha=1.5)
highboost = highboost_filtering(image, kernel_size=3, k=2.0)

# Display results
plt.figure(figsize=(15, 5))

plt.subplot(131)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(132)
plt.imshow(sharpened, cmap='gray')
plt.title('Unsharp Masking')
plt.axis('off')

plt.subplot(133)
plt.imshow(highboost, cmap='gray')
plt.title('Highboost Filtering')
plt.axis('off')

plt.tight_layout()
plt.show()
