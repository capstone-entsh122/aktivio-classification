import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    GEMINI_AI_API_URL = "https://api.gemini.ai/v1/nutrition"
    GEMINI_AI_API_KEY = os.environ.get('GEMINI_AI_API_KEY')
    MODEL_PATH = 'path_to_your_model.h5'
