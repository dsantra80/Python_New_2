from flask import Blueprint, request, render_template, jsonify
from config import Config
import os

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
    
    # Simulate a response from the GradientAI model
    response = {
        "prompt": prompt,
        "response": f"This is a generated response to the prompt: {prompt}",
        "max_tokens": max_tokens,
        "temperature": temperature
    }
    return response
