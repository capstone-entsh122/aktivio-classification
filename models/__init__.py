from tensorflow.keras.models import load_model
from config import Config

model = load_model(Config.MODEL_PATH)
