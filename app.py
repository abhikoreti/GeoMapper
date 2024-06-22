from flask import Flask, request, render_template, send_from_directory
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os
from PIL import Image

app = Flask(__name__)

# Load your trained model
model = load_model('./mobilenetv2_best1.keras')

# Define the class names (UC Merced dataset has 21 classes)
class_names = [
    'agricultural', 'airplane', 'baseballdiamond', 'beach', 'buildings',
    'chaparral', 'denseresidential', 'forest', 'freeway', 'golfcourse',
    'harbor', 'intersection', 'mediumresidential', 'mobilehomepark',
    'overpass', 'parkinglot', 'river', 'runway', 'sparseresidential',
    'storagetanks', 'tenniscourt'
]

def model_predict(img_path, model):
    img = image.load_img(img_path, target_size=(224, 224))  # Adjust target size as per your model input
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = x / 255.0  # Normalize the image if your model was trained on normalized images
    preds = model.predict(x)
    return preds

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']
        
        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        upload_path = os.path.join(basepath, 'uploads')
        if not os.path.exists(upload_path):
            os.makedirs(upload_path)
        
        file_path = os.path.join(upload_path, f.filename)
        f.save(file_path)
        
        # If the file is a .tif, convert it to .png
        if file_path.endswith('.tif'):
            img = Image.open(file_path)
            png_path = file_path.rsplit('.', 1)[0] + '.png'
            img.save(png_path, 'PNG')
            file_path = png_path
        
        # Make prediction
        preds = model_predict(file_path, model)
        pred_class = np.argmax(preds, axis=1)[0]
        result = class_names[pred_class]  # Get the class name
        
        return render_template('index.html', result=result, image_url=os.path.basename(file_path))
    return render_template('index.html', result=None, image_url=None)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    basepath = os.path.dirname(__file__)
    return send_from_directory(os.path.join(basepath, 'uploads'), filename)

if __name__ == '__main__':
    app.run(debug=True)
