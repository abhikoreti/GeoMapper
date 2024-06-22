# GeoMapper

This project is a Flask web application for classifying remote sensing images using a pre-trained MobileNetV2 model. Users can upload an image, and the application will classify it according to one of the classes from the UC Merced Land Use Dataset. This is a personal project to show case my M.Tech thesis work on remote sensing image classification.

## Project Structure

   > Directory Tree Structure

     \project_directory
     ├── \static
     │   ├── styles.css
     ├── \templates
     │   └── index.html
     ├── \uploads
     ├── app.py
     ├── mobilenetv2_best1.keras
     ├── requirements.txt
     ├── vercel.json
     ├── .gitignore
     └── README.md

## Features

- Upload an image for classification.
- Supports `.tif` image files and converts them to `.png` for display.
- Classifies images into 21 classes from the UC Merced Land Use Dataset.
- Displays the uploaded image and the classification result.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt

4. **Ensure the model file is in place**:
   Place the mobilenetv2_best1.keras file in the root of your project directory.

## Usage

1. **Run the Flask application**:
   ```bash
   python app.py
   
2. Open a web browser and navigate to http://127.0.0.1:5000/.

3. Upload an image using the provided form and view the classification result.
