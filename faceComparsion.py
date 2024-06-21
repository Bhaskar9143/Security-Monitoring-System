import face_recognition

def are_faces_same(image_path1, image_path2, tolerance=0.6):

    # Load the first image
    image1 = face_recognition.load_image_file(image_path1)
    # Load the second image
    image2 = face_recognition.load_image_file(image_path2)

    # Get the face encodings for each image (this assumes each image contains exactly one face)
    encodings1 = face_recognition.face_encodings(image1)
    encodings2 = face_recognition.face_encodings(image2)

    # If no faces are found in either image, return False
    
    if len(encodings1) == 0 or len(encodings2) == 0:
         return False

    # Compare the first face in each image
    match = face_recognition.compare_faces([encodings1[0]], encodings2[0], tolerance=tolerance)
#     print(match[0])
    return match[0]


