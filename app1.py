from flask import Flask, render_template, request, redirect, url_for
from PIL import Image
import stepic
import os

app = Flask(__name__)

# Function to encode data into the image
def encode(image_path, data):
    with Image.open(image_path) as image:
        # Convert data to bytes
        data_bytes = data.encode('utf-8')
        
        # Embed the data into the image
        steg_image = stepic.encode(image, data_bytes)
        
        # Save the image with embedded data in the specified directory
        steg_image.save(image_path)
        print(f"Data embedded and saved in {image_path}")

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'Bhaskar' or request.form['password'] != 'Bhaskar@123':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('upload_image'))
    return render_template('login1.html', error=error)

@app.route('/upload_image', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        # Get the uploaded image and name
        image = request.files['image']
        name = request.form['name']
        
        # Ensure the file extension is .png
        image.filename = 'uploaded_image.png'
        
        # Save the image file to the specified directory
        image_path = os.path.join('D:\\', 'projects', 'facerec', 'test2', 'homies_images', image.filename)
        image.save(image_path)
        
        # Perform encoding with the provided name
        encode(image_path, name)
        
        # Redirect to a success page or perform any other actions
        return 'Image uploaded and encoded successfully!'
    return render_template('upload_image.html')

if __name__ == '__main__':
    app.run(debug=True)
