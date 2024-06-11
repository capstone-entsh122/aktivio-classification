import google.generativeai as genai

def get_response_nutrition(image_data, prompt):
    try:
        model = genai.GenerativeModel('gemini-pro-vision')
        response = model.generate_content([image_data[0], prompt])
        return response.text
    except Exception as e:
        print(f"Error during API call: {e}")
        return None