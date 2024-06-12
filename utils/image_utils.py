import base64
from PIL import Image
import numpy as np
import io

def prep_image(uploaded_file):
    if uploaded_file is not None:
        # Open the image using PIL
        image = Image.open(uploaded_file)

        # Convert the image to JPEG format
        with io.BytesIO() as output:
            image.convert('RGB').save(output, format='JPEG')
            image_data = output.getvalue()

        # Encode the image data as base64
        base64_image = base64.b64encode(image_data).decode('utf-8')

        image_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64_image
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No File is uploaded!")

# def prep_image(uploaded_file):
#     if uploaded_file is not None:
#         # Read the file as bytes
#         bytes_data = uploaded_file.getvalue()
#         image_parts = [
#             {
#                 "mime_type": uploaded_file.type,
#                 "data": bytes_data
#             }
#         ]
#         return image_parts
#     else:
#         raise FileNotFoundError("No File is uploaded!")

def prep_image_cnn(image):
    image = image.resize((224, 224))
    image_array = np.array(image) / 255.0
    image_array = np.expand_dims(image_array, axis=0)
    return image_array