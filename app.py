from flask import Flask, render_template, request, redirect, url_for, session
import os
import shutil
from videoToPhoto import extract_unique_faces
from traversing import *
from storingDataInImage import *
from faceComparsion import *
from comp import *
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.urandom(48)  # Generate a random secret key for each run. Replace with a static key in production.
UPLOAD_FOLDER = r'.\static\uploads'
ALLOWED_EXTENSIONS_VIDEO = {'mp4', 'avi', 'mov'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename, allowed_extensions):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

def clear_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form['user_id']
        password = request.form['password']
        if user_id == 'Bhaskar' and password == 'Bhaskar@123':
            session['logged_in'] = True
            return redirect(url_for('upload_file'))
        else:
            return "Invalid credentials, please try again."
    return render_template('login.html')

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        if 'file' in request.files:
            file = request.files['file']
            if file.filename == '':
                return redirect(request.url)
            if file and allowed_file(file.filename, ALLOWED_EXTENSIONS_VIDEO):
                filename = file.filename
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)
                return redirect(url_for('uploaded_file', filename=filename))
    
    return render_template('index.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    video_path = f"./static/uploads/{filename}"
    extract_unique_faces(video_path, r'D:\projects\facerec\test2\images', interval=30, tolerance=0.6)
    homies_images = r'D:\projects\facerec\test2\homies_images'
    images = r'D:\projects\facerec\test2\images'
    messages = comp(homies_images, images)
    return render_template('video_player.html', filename=filename, messages=messages)

if __name__ == '__main__':
    clear_folder(r'D:\projects\facerec\test2\images')  # Clear images folder on start
    app.run(debug=True)
