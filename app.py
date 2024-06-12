import os
import google.generativeai as genai
import tensorflow as tf
import mimetypes
from flask import Flask, request, jsonify
import numpy as np
from PIL import Image
import json

from models.gemini_ai import get_response_nutrition
from utils.image_utils import prep_image, prep_image_cnn
os.environ["CUDA_VISIBLE_DEVICES"] = "-1" 
app = Flask(__name__)

# Load model CNN
model_path = "aktivio9986.h5"
cnn_model = tf.keras.models.load_model(model_path)

# Set API Key
# GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"] = "AIzaSyBSlPzxVot-SwXlFevsUAnq53S58yjojUM"
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

@app.route('/api/classify', methods=['POST'])
def predict():
   
    # Get the uploaded file
    uploaded_file = request.files['image']

    # Open and display the uploaded image
    image = Image.open(uploaded_file)

    # Preprocess the image for CNN model
    image_for_cnn = prep_image_cnn(image)

    # Classify the image using the CNN model
    predictions = cnn_model.predict(image_for_cnn)
    class_idx = np.argmax(predictions, axis=1)[0]
    class_labels = [
        'Ayam Goreng', 'Bakso', 'Bubur Ayam', 'Mi Goreng', 'Nasi Putih', 'Sate', 'Soto', 'Telur Dadar', 'Telur Mata Sapi',
        'bakwan', 'batagor', 'bihun goreng', 'ca sayur', 'cake', 'cumi asam manis', 'cumi goreng tepung', 'dimsum', 'donat',
        'gado gado', 'ikan goreng', 'kentang goreng', 'martabak', 'mie ayam', 'nasi goreng', 'nasi kuning', 'nasi padang',
        'pecel', 'pempek', 'pepes ikan', 'perkedel', 'rawon', 'rendang', 'salad buah', 'sayur asem', 'singkong goreng',
        'sop daging sapi', 'tempe goreng', 'tongseng kambing', 'yoghurt'
    ]
    class_label = class_labels[class_idx]

    # Determine the MIME type of the file
    # mime_type, _ = mimetypes.guess_type(uploaded_file.filename)
    
     # Preprocess the image for Gemini AI model
    image_data = prep_image(uploaded_file)

    # Prompt Template
    input_prompt_nutrition = f"""
    Anda adalah seorang Ahli Gizi yang ahli. Sebagai ahli gizi yang terampil, Anda diharuskan untuk menganalisis makanan dalam gambar dan menentukan nilai gizi total.
    Gambar ini memperlihatkan {class_label}.
    Silakan berikan rincian dari jenis makanan yang ada dalam {class_label} beserta kandungan gizinya.
    Berikut kata yang harus ditampilkan :
    Ukuran porsi, Kalori, Protein, Lemak, Karbohidrat, Serat
    tampilkan dalam bentuk raw string JSON
    """

    # Get the nutrition response
    response = get_response_nutrition(image_data, input_prompt_nutrition)
    
    cleaned_response = json.loads(response.replace("\n", "").replace('"', '\\"'))
       

    return jsonify({"class_label": class_label, "nutrition_response": cleaned_response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)