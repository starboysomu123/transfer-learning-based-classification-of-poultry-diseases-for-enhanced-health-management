====================================
🧠 POULTRYDETECT - AI Image Classifier
====================================

Project Title:
--------------
PoultryDetect: Transfer Learning-Based Classification of Poultry Diseases for Enhanced Health Management

Description:
------------
PoultryDetect is a Flask-based web application that allows users to upload images of chickens and detects common poultry diseases using a deep learning model (ResNet50 with Transfer Learning). This project aims to help poultry farmers identify diseases early and take preventive action.

Key Features:
-------------
✅ Upload an image of a chicken  
✅ AI model predicts one of the following conditions:
   - Healthy
   - Coccidiosis
   - Salmonella
   - New Castle Disease  
✅ Instant classification result on-screen  
✅ Simple and responsive web interface  
✅ Developed using Flask + TensorFlow + Keras + HTML/CSS  

Project Structure:
------------------
poultry-diseases/
│
├── app.py                        # Main Flask backend logic  
├── healthy_vs_rotten.h5         # Pretrained Keras model (ResNet50-based)  
│
├── static/                      # Static files (CSS, JS, Images)
│   ├── assets/                  # CSS and design-related assets
│   ├── uploads/                 # Uploaded user images
│
├── templates/                   # HTML pages rendered via Flask
│   ├── index.html               # Home page
│   ├── portfolio-details.html  # Prediction page
│   ├── blog-single.html        # About page
│   ├── blog.html               # Contact page
│
└── README.txt                   # Project overview and instructions


How to Run Locally:
-------------------
1. Install Python 3.10+ and pip
2. Install required packages:
        pip install flask tensorflow pillow numpy

3. Make sure `healthy_vs_rotten.h5` is in the project root.
4. Start the app:
        python app.py
5. Open a browser and go to:
        http://127.0.0.1:5000



Model Details:
--------------
- Base Model: ResNet50 (Pretrained on ImageNet)
- Fine-tuned for 4-class classification
- Input shape: 224x224x3
- Optimized using Keras Tuner (Hyperband)

Developer Info:
---------------
👩‍💻 Developed by: ANNAM SOMNATH  
🎓 Institution: SIDDARTHA INSTITUTE OF SCIENCE AND TECHNOLOGY  
📅 Year: 2025  
🌐 Tech Stack: Python, Flask, TensorFlow, HTML, CSS

License:
--------
This project is for academic and educational purposes.

