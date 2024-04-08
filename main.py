# Since we are proceeding with only the two available images, let's load them and align horizontally
from PIL import Image
import os

# Define the paths to the available images
image_paths = [
    '/mnt/data/image1.png',  # First image
    '/mnt/data/image.png',   # Second image
]

# Load the images
images = [Image.open(path) for path in image_paths]

# Find the smallest height
min_height = min(img.height for img in images)

# Resize the images to have the same height
resized_images = [img.resize((int(img.width * min_height / img.height), min_height)) for img in images]

# Create a new image with the combined width of both images and the minimum height
combined_width = sum(img.width for img in resized_images)
combined_image = Image.new('RGB', (combined_width, min_height))

# Paste the images into the combined image
x_offset = 0
for img in resized_images:
    combined_image.paste(img, (x_offset, 0))
    x_offset += img.width

# Save the combined image to a file
combined_image_path = '/mnt/data/combined_image.png'
combined_image.save(combined_image_path)

# Return the path to the saved image
combined_image_path

