from flask import Flask, request, jsonify
from models.food_classifier import classify_image
from services.gemini_service import get_food_description

app = Flask(__name__)

@app.route('/classify', methods=['POST'])
def classify_food():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    img = request.files['image']
    food_type = classify_image(img)
    description = get_food_description(food_type)
    
    return jsonify({
        'food_type': food_type,
        'description': description
    })

if __name__ == '__main__':
    app.run(debug=True)