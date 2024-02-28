from email.mime import image
import numpy as np 
import matplotlib.pyplot as plt 
from skimage import io, color
from skimage.filters import threshold_otsu
from scipy.ndimage import binary_fill_holes
from skimage.measure import find_contours 
from skimage import measure
from skimage.morphology import remove_small_objects
from skimage import filters
from PIL import Image


# Function to calculate distance from a point to a horizontal line y = constant
def distance_to_horizontal_line(point, y_constant):
    return abs(point[0] - y_constant)  # point[1] is the y-coordinate of the point

# Function to calculate distance from a point to a vertical line x = constant
def distance_to_vertical_line(point, x_constant):
    return abs(point[1] - x_constant)  # point[0] is the x-coordinate of the point

def trim_subcontour(subcontour):
    total_points = len(subcontour)
    remove_count = int(total_points * 0.1)  # 10% from each side

    # Remove 10% from start and 10% from end
    trimmed_subcontour = subcontour[remove_count:-remove_count]
    return trimmed_subcontour


def seperate4(contour):
    # Assuming 'contour' is a list of (y, x) points
    contour_array = np.array(largest)  # Convert to NumPy array for easier calculations
    #center_y, center_x = np.mean(contour_array, axis=0)

    # Assuming 'contour' is a list of (y, x) points from your contour detection
    min_y = min(contour_array, key=lambda point: point[0])[0]
    max_y = max(contour_array, key=lambda point: point[0])[0]
    min_x = min(contour_array, key=lambda point: point[1])[1]
    max_x = max(contour_array, key=lambda point: point[1])[1]

    north_subcontour = []
    south_subcontour = []
    east_subcontour = []
    west_subcontour = []
    # Iterate through each point in the contour
    for point in contour_array:
        # Calculate distances to each line
        distance_to_ymin = distance_to_horizontal_line(point, min_y)
        distance_to_ymax = distance_to_horizontal_line(point, max_y)
        distance_to_xmin = distance_to_vertical_line(point, min_x)
        distance_to_xmax = distance_to_vertical_line(point, max_x)

        # Find the minimum distance and corresponding direction
        min_distance = min(distance_to_ymin, distance_to_ymax, distance_to_xmin, distance_to_xmax)
        if min_distance == distance_to_ymin:
            north_subcontour.append(point)
        elif min_distance == distance_to_ymax:
            south_subcontour.append(point)
        elif min_distance == distance_to_xmin:
            west_subcontour.append(point)
        elif min_distance == distance_to_xmax:
            east_subcontour.append(point)

    return north_subcontour, south_subcontour, west_subcontour, east_subcontour


def compress_and_resize_image(input_image_path, output_image_path, base_width, quality):
    """
    Compress and resize an image.
    
    :param input_image_path: str, The path of the image to be processed.
    :param output_image_path: str, The path to save the compressed and resized image.
    :param base_width: int, The new width of the image. The height will be set proportionally.
    :param quality: int, The quality of the compressed image (1 to 100).
    """
    # Open the image
    img = Image.open(input_image_path)
    
    # Calculate the height using the new width to maintain the aspect ratio
    w_percent = (base_width / float(img.size[0]))
    h_size = int((float(img.size[1]) * float(w_percent)))
    
    # Resize the image using Resampling.LANCZOS for high quality
    img = img.resize((base_width, h_size), Image.Resampling.LANCZOS)
    
    # Save the image with compression
    img.save(output_image_path, quality=quality, optimize=True)
    return output_image_path
    

