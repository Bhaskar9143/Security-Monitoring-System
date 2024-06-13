import os
from PIL import Image

def traverse(directory):
    results = []
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(directory, filename)
            with Image.open(image_path) as img:
                # print(f"Processing {filename} with size {img.size}")
                results.append((filename, img.size))
    return results