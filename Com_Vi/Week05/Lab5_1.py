'''จงปรับปรุงโค้ดเพื่อนำ Midpoint filter เพิ่มมาอีก 1 อัลกอริทึม 
และปรับปรุงให้โค้ดทำงานร่วมกับรูปภาพของตนเอง และปรับปรุงการแสดงผลให้แสดงภาพผลลัพธ์แทนอาเรย์ จากนั้นนำโค้ดที่แก้ไข และผลลัพธ์ที่ได้มาใส่ด้านล่าง
รูปตัวเอง'''

# import numpy as np
# from scipy.ndimage import median_filter, maximum_filter, minimum_filter
# import matplotlib.pyplot as plt

# def apply_median_filter(image, size):
#     return median_filter(image, size=size)

# def apply_max_filter(image, size):
#     return maximum_filter(image, size=size)

# def apply_min_filter(image, size):
#     return minimum_filter(image, size=size)

# # Example usage
# def main():
#     np.random.seed(0)
#     image = np.random.randint(0, 256, (10, 10), dtype=np.uint8)
#     print("Original Image:\n", image)
#     filter_size = 3 #คิดเป็นเลขคี่เพื่อหาจุดตรงกลาง

#     median_filtered = apply_median_filter(image, size=filter_size)
#     max_filtered = apply_max_filter(image, size=filter_size)
#     min_filtered = apply_min_filter(image, size=filter_size)

#     print("\nMedian Filtered Image:\n", median_filtered)
#     print("\nMax Filtered Image:\n", max_filtered)
#     print("\nMin Filtered Image:\n", min_filtered)

#     plt.figure(figsize=(10, 8))

#     plt.subplot(2, 2, 1)
#     plt.title("Original Image")
#     plt.imshow(image, cmap="gray")
#     plt.colorbar()

#     plt.subplot(2, 2, 2)
#     plt.title("Median Filtered")
#     plt.imshow(median_filtered, cmap="gray")
#     plt.colorbar()

#     plt.subplot(2, 2, 3)
#     plt.title("Max Filtered")
#     plt.imshow(max_filtered, cmap="gray")
#     plt.colorbar()

#     plt.subplot(2, 2, 4)
#     plt.title("Min Filtered")
#     plt.imshow(min_filtered, cmap="gray")
#     plt.colorbar()

#     plt.tight_layout()
#     plt.show()

# if __name__ == "__main__":
#     main()


import numpy as np
from scipy.ndimage import median_filter, maximum_filter, minimum_filter
import matplotlib.pyplot as plt
from PIL import Image


def apply_median_filter(image, size):
    return median_filter(image, size=size)

def apply_max_filter(image, size):
    return maximum_filter(image, size=size)

def apply_min_filter(image, size):
    return minimum_filter(image, size=size)

def apply_midpoint_filter(image, size):
    min_filtered = minimum_filter(image, size=size)
    max_filtered = maximum_filter(image, size=size)
    return (min_filtered + max_filtered) / 2

def main():
    image = np.array(Image.open('me.jpg').convert('L'))
    filter_size = 3

    # Apply filters
    median_filtered = apply_median_filter(image, size=filter_size)
    max_filtered = apply_max_filter(image, size=filter_size)
    min_filtered = apply_min_filter(image, size=filter_size)
    midpoint_filtered = apply_midpoint_filter(image, size=filter_size)

    # Display results
    plt.figure(figsize=(10, 8))

    plt.subplot(2, 3, 1)
    plt.title("Original Image")
    plt.imshow(image, cmap="gray")
    plt.colorbar()

    plt.subplot(2, 3, 2)
    plt.title("Median Filtered")
    plt.imshow(median_filtered, cmap="gray")
    plt.colorbar()

    plt.subplot(2, 3, 3)
    plt.title("Max Filtered")
    plt.imshow(max_filtered, cmap="gray")
    plt.colorbar()

    plt.subplot(2, 3, 4)
    plt.title("Min Filtered")
    plt.imshow(min_filtered, cmap="gray")
    plt.colorbar()

    plt.subplot(2, 3, 5)
    plt.title("Midpoint Filtered")
    plt.imshow(midpoint_filtered, cmap="gray")
    plt.colorbar()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
