import base64
import google.generativeai as genai

def get_response_nutrition(image, prompt):
    try:
        model = genai.GenerativeModel('gemini-pro-vision')
        instances = [
            {
                "image": {"data": base64.b64encode(image.read()).decode('utf-8')},
                "prompt": prompt
            }
        ]
        response = model.generate_content(instances)
        return response.text
    except Exception as e:
        print(f"Error during API call: {e}")
        return None