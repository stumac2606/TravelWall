from PIL import Image
import os

def reduce_image_size(input_path, output_path, quality=85):
    """
    Reduces the memory size of an image by adjusting its quality.

    Parameters:
    input_path (str): Path to the input image.
    output_path (str): Path to save the output image.
    quality (int): Quality of the output image (1-95).

    Returns:
    None
    """
    # Open an image file
    with Image.open(input_path) as img:
        # Convert PNG to JPEG to reduce size, PNG is lossless so changing quality won't work
        if img.format == 'PNG':
            img = img.convert('RGB')
            output_path = output_path.replace('.png', '.jpg')

        # Save the image with the specified quality
        img.save(output_path, quality=quality, optimize=True)

        print(f"Image saved to {output_path} with quality {quality}")

def process_images(input_directory, output_directory, quality=85):
    """
    Processes all images in the input directory and saves the compressed images to the output directory.

    Parameters:
    input_directory (str): Path to the input directory containing images.
    output_directory (str): Path to the output directory to save compressed images.
    quality (int): Quality of the output image (1-95).

    Returns:
    None
    """
    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Process each image in the input directory
    for filename in os.listdir(input_directory):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            input_path = os.path.join(input_directory, filename)
            output_path = os.path.join(output_directory, filename)
            reduce_image_size(input_path, output_path, quality)

# Example usage:
input_directory = 'C:/Users/stuar/OneDrive/Documents/GitHub/TravelWall/Media'
output_directory = 'C:/Users/stuar/OneDrive/Documents/GitHub/TravelWall/Media/lowres'
quality = 85  # Adjust this value as needed, lower means more compression and smaller file size

process_images(input_directory, output_directory, quality)
