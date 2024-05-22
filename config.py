from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    MAX_TOKENS = os.getenv('MAX_TOKENS', 100)
    TEMPERATURE = os.getenv('TEMPERATURE', 0.7)
