import os

def change_extension_to_lowercase(directory):
    # Check if the directory exists
    if not os.path.exists(directory):
        print(f"Directory does not exist: {directory}")
        return

    for filename in os.listdir(directory):
        print(f"Processing file: {filename}")  # Debugging statement
        old_file_path = os.path.join(directory, filename)

        # Only process files, not directories
        if os.path.isfile(old_file_path):
            # Prepare the new filename with lowercase extension
            new_filename = f"{os.path.splitext(filename)[0]}.jpg"  # Change to .jpg
            new_file_path = os.path.join(directory, new_filename)
            
            # If the current file is not already in lowercase .jpg
            if filename.lower() != new_filename.lower():
                # Rename the file
                os.rename(old_file_path, new_file_path)
                print(f"Renamed: {old_file_path} -> {new_file_path}")
            else:
                print(f"Already in lowercase .jpg, skipping: {old_file_path}")

# Specify the directory containing your photos
photo_directory = r'C:\Users\stuar\OneDrive\Documents\GitHub\TravelWall\Media\Bordeaux'
change_extension_to_lowercase(photo_directory)
