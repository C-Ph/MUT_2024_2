import cv2
import matplotlib.pyplot as plt

# Load the images
img1 = cv2.imread('data/base_0.jpg',0)
img2 = cv2.imread('data/test_1.jpg',0)#test_2.jpg

# Calculate the histograms, and normalize them
##hist_img1 = cv2.calcHist([img1], [0, 1, 2], None, [256, 256, 256], [0, 256, 0, 256, 0, 256])
##cv2.normalize(hist_img1, hist_img1, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
##hist_img2 = cv2.calcHist([img2], [0, 1, 2], None, [256, 256, 256], [0, 256, 0, 256, 0, 256])
##cv2.normalize(hist_img2, hist_img2, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

hist_img1 = cv2.calcHist(img1, [0], None, [256], [0,256])
cv2.normalize(hist_img1, hist_img1, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
hist_img2 = cv2.calcHist(img2, [0], None, [256], [0,256])
cv2.normalize(hist_img2, hist_img2, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

# Find the metric value
metric_val1 = cv2.compareHist(hist_img1, hist_img2, cv2.HISTCMP_CORREL)
metric_val2 = cv2.compareHist(hist_img1, hist_img2, cv2.HISTCMP_CHISQR)
metric_val3 = cv2.compareHist(hist_img1, hist_img2, cv2.HISTCMP_INTERSECT)
metric_val4 = cv2.compareHist(hist_img1, hist_img2, cv2.HISTCMP_BHATTACHARYYA)
print("Correlation =", metric_val1)
print("Chi Square =", metric_val2)
print("Intersection =", metric_val3)
print("Bhattacharyya =", metric_val4)

plt.subplot(221), plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)),
plt.title('Base_img')
plt.subplot(222), plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)),
plt.title('Tester_img')
plt.subplot(223), plt.hist(img1.ravel(),256,[0,256]),
plt.title('Base')
plt.subplot(224), plt.hist(img2.ravel(),256,[0,256]),
plt.title('Tester')
plt.show()
