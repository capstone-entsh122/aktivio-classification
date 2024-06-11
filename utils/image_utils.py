from PIL import Image
import numpy as np

def prep_image(uploaded_file, mime_type):
    # Read the file as bytes
    bytes_data = uploaded_file.read()
    return bytes_data

def prep_image_cnn(image):
    image = image.resize((224, 224))
    image_array = np.array(image) / 255.0
    image_array = np.expand_dims(image_array, axis=0)
    return image_array