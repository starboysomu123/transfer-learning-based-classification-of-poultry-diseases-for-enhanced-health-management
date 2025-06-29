import os
import numpy as np
import tensorflow as tf
from flask import Flask, render_template, request
from keras.preprocessing.image import load_img, img_to_array

# Initialize Flask app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Load your saved model
model = tf.keras.models.load_model("healthy_vs_rotten.h5")

# Class labels in the same order as training
labels = ['Coccidiosis', 'Healthy', 'New Castle Disease', 'Salmonella']

# Function to preprocess and predict
def get_model_prediction(image_path):
    img = load_img(image_path, target_size=(224, 224))
    x = img_to_array(img)
    x = np.expand_dims(x, axis=0)  # Batch dimension
    predictions = model.predict(x, verbose=0)
    predicted_class = np.argmax(predictions)
    return labels[predicted_class]

# Home Page
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/about')
def about():
    return render_template("blog-single.html")

@app.route('/contact')
def contact():
    return render_template("blog.html")

# Get Started → Upload Page
@app.route('/predict-page')
def predict_page():
    return render_template("portfolio-details.html")

# Predict Route
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files['pc_image']
        filename = file.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        prediction = get_model_prediction(filepath)

        # Send prediction and image back to contact.html
        return render_template("contact.html", predict=prediction, image_name=filename)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
