import cv2
import face_recognition
import os
import glob
from PIL import Image, PngImagePlugin
from traversing import *
def clear_output_folder(output_folder):
    """
    Clears all files in the output folder.
    """
    files = glob.glob(f"{output_folder}/*")
    for f in files:
        os.remove(f)

def extract_unique_faces(video_path, output_folder=r"D:\projects\facerec\test2\images", interval=0, tolerance=0.1):
    """
    Extract unique faces from a video at given interval.

    Parameters:
    - video_path: Path to the video file.
    - output_folder: Folder to save the extracted frames.
    - interval: Number of frames to skip between each extraction.
    - tolerance: How much distance between faces to consider it a match. Lower is more strict. 0.6 is typical best performance.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    else:
        clear_output_folder(output_folder)

    video_capture = cv2.VideoCapture(video_path)
    fps = video_capture.get(cv2.CAP_PROP_FPS)
    frame_count = 0
    saved_count = 0
    known_face_encodings = []

    while video_capture.isOpened():
        ret, frame = video_capture.read()
        if not ret:
            break

        if frame_count % interval == 0:
            # Convert the frame from BGR (OpenCV format) to RGB (face_recognition format)
            rgb_frame = frame[:, :, ::-1]

            # Find all the faces and face encodings in the current frame
            face_locations = face_recognition.face_locations(rgb_frame)
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

            for face_location, face_encoding in zip(face_locations, face_encodings):
                # Check if this face is a match for any known face
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=tolerance)
                
                if not any(matches):
                    # Save the face if this is a new face
                    top, right, bottom, left = face_location
                    face_image = frame[top:bottom, left:right]
                    face_path = f"{output_folder}/face_{saved_count}.png"
                    cv2.imwrite(face_path, face_image)

                    # Calculate the elapsed time in the video
                    elapsed_time = frame_count / fps
                    minutes = int(elapsed_time // 60)
                    seconds = int(elapsed_time % 60)
                    time_text = f"{minutes:02}:{seconds:02}"

                    # Add elapsed time to image metadata
                    pil_image = Image.open(face_path)
                    metadata = PngImagePlugin.PngInfo()
                    metadata.add_text("Elapsed Time", time_text)
                    pil_image.save(face_path, pnginfo=metadata)
                    
                    saved_count += 1
                    # Add the face encoding to the known faces list
                    known_face_encodings.append(face_encoding)

        frame_count += 1

    video_capture.release()

# Example usage:
# video_path = r"D:\projects\facerec\Bhuvans_video.mp4"
# output_folder = r"D:\projects\facerec\test\images"

# Extract unique faces from the video
# extract_unique_faces(video_path, output_folder, interval=30, tolerance=0.6)
