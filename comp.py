# comp.py

from PIL import Image
from faceComparsion import *
from traversing import *
from storingDataInImage import *
# from whatsapp import send_whatsapp_message
#from abcd import send_whatsapp_message  # Importing the send_whatsapp_message function from abcd.py
#import pywhatkit as kit

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
    rt = 0
    messages = []
    for img in y:
        pc_path = rf"D:\projects\facerec\test4\images\{img[0]}"
        dl = read_image_metadata(pc_path).get("Elapsed Time", "Unknown Time")
        bfg = 0
        for pc in x:
            img_path = rf"D:\projects\facerec\test4\homies_images\{pc[0]}"
            if are_faces_same(img_path, pc_path):
                decoded_text = decode(img_path)
                if decoded_text:
                    messages.append(f"{decoded_text} is here to visit you at {dl}")
                else:
                    messages.append(f"Marker not found in {img_path} at {dl}")
                bfg = 1

        if bfg == 0:
            messages.append(f"An intruder is here at {dl}")
            # send_whatsapp_message('+919502237652', "!! INTRUDER !!")
           # kit.sendwhatmsg_instantly('9502237652', 'message', wait_time=0, tab_close=True)
            #send_whatsapp_message(phone_number, f"An intruder is detected at {dl}")  # Sending WhatsApp message

    return messages
# Example usage:
