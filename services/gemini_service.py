from models.text_generator import generate_text

def get_food_description(food_type):
    prompt = f"Tell me about {food_type} as a dish, including its nutrition and calories."
    return generate_text(prompt)