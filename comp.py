from PIL import Image
from faceComparsion import *
from traversing import *
from  storingDataInImage import *
def read_image_metadata(image_path):
    """
    Read metadata from an image.

    Parameters:
    - image_path: Path to the image file.

    Returns:
    - metadata: A dictionary containing the image metadata.
    """
    with Image.open(image_path) as img:
        metadata = img.info
    return metadata

def comp(homies_images, images):
    x = traverse(homies_images)
    y = traverse(images)
    messages = []
    for img in y:
        pc_path = rf"D:\projects\facerec\test\images\{img[0]}"
        dl = read_image_metadata(pc_path).get("Elapsed Time", "Unknown Time")
        bfg = 0
        for pc in x:
            img_path = rf"D:\projects\facerec\test\homies_images\{pc[0]}"
            if are_faces_same(img_path, pc_path):
                decoded_text = decode(img_path)
                if decoded_text:
                    messages.append(f"{decoded_text} is here to visit you at {dl}")
                else:
                    messages.append(f"Marker not found in {img_path} at {dl}")
                bfg = 1
                
        if bfg == 0:
            messages.append(f"An intruder is here at {dl}")
    return messages
