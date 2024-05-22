from flask import Blueprint, request, render_template, jsonify
from config import Config
import os
import requests

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/')
def index():
    return render_template('index.html')

@main_blueprint.route('/generate', methods=['POST'])
def generate():
    prompt = request.json.get('prompt')
    response = call_gradient_ai(prompt)
    return jsonify(response)

def call_gradient_ai(prompt):
    max_tokens = int(os.getenv('MAX_TOKENS', Config.MAX_TOKENS))
    temperature = float(os.getenv('TEMPERATURE', Config.TEMPERATURE))
    
    # Simulate a call to the GradientAI model (replace with actual API call)
    api_url = "http://api.gradientai.com/llama-3-8b-instruct"
    headers = {"Authorization": "Bearer YOUR_API_KEY"}  # If API key is needed
    data = {
        "prompt": prompt,
        "max_tokens": max_tokens,
        "temperature": temperature
    }

    response = requests.post(api_url, json=data, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to get response from the model"}