def find_boundaries_scalebar(image_path, width,quality, sigma_value,correction_value,max_pix,P):
    Image.MAX_IMAGE_PIXELS = None
    outputPath = "/Users/issamhammadi/Documents/GitHub/code/Database/imageMacCompressed.jpg"
    # compression of the image, check the function in image_outil for more documentation
    compress_and_resize_image(image_path, outputPath, width,quality)
    #Read compressed image 
    RGB = io.imread(outputPath)
    #convert image to grayscale
    I = color.rgb2gray(RGB)
    #removing image noise with a blur
    # Apply Gaussian blur with a specified sigma value
    IG = filters.gaussian(I, sigma=sigma_value) 
    #convert image to binary image
    thres = threshold_otsu(IG)
    thres_prime = thres
    print(" thresholding value = ", thres)
    #here I add a value to optimise the algorithm to my set of images
    #Verification of thres not exceeding 1 
    if (thres * correction_value <1):
        thres = thres * correction_value
        print("everything is okay!!")
    else:
        thres = thres
        print("!Adjust the correction!")

    BW = IG > thres
    #Fill the holes in the binary image
    BW2 = binary_fill_holes(BW)
    #Remove small objects from binary image
    BW3 = remove_small_objects(BW2, max_pix, connectivity=8) 
    #find contours 
    contours = find_contours(BW3, P)
    print("number of closed contours found is: ", len(contours))
    #Sorting contours in a decreasing way
    sorted_contours = sorted(contours, key=lambda x: len(x), reverse=True)
    # Getting only the largest contour
    largest_contour = sorted_contours[0]

    #detecting the scalebar
    binary_image = I < thres_prime
    label_image = measure.label(binary_image)
    regions = measure.regionprops(label_image)

    max_length = 0
    largest_rectangle = None

    # Iterate through region properties to find and plot rectangles
    for region in regions:
        # Get the dimensions of the bounding box
        minr, minc, maxr, maxc = region.bbox
        width = maxc - minc
        height = maxr - minr

        # Calculate width to height ratio
        ratio = width / float(height) if width < height else height / float(width)

        # Update criteria to include orientation for horizontal rectangles
        if 0.005 <= ratio <= 0.10:
            # Check if this rectangle is the largest one found so far
            length = max(width, height)  # Use the longer dimension as the 'length'
            if length > max_length:
                max_length = length
                largest_rectangle = region  # Store the region object of the largest rectangle
        # Define your rectangle-detection criteria (adjust these values as needed)
    return thres, outputPath, largest_contour, largest_rectangle

image_path = "/Users/issamhammadi/Documents/GitHub/code/Database/micrographies/253-sel1-600°C_image golbale_0.jpg"
entered_longueur = 3000
quality =100
entered_sigma = 0
entered_correction = 1.25
entered_P = 0.8
entered_max_pixel = 100

thres, output_path, largest, largest_rectangle =find_boundaries_scalebar(image_path,entered_longueur,quality, entered_sigma ,entered_correction,entered_max_pixel,entered_P)



"""
for y, x in contour_array:
    if y < center_y:
        north_subcontour.append((x, y))
    else:
        south_subcontour.append((x, y))

    if x < center_x:
        west_subcontour.append((x, y))
    else:
        east_subcontour.append((x, y))

original_image = io.imread(output_path)
"""

#print(south_subcontour)
"""
# Determine thresholds for what constitutes 'near' an edge - this could be a percentage of the total size
y_threshold = (max_y - min_y) * 0.4 # Adjust thresholds based on your data specifics
x_threshold = (max_x - min_x) * 0.02
print(f"y thres = {y_threshold}")
print(f"x thres = {x_threshold}")
print(f"length of the contour = {len(contour_array)}")

top_subcontour = [pt for pt in contour_array if pt[0] <= min_y + y_threshold]
bottom_subcontour = [pt for pt in contour_array if pt[0] >= max_y - y_threshold]
left_subcontour = [pt for pt in contour_array if pt[1] <= min_x + x_threshold]
right_subcontour = [pt for pt in contour_array if pt[1] >= max_x - x_threshold]
"""

original_image = io.imread(output_path)
north_subcontour, south_subcontour, west_subcontour, east_subcontour = seperate4(largest)

# Plotting
plt.figure(figsize=(10, 6))  # Adjust the size as needed

# Show the original image
plt.imshow(original_image, cmap='gray')  # Adjust colormap as needed


# Plot each subcontour with different colors
plt.scatter(*zip(*[(y, x) for x, y in north_subcontour]), color='blue', label='Nord', s =1)
plt.scatter(*zip(*[(y, x) for x, y in south_subcontour]), color='green', label='Sud', s = 1)
plt.plot(*zip(*[(y, x) for x, y in west_subcontour]), color='red', label='Ouest')
plt.plot(*zip(*[(y, x) for x, y in east_subcontour]), color='yellow', label='Est')


# Add additional plot settings
plt.legend()
plt.axis('image')
plt.show()