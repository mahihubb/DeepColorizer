from flask import Flask, request, render_template, send_from_directory, redirect, url_for
import os
from werkzeug.utils import secure_filename
import cv2
import numpy as np

app = Flask(__name__)

# Ensure the uploads folder exists
UPLOAD_FOLDER = './uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Max upload size 16MB

# Load the colorization model once during app initialization
print("Loading models...")
net = cv2.dnn.readNetFromCaffe('./models/models_colorization_deploy_v2.prototxt',
                               './models/colorization_release_v2.caffemodel')
pts = np.load('./models/pts_in_hull.npy')

class8 = net.getLayerId("class8_ab")
conv8 = net.getLayerId("conv8_313_rh")
pts = pts.transpose().reshape(2, 313, 1, 1)

net.getLayer(class8).blobs = [pts.astype("float32")]
net.getLayer(conv8).blobs = [np.full([1, 313], 2.606, dtype="float32")]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return 'No file uploaded'

    file = request.files['file']
    if file.filename == '':
        return 'No selected file'

    if file:
        # Secure the filename to prevent issues
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        # Save the uploaded file to the upload folder
        file.save(file_path)

        # Perform colorization
        colorized_image_path = colorize_image(file_path)

        # Redirect to results page with both images
        return redirect(url_for('result', original_image=filename, colorized_image=colorized_image_path))

def colorize_image(image_path):
    # Load the black & white image
    image = cv2.imread(image_path)
    scaled = image.astype("float32") / 255.0
    lab = cv2.cvtColor(scaled, cv2.COLOR_BGR2LAB)

    resized = cv2.resize(lab, (224, 224))
    L = cv2.split(resized)[0]
    L -= 50

    # Feed L channel into the model
    net.setInput(cv2.dnn.blobFromImage(L))
    ab = net.forward()[0, :, :, :].transpose((1, 2, 0))

    # Resize result back to original image size
    ab = cv2.resize(ab, (image.shape[1], image.shape[0]))

    L = cv2.split(lab)[0]
    colorized = np.concatenate((L[:, :, np.newaxis], ab), axis=2)
    colorized = cv2.cvtColor(colorized, cv2.COLOR_LAB2BGR)
    colorized = np.clip(colorized, 0, 1)

    colorized = (255 * colorized).astype("uint8")

    # Save colorized image in the same upload folder
    colorized_filename = f'colorized_{os.path.basename(image_path)}'
    colorized_path = os.path.join(app.config['UPLOAD_FOLDER'], colorized_filename)
    cv2.imwrite(colorized_path, colorized)

    return colorized_filename

# Route to serve the uploaded images from the uploads folder
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/result')
def result():
    original_image = request.args.get('original_image')
    colorized_image = request.args.get('colorized_image')
    return render_template('result.html', original_image=original_image, colorized_image=colorized_image)

if __name__ == '__main__':
    app.run(debug=True)
