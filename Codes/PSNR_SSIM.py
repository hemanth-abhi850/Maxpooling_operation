import numpy as np
import cv2
from skimage.metrics import structural_similarity as ssim

def calculate_psnr(original, approx):
    """Computes the Peak Signal-to-Noise Ratio (PSNR) between two images."""
    mse = np.mean((original - approx) ** 2)  # Mean Squared Error (MSE)
    if mse == 0:  # If images are identical
        return float("inf")

    max_pixel = 255.0  # Maximum pixel value for 8-bit images
    psnr = 20 * np.log10(max_pixel / np.sqrt(mse))  # PSNR formula
    return psnr

def calculate_ssim(original, approx):
    """Computes the Structural Similarity Index (SSIM) between two images."""
    original_gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY) if len(original.shape) == 3 else original
    approx_gray = cv2.cvtColor(approx, cv2.COLOR_BGR2GRAY) if len(approx.shape) == 3 else approx

    score, _ = ssim(original_gray, approx_gray, full=True)
    return score

# Load the image (Assuming it's already loaded as a NumPy array)
# image = cv2.imread("your_image.png", cv2.IMREAD_GRAYSCALE)

pool_size = (2, 2)

# Perform Exact and Approximate Max Pooling
exact_pooled_image = exact_pooled_image  ## original  image
approx_pooled_image = approx_pooled_image   ## approximate image

# Compute PSNR
psnr_value = calculate_psnr(exact_pooled_image, approx_pooled_image)
ssim_value = calculate_ssim(exact_pooled_image, approx_pooled_image)
print(f"PSNR between Exact and Approximate Average Pooling: {psnr_value:.2f} dB")
print(f"Structural Similarity Index (SSIM)  : {ssim_value:.4f} dB")
