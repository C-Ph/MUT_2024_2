# #ทำงานร่วมกับรูปภาพของตนเอง ตัวอย่าง

# def apply_filter(image, filter_size, mode):
#     def get_window(x, y):
#         window = []
#         for i in range(-half_size, half_size + 1):
#             for j in range(-half_size, half_size + 1):
#                 xi = min(max(x + i, 0), rows - 1)
#                 yj = min(max(y + j, 0), cols - 1)
#                 window.append(image[xi][yj])
#         return window

#     # Validate inputs
#     if filter_size % 2 == 0:
#         raise ValueError("Filter size must be an odd integer.")

#     half_size = filter_size // 2
#     rows, cols = len(image), len(image[0])
#     filtered_image = [[0 for _ in range(cols)] for _ in range(rows)]

#     for x in range(rows):
#         for y in range(cols):
#             window = get_window(x, y)

#             if mode == 'median':
#                 filtered_image[x][y] = sorted(window)[len(window) // 2]
#             elif mode == 'max':
#                 filtered_image[x][y] = max(window)
#             elif mode == 'min':
#                 filtered_image[x][y] = min(window)
#             else:
#                 raise ValueError("Mode must be 'median', 'max', or 'min'.")

#     return filtered_image

# if __name__ == "__main__":
#     input_image = [
#         [1, 2, 3, 4, 5],
#         [6, 7, 8, 9, 10],
#         [11, 12, 13, 14, 15],
#         [16, 17, 18, 19, 20],
#         [21, 22, 23, 24, 25]
#     ]

#     filter_size = 3

#     print("Original Image:")
#     for row in input_image:
#         print(row)

#     median_filtered = apply_filter(input_image, filter_size, 'median')
#     print("\nMedian Filtered Image:")
#     for row in median_filtered:
#         print(row)

#     max_filtered = apply_filter(input_image, filter_size, 'max')
#     print("\nMax Filtered Image:")
#     for row in max_filtered:
#         print(row)

#     min_filtered = apply_filter(input_image, filter_size, 'min')
#     print("\nMin Filtered Image:")
#     for row in min_filtered:
#         print(row)