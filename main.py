from PIL import Image
import os
import subprocess
import piexif
from datetime import datetime

def format_creation_date(original_creation_date):
    return datetime.strptime(original_creation_date, '%Y:%m:%d %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')

def get_image_attributes(image_path):
    try:
        # Open the image
        image = Image.open(image_path)

        # Get image size in MB
        size_mb = os.path.getsize(image_path) / (1024 * 1024)

        # Get width and height of the image
        width, height = image.size

        # Get image modification date
        modification_date = os.path.getmtime(image_path)

        # Get EXIF metadata of the image
        exif_bytes = image.info.get("exif")

        # Convert EXIF metadata from bytes to dictionary
        exif_dict = {}
        if exif_bytes:
            exif_dict = piexif.load(exif_bytes)

        # Extract original creation date from EXIF metadata
        original_creation_date = exif_dict["Exif"].get(piexif.ExifIFD.DateTimeOriginal, "Unknown").decode()

        # Format modification date
        modification_date_formatted = datetime.fromtimestamp(modification_date).strftime('%Y-%m-%d %H:%M:%S')

        # Format original creation date
        original_creation_date_formatted = format_creation_date(original_creation_date)

        # Change the creation date of the file
        subprocess.run(["touch", "-d", original_creation_date_formatted, image_path])

        # Print the attributes
        print_image_attributes(size_mb, width, height, original_creation_date_formatted, modification_date_formatted)

    except Exception as e:
        print(f"Error while getting image attributes: {e}")

def print_image_attributes(size_mb, width, height, original_creation_date_formatted, modification_date_formatted):
    print(f"Image size: {size_mb:.2f} MB")
    print(f"Width: {width} pixels")
    print(f"Height: {height} pixels")
    print(f"Original creation date: {original_creation_date_formatted}")
    print(f"Modification date: {modification_date_formatted}")

if __name__ == "__main__":
    # image_path = input("Enter the image path: ").strip()
    image_path = '/home/jean/Pictures/IMG_20141121_223739.jpg'.strip()
    get_image_attributes(image_path)
