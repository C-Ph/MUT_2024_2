import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('D:/COD_E/001_Project/CLASS_2024/Comvi/Week04/me.jpg')

blur_5x5 = cv2.blur(img, (5, 5))        # ขนาดหน้ากาก 5x5
blur_25x25 = cv2.blur(img, (25, 25))    # 25x25
blur_55x55 = cv2.blur(img, (55, 55))    # 55x55

'''เมื่อขนาดหน้ากากใหญ่ขึ้น ภาพจะถูกทำให้เบลอ (blurred) มากขึ้น'''

# แสดงภาพต้นฉบับและภาพที่ทำการ Smoothing 
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)) 
plt.title('Original Image')
plt.xticks([]), plt.yticks([])

plt.subplot(2, 2, 2)
plt.imshow(cv2.cvtColor(blur_5x5, cv2.COLOR_BGR2RGB))
plt.title('Blurred with 5x5 Kernel')
plt.xticks([]), plt.yticks([])

plt.subplot(2, 2, 3)
plt.imshow(cv2.cvtColor(blur_25x25, cv2.COLOR_BGR2RGB))
plt.title('Blurred with 25x25 Kernel')
plt.xticks([]), plt.yticks([])

plt.subplot(2, 2, 4)
plt.imshow(cv2.cvtColor(blur_55x55, cv2.COLOR_BGR2RGB))
plt.title('Blurred with 55x55 Kernel')
plt.xticks([]), plt.yticks([])

plt.tight_layout()
plt.show()