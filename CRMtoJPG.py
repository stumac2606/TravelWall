import os
import rawpy
from PIL import Image

# Directory containing the .CR3 files
input_directory = r"C:\Users\stuar\OneDrive\Documents\GitHub\TravelWall\Media\Bordeaux"
output_directory = r"C:\Users\stuar\OneDrive\Documents\GitHub\TravelWall\Media\Bordeaux"

# Make sure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# Loop through all files in the input directory
for filename in os.listdir(input_directory):
    if filename.lower().endswith(".cr3"):
        input_path = os.path.join(input_directory, filename)
        
        # Read the .CR3 file using rawpy
        with rawpy.imread(input_path) as raw:
            # Convert the raw image to RGB
            rgb_image = raw.postprocess()

            # Create the output path for the jpg file
            output_filename = os.path.splitext(filename)[0] + ".jpg"
            output_path = os.path.join(output_directory, output_filename)

            # Save the image using Pillow
            image = Image.fromarray(rgb_image)
            image.save(output_path, "JPEG")
            print(f"Converted {filename} to {output_filename}")

print("All .CR3 files have been converted to .jpg")
