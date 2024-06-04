from flask import Blueprint, request, jsonify
from models import model
from services import get_nutrition_info
from helpers import preprocess_image
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import io

def init_routes(app):
    main = Blueprint('main', __name__)

    @main.route("/classify", methods=["POST"])
    def classify_image():
        if 'file' not in request.files:
            return jsonify({"error": "No file part"}), 400

        file = request.files['file']
        
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400

        try:
            # Read the image file
            image = Image.open(io.BytesIO(file.read()))
            
            # Preprocess the image
            processed_image = preprocess_image(image, target_size=(224, 224))  # Adjust the target size as needed
            
            # Make predictions
            predictions = model.predict(processed_image)
            # Assume the model returns a list of probabilities for each class
            predicted_class = np.argmax(predictions, axis=1)[0]
            predicted_probability = np.max(predictions)
            
            # Map the predicted class to a food item name
            # This should match the classes used during model training
            class_names = ["apple", "banana", "burger", "carrot", "pizza"]  # Update this list based on your model
            food_item = class_names[predicted_class]
            
            # Get nutrition information from Gemini AI
            nutrition_info = get_nutrition_info(food_item)
            
            if not nutrition_info:
                return jsonify({"error": "Failed to get nutrition information from Gemini AI"}), 500

            # Combine the results
            result = {
                "predictions": {
                    "class": food_item,
                    "probability": float(predicted_probability)
                },
                "nutrition_info": nutrition_info
            }

            # Return the results as JSON
            return jsonify(result), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    app.register_blueprint(main)
