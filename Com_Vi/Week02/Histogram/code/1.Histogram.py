import cv2 
from matplotlib import pyplot as plt 
img = cv2.imread('data/1.png',0)#1.png, 2.png, 3.png
  
# alternative way to find histogram of an image 
plt.hist(img.ravel(),256,[0,256]) 
plt.show() 
