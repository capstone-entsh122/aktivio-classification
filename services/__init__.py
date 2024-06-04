import requests
from config import Config

def get_nutrition_info(food_item):
    response = requests.post(
        Config.GEMINI_AI_API_URL,
        headers={"Authorization": f"Bearer {Config.GEMINI_AI_API_KEY}"},
        json={"food_item": food_item}
    )
    
    if response.status_code == 200:
        return response.json()
    else:
        return None
