import base64
import google.generativeai as genai


import base64

def get_response_nutrition(image_bytes, prompt, mime_type):
    try:
        model = genai.GenerativeModel('gemini-pro-vision')
        instances = [
            {
                "content": [
                    {
                        "blob": {
                            "mime_type": mime_type,
                            "data": base64.b64encode(image_bytes).decode('utf-8')
                        }
                    },
                    {
                        "text": prompt
                    }
                ]
            }
        ]
        response = model.generate_content(instances)
        return response.text
    except Exception as e:
        print(f"Error during API call: {e}")
        return None