import numpy as np
import cv2
import matplotlib.pyplot as plt
from skimage.metrics import peak_signal_noise_ratio as psnr, structural_similarity as ssim


def Max_pooling_colour(a, b, c, d):
    x = Max_operator6(a, b)
    y = Max_operator6(c, d)
    z = Max_operator6(x, y)
    return z

def Max_pooling_colour_aprx(a1, a2, a3, a4,a5,a6,a7,a8,a9):
    y1 = Max_operator_aprx(a1, a2)
    y2 = Max_operator_aprx(a3, a4)
    y3 = Max_operator_aprx(a5, a6)
    y4 = Max_operator_aprx(a7, a8)
    y5 = Max_operator_aprx(y1, y2)
    y6 = Max_operator_aprx(y3, y4)
    y7 = Max_operator_aprx(y5, y6)
    z  = Max_operator_aprx(y7, a9)
    return z

def Max_pooling_colour_aprx1(a1, a2, a3, a4,a5,a6,a7,a8,a9):
    y1 = Max_operator_aprx1(a1, a2)
    y2 = Max_operator_aprx1(a3, a4)
    y3 = Max_operator_aprx1(a5, a6)
    y4 = Max_operator_aprx1(a7, a8)
    y5 = Max_operator_aprx1(y1, y2)
    y6 = Max_operator_aprx1(y3, y4)
    y7 = Max_operator_aprx1(y5, y6)
    z  = Max_operator_aprx1(y7, a9)
    return z
import numpy as np

def max_pooling_original_colour3(image, pool_size=3):
    height, width, channels = image.shape
    new_height, new_width = height // pool_size, width // pool_size
    result = np.zeros((new_height, new_width, channels), dtype=np.uint8)

    for c in range(channels):
        for i in range(new_height):
            for j in range(new_width):
                region = image[i * pool_size:(i + 1) * pool_size, j * pool_size:(j + 1) * pool_size, c]
                result[i, j, c] = np.max(region)

    return result

def max_pooling_proposed_colour3(image, pool_size=3):
    height, width, channels = image.shape
    new_height, new_width = height // pool_size, width // pool_size

    # Pad image to ensure 3x3 regions exist everywhere
    pad_h = (pool_size - height % pool_size) % pool_size
    pad_w = (pool_size - width % pool_size) % pool_size

    padded_image = np.pad(image, ((0, pad_h), (0, pad_w), (0, 0)), mode='constant', constant_values=0)
    result = np.zeros((new_height, new_width, channels), dtype=np.uint8)

    for c in range(channels):
        for i in range(new_height):
            for j in range(new_width):
                region = padded_image[i * pool_size:(i + 1) * pool_size, j * pool_size:(j + 1) * pool_size, c]

                if region.shape == (3, 3):
                    # Extract 9 elements from the 3x3 region
                    r1, r2, r3 = region[0, 0], region[0, 1], region[0, 2]
                    r4, r5, r6 = region[1, 0], region[1, 1], region[1, 2]
                    r7, r8, r9 = region[2, 0], region[2, 1], region[2, 2]
                else:
                    # Handle cases where region is not exactly 3x3
                    region_flattened = region.flatten()
                    while len(region_flattened) < 9:
                        region_flattened = np.append(region_flattened, 0)  # Pad with zeros
                    r1, r2, r3, r4, r5, r6, r7, r8, r9 = region_flattened[:9]

                # Compute max pooling based on your approximation function
                # result[i, j, c] = Max_pooling_colour(r1, r2, r3, r4, r5, r6, r7, r8, r9)
                result[i, j, c] = Max_pooling_colour_aprx1(r1, r2, r3, r4, r5, r6, r7, r8, r9)

    return result



