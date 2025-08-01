import os
import numpy as np
from flask import Flask, request, render_template, jsonify, redirect
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import tensorflow as tf

# Initialize Flask app
app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load model and class labels
model = load_model('best_model.h5')
class_names = ['carton', 'metal', 'plastico', 'vidrio']

# Info for trash types
trash_info = {
    'carton': "📦 Carton is recyclable. Flatten it before disposal.",
    'metal': "🔩 Metals like cans and foils should be rinsed and recycled.",
    'plastico': "🧴 Plastics vary by type. Check local recycling codes.",
    'vidrio': "🍾 Glass is fully recyclable. Remove lids and rinse first."
}

# Prediction logic
def model_predict(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = tf.expand_dims(image.img_to_array(img), 0)
    preds = model.predict(img_array)
    pred_idx = np.argmax(preds[0])
    confidence = 100 * np.max(preds[0])
    return class_names[pred_idx], confidence

# Routes
@app.route('/')
def root():
    return redirect('/home')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['image']
        if file:
            filename = file.filename
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(path)
            prediction, confidence = model_predict(path)
            return render_template('index.html',
                                   filename=filename,
                                   prediction=prediction,
                                   confidence=confidence,
                                   trash_info=trash_info[prediction])
    return render_template('index.html')

@app.route('/webcam')
def webcam():
    return render_template('webcam.html')

@app.route('/predict_webcam', methods=['POST'])
def predict_webcam():
    file = request.files['image']
    if file:
        path = os.path.join(app.config['UPLOAD_FOLDER'], 'webcam.jpg')
        file.save(path)
        prediction, confidence = model_predict(path)
        return jsonify({'prediction': prediction, 'confidence': confidence})
    return jsonify({'error': 'No image received'})

if __name__ == '__main__':
    app.run(debug=True)
