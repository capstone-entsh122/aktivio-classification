import numpy as np
from tensorflow import MobileNetV2, preprocess_input, decode_predictions
from utils.image_utils import load_and_preprocess_image

model = MobileNetV2(weights='imagenet')

def classify_image(img_file):
    img_array = load_and_preprocess_image(img_file)
    predictions = model.predict(img_array)
    decoded = decode_predictions(predictions, top=1)[0]
    return decoded[0][1]  # food type