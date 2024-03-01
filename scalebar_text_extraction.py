import pytesseract
from skimage import io, color, filters
from skimage.transform import resize
import numpy as np

# Function to process the image and extract the scale bar text
def extract_scale_bar_text(image_path):
    # Load the image
    image = io.imread(image_path)
    
    # If the image is not in grayscale, convert it
    if len(image.shape) == 3:
        image = color.rgb2gray(image)
    
    # Invert the image if necessary (ensure text is white and background is black)
    if np.mean(image) > 0.5:
        image = 1 - image
    
    # Apply a threshold to create a binary image
    thresh = filters.threshold_otsu(image)
    binary = image > thresh
    
    # Resize and crop the image to where the scale bar text is expected
    # These values might need to be adjusted depending on the image's layout
    height, width = binary.shape
    cropped = binary[int(height * 0.8):, int(width * 0.2):int(width * 0.8)]
    
    # Use pytesseract to extract text
    text = pytesseract.image_to_string(cropped, config='--psm 11')
    
    return text

# Replace 'image_path' with the path to your image
image_path = '/Users/issamhammadi/Documents/GitHub/code/Database/image_compressed.jpg'
scale_bar_text = extract_scale_bar_text(image_path)
print("Detected scale bar text:", scale_bar_text)