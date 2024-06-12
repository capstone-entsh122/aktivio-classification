import google.generativeai as genai
import json
import re

def get_response_nutrition(image_data, prompt):
    try:
        model = genai.GenerativeModel('gemini-pro-vision')
        response = model.generate_content([image_data[0], prompt])
        # Clean the response string
        cleaned_response = re.sub(r'\n|\s+', ' ', response.text).strip()

        # Parse the cleaned response into a JSON object
        nutrition_data = json.loads(cleaned_response)
        return nutrition_data
    except Exception as e:
        print(f"Error during API call: {e}")
        return None