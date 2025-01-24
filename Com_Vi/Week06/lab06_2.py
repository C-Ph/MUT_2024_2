import numpy as np
import cv2

img = cv2.imread('bb.jpg', cv2.IMREAD_GRAYSCALE)
image = img.astype(np.float64)
noise_std = 0.2
noise = np.random.rayleigh(noise_std, img.shape)
noisy_image = cv2.addWeighted(image, 1, noise, 70, 0.0).astype(np.uint8)

width = 500
height = 400
dim = (width, height)

resized_img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
resized_noise = cv2.resize(noise, dim, interpolation=cv2.INTER_AREA) 
resized_noisy = cv2.resize(noisy_image, dim, interpolation=cv2.INTER_AREA)

cv2.imshow('Image', resized_img)
cv2.imshow('Noise', resized_noise)
cv2.imshow('Noisy Image', resized_noisy)
cv2.waitKey(0)
