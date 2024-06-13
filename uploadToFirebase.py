import firebase_admin
from firebase_admin import credentials, firestore, storage
import os
from PIL import Image
import json

from traversing import traverse

def upload_image_to_firebase():
    try:
        local_images = "./homies_images/"
        images = traverse(local_images)
        bucket = storage.bucket()
        
        download_urls = []

        for filename, _ in images:
            blob = bucket.blob(f"homies/{filename}")
            blob.upload_from_filename(f"{local_images}{filename}")

            blob.make_public()
            download_urls.append(blob.public_url)
            print(f"Uploaded {filename} and it can be accessed at {blob.public_url}")
        
        return download_urls

    except Exception as e:
        print(e)
        return []

if __name__ == '__main__':
    cred = credentials.Certificate(r'D:\projects\facerec\test\credentials.json')
    firebase_admin.initialize_app(cred, {
        'storageBucket': 'human-intruder-detection.appspot.com'
    })
    urls = upload_image_to_firebase()
    