from PIL import Image
import numpy as np
import io

def prep_image(uploaded_file):
    if uploaded_file is not None:
        # Read the file as bytes
        if isinstance(uploaded_file, io.BytesIO):
            bytes_data = uploaded_file.getvalue()
        else:
            bytes_data = uploaded_file.read()
        
        image_parts = [
            {
                "mime_type": "image/jpeg",  # Assuming the uploaded file is always an image
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No File is uploaded!")

def prep_image_cnn(image):
    image = image.resize((224, 224))
    image_array = np.array(image) / 255.0
    image_array = np.expand_dims(image_array, axis=0)
    return image_array