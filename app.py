from flask import Flask, render_template, request, redirect, url_for, session
import os
import shutil
from videoToPhoto import extract_unique_faces
from comp import comp
import os
import threading

app = Flask(__name__)
UPLOAD_FOLDER = r'.\static\uploads'
ALLOWED_EXTENSIONS_VIDEO = {'mp4', 'avi', 'mov'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#app.secret_key = os.urandom(48)  # Generate a random secret key for each run. Replace with a static key in production.

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
    extract_unique_faces(video_path, r'D:\projects\facerec\test4\images', interval=30, tolerance=0.6)
    homies_images = r'D:\projects\facerec\test4\homies_images'
    images = r'D:\projects\facerec\test4\images'
    messages = comp(homies_images, images)
    def send_message_thread():
        import pywhatkit as kit
        kit.sendwhatmsg_instantly('+919502237652',  "!! INTRUDER !! Please check, there is a new face detected whil", wait_time=20, tab_close=True)
    for i in messages:
        if i[:2]=="An":
            thread = threading.Thread(target=send_message_thread)
            thread.start()
            break
    return render_template('video_player.html', filename=filename, messages=messages)

if __name__ == '__main__':
    clear_folder(r'D:\projects\facerec\test4\images')  
    app.run(debug=True,host="0.0.0.0",port=8000)
