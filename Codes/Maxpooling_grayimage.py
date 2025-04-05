import numpy as np
import cv2
import matplotlib.pyplot as plt
from skimage.metrics import peak_signal_noise_ratio as psnr, structural_similarity as ssim


def Max_pooling_gray(a, b, c, d):
    x = Max_operator6(a, b)
    y = Max_operator6(c, d)
    z = Max_operator6(x, y)
    return z

def Max_pooling_gray_aprx(a, b, c, d):
    x = Max_operator_aprx1(a, b)
    y = Max_operator_aprx1(c, d)
    z = Max_operator_aprx1(x, y)
    return z

def max_pooling_original(image, pool_size):
    height, width = image.shape[:2]
    new_height, new_width = height // pool_size, width // pool_size
    result = np.zeros((new_height, new_width), dtype=np.uint8)

    for i in range(new_height):
        for j in range(new_width):
            region = image[i * pool_size:(i + 1) * pool_size, j * pool_size:(j + 1) * pool_size]
            result[i, j] = np.max(region)

    return result

def max_pooling_proposed(image, pool_size):
    height, width = image.shape[:2]
    new_height, new_width = height // pool_size, width // pool_size
    result = np.zeros((new_height, new_width), dtype=np.uint8)

    for i in range(new_height):
        for j in range(new_width):
            region = image[i * pool_size:(i + 1) * pool_size, j * pool_size:(j + 1) * pool_size]
            result_A, result_B, result_C, result_D = region[0, 0], region[0, 1], region[1, 0], region[1, 1]
            #result[i, j] = Max_pooling_gray(result_A, result_B, result_C, result_D)
            result[i, j] = Max_pooling_gray_aprx(result_A, result_B, result_C, result_D)

    return result

def main():
    image = cv2.imread('kodim5.png', cv2.IMREAD_GRAYSCALE)

    exact_pooled = max_pooling_original(image, pool_size=2)
    approx_pooled = max_pooling_proposed(image, pool_size=2)

    psnr_value = psnr(exact_pooled, approx_pooled)
    ssim_value = ssim(exact_pooled, approx_pooled)

    print(f'PSNR between exact and approximate pooling: {psnr_value:.2f} dB')
    print(f'SSIM between exact and approximate pooling: {ssim_value:.4f}')

    plt.figure(figsize=(10, 4))
    plt.subplot(1, 3, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Original Image')

    plt.subplot(1, 3, 2)
    plt.imshow(exact_pooled, cmap='gray')
    plt.title('Exact Max Pooling')

    plt.subplot(1, 3, 3)
    plt.imshow(approx_pooled, cmap='gray')
    plt.title('Proposed Max Pooling')

    plt.show()

if __name__ == '__main__':
    main()
