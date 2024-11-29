import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("data/test_2.jpg")
if img is None:
    print('Could not open or find the image:',)
    exit(0)
## [Resize image]
scale_percent = 100 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
src= cv.resize(img, dim, interpolation = cv.INTER_AREA)

## [Convert to grayscale]
src = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
## [Convert to grayscale]

## [Apply Histogram Equalization]
dst = cv.equalizeHist(src)
## [Apply Histogram Equalization]

## [Display results]
cv.imshow('Source image', src)
cv.imshow('Equalized Image', dst)
## [Display results]

## [Wait until user exits the program]
cv.waitKey()
## [Wait until user exits the program]
