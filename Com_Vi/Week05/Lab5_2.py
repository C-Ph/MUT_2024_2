# Laplacian
'''จงแก้ไขโค้ด และแคปภาพผลลัพธ์จากการทำ Laplacian โดยใช้ภาพตัวเองและเปลี่ยนแปลงขนาดของหน้ากากของ Laplacian ให้ครบทุกแบบ
รูปตัวเอง'''

import numpy as np
import matplotlib.pyplot as plt


def apply_laplacian(image, kernel_type):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Define different Laplacian kernels
    kernels = {
        'basic': np.array([[0, 1, 0],
                          [1, -4, 1],
                          [0, 1, 0]]),
        
        'diagonal': np.array([[1, 1, 1],
                            [1, -8, 1],
                            [1, 1, 1]]),
        
        'extended': np.array([[0, 0, -1, 0, 0],
                            [0, -1, -2, -1, 0],
                            [-1, -2, 16, -2, -1],
                            [0, -1, -2, -1, 0],
                            [0, 0, -1, 0, 0]])
    }
    
    # Apply custom kernel
    laplacian = cv2.filter2D(gray, -1, kernels[kernel_type])
    
    # Normalize output
    laplacian = cv2.normalize(laplacian, None, 0, 255, cv2.NORM_MINMAX)
    
    return laplacian.astype(np.uint8)

# Read your image
image = cv2.imread('me.jpg')

# Apply different Laplacian kernels
basic_laplacian = apply_laplacian(image, 'basic')
diagonal_laplacian = apply_laplacian(image, 'diagonal')
extended_laplacian = apply_laplacian(image, 'extended')

# Display results
plt.figure(figsize=(12, 8))

plt.subplot(221)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(222)
plt.imshow(basic_laplacian, cmap='gray')
plt.title('Basic Laplacian (3x3)')
plt.axis('off')

plt.subplot(223)
plt.imshow(diagonal_laplacian, cmap='gray')
plt.title('Diagonal Laplacian (3x3)')
plt.axis('off')

plt.subplot(224)
plt.imshow(extended_laplacian, cmap='gray')
plt.title('Extended Laplacian (5x5)')
plt.axis('off')

plt.tight_layout()
plt.show()