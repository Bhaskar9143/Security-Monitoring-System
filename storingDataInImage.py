from PIL import Image
import stepic
from traversing import traverse
import os
def encode(image_path, data):
    with Image.open(image_path) as image:
        # Convert data to bytes
        data_bytes = data.encode('utf-8')
        
        # Embed the data into the image
        steg_image = stepic.encode(image, data_bytes)
        
        # Save the image with embedded data in the same file
        steg_image.save(image_path)
        print(f"Data embedded and saved in {image_path}")

def decode(image_path):
    with Image.open(image_path) as image:
        # Retrieve the hidden data
        hidden_data = stepic.decode(image)
        
        # Convert bytes back to string
        data = hidden_data
        return data
# List of messages to encode
# messages = ['Bhaskar', 'Lisa', 'Mark', 'Tina']
# pc = 0

# # Traverse the directory and get image paths
# image_info = traverse(r'D:\projects\facerec\test\homies_images')

# for img_info in image_info:
#     img_path = os.path.join(r'D:\projects\facerec\test\homies_images', img_info[0])
#     encode(img_path, messages[pc])
#     pc += 1

# for img_info in image_info:
#     img_path = os.path.join(r'D:\projects\facerec\test\homies_images', img_info[0])
#     decoded_message = decode(img_path)
#     print(f"Retrieved message from {img_info[0]}: {decoded_message}")

messages = ['0.05','0.30','0.31','0.55','0.57','0.59','1.15']
pc = 0

# Traverse the directory and get image paths
#image_info = traverse(r'D:\projects\facerec\test\images')

# for img_info in image_info:
#     img_path = os.path.join(r'D:\projects\facerec\test\images', img_info[0])
#     encode(img_path, messages[pc])
#     pc += 1
# for img in image_info:
#     img_path = os.path.join(r'D:\projects\facerec\test\images', img[0])
#     print(decode(img_path))