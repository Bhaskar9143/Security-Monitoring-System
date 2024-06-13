from traversing import traverse
from faceComparsion import are_faces_same
from storingDataInImage import decode_image

def comp(homies_images, images):
    x = traverse(homies_images)
    y = traverse(images)
    for img in y:
        bfg = 0
        for pc in x:
            img_path = rf"D:\projects\facerec\test\homies_images\{pc[0]}"
            pc_path = rf"D:\projects\facerec\test\images\{img[0]}"
            if are_faces_same(img_path, pc_path):
                decoded_text = decode_image(img_path)
                if decoded_text:
                    print(decoded_text + " is here to visit you")
                else:
                    print("Marker not found in", img_path)
                bfg = 1
                break
        if bfg == 0:
            print("An intruder is here")
        else:
            break

comp(r'D:\projects\facerec\test\homies_images', r'D:\projects\facerec\test\images')
