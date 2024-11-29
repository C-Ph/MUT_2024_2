import cv2
import numpy as np
import matplotlib.pyplot as plt

#img = cv2.imread('.\\cat.jpg')
img = cv2.imread('/COD_E/001_Project/CLASS/Lab1/cat.jpg', -1)

#cv2.imshow("image", img[:,:,::-1])
#cv2.waitKey()
#cv2.destroyAllWindows()
plt.imshow(img[:,:,::-1])
plt.show()
